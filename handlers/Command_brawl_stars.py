from aiogram.types import Message, CallbackQuery
from aiogram import F, Bot
import os
from aiogram import types, exceptions, Router
from database import bd as db
from uttils import parser_profile_photo_and_name as pars
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from handlers.All_fsms_context import BrawlStarsID

rp = Router()
load_dotenv()
bot = Bot(token = os.getenv("TOKEN_API"))



# Обработчик команды Brawl Stars. Получает разметку от функции communication и отправляет ее пользователю.
async def brawl_stars_command_handler(message: Message):
    from battons.battons import communication
    markup = await communication()
    await message.answer("Выбери действие:", reply_markup = markup)

# Функция для парсинга фотографии профиля. Если происходит ошибка BadRequest, вызывается функция change_brawl_id.
async def pars_profile_photo(message: Message, profile_id, user_id):
    try:
        await pars.pars_profile_photo(profile_id)
        profile_photo = f"D:\Project\Tg-Brawl-Bot\profile_photos\{profile_id}.webp"
        await message.answer_photo(photo = types.FSInputFile(path = profile_photo))
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
    except exceptions.TelegramBadRequest:
        await change_brawl_id(message, user_id)

# Функция для изменения Brawl Stars ID пользователя в случае ошибки.
async def change_brawl_id(message: Message, user_id):
    await message.answer("Похоже вы указали не правильный Brawl Stars ID.")
    await message.answer("Напиши еще раз свой Brawl Stars ID(без #):")
    @rp.message(F.text)
    async def profile_bs_id(message: Message):
        brawl_id = str(message.text.upper())
        await db.save_brawl_stars_id_1(user_id, brawl_id)
        await pars_profile_photo(message, brawl_id, user_id)

# Обработчик кнопки. Удаляет предыдущее сообщение и отправляет новое с выбором Brawl Stars ID.
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    from battons.battons import brawl_stars_name
    user_id = call.from_user.id
    markup = await brawl_stars_name(user_id)
    await call.message.answer("Выберите Brawl Stars ID из доступных вам:", reply_markup = markup)

# Обработчик кнопки для добавления Brawl Stars ID. Устанавливает состояние и сохраняет user_id и nume.
async def handler_batton_add_brawl_id(call: CallbackQuery, state: FSMContext):
    await state.set_state(BrawlStarsID.brawl_id)
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = int(call.data.split("_")[-1])
    await call.message.answer("Напиши свой Brawl Stars ID(без #):")
    await db.save_user_id(user_id)
    await state.update_data(nume = nume, user_id = user_id)

# Обработчик для добавления Brawl Stars ID. Проверяет правильность ID и сохраняет его.
async def fsm_context_batton_add_brawl_id(message: Message, state: FSMContext):
    try:
        await state.update_data(brawl_id = message.text.upper())
        data = await state.get_data()
        nume = data["nume"]
        user_id = data["user_id"]
        brawl_id = data["brawl_id"]
        brawl_name = await pars.pars_profile_name(brawl_id)
        await db.__getattribute__(f"save_brawl_stars_name_{nume}")(brawl_name, user_id)
        os.remove(f"profile_names\{brawl_id}.html")
        await db.__getattribute__(f"save_brawl_stars_id_{nume}")(user_id, brawl_id)
        await pars_profile_photo(message, brawl_id, user_id)
        await state.clear()
    except AttributeError:
        await message.answer("Похоже вы отправили свой Brawl Stars ID не правильно😥\nПопробуйте еще раз.")

# Обработчик кнопки для отправки фотографии профиля.
async def handler_batton_send_profile_photo(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = int(call.data.split("_")[-1])
    brawl_id = str(await getattr(db, f'get_brawl_id_{nume}')(user_id))
    await pars_profile_photo(call.message, brawl_id, user_id)

# Обработчик кнопки "Назад". Удаляет предыдущее сообщение и отправляет новое с выбором действия.
async def handler_batton_back(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    from battons.battons import communication
    markup = await communication()
    await call.message.answer("Выбери действие:", reply_markup = markup)

# Обработчик кнопки "Изменить". Удаляет предыдущее сообщение и отправляет новое с выбором Brawl Stars ID.
async def handler_batton_change(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    from battons.battons import change_brawl_stars_name
    user_id = call.from_user.id
    markup = await change_brawl_stars_name(user_id)
    await call.message.answer("Выберите Brawl Stars ID из доступных вам:", reply_markup = markup)

# Функция для изменения Brawl Stars ID пользователя. Устанавливает состояние и сохраняет user_id и nume.
async def change_brawl_id(call: CallbackQuery, state: FSMContext):
    await state.set_state(BrawlStarsID.new_brawl_id)
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = int(call.data.split("_")[-1])
    await call.message.answer("Напиши свой новый Brawl Stars ID(без #):")
    await state.update_data(nume = nume, user_id = user_id)

# Функция для обработки нового Brawl Stars ID пользователя. Проверяет правильность ID и сохраняет его.
async def new_profile_bs_id(message: Message, state: FSMContext):
    try:
        await state.update_data(new_brawl_id = message.text.upper())
        data = await state.get_data()
        nume = data["nume"]
        user_id = data["user_id"]
        new_brawl_id = data["new_brawl_id"]
        await db.update_brawl_id(nume, new_brawl_id, user_id)
        brawl_name = await pars.pars_profile_name(new_brawl_id)
        if brawl_name is None:
            raise ValueError("Не удалось спарсить имя из-за неправильного ID")
        await db.__getattribute__(f"save_brawl_stars_name_{nume}")(brawl_name, user_id)
        os.remove(f"profile_names\{new_brawl_id}.html")
        await message.answer("Твой Brawl Stars ID успешно изменён😁👍")
        await state.clear()
    except (AttributeError, ValueError):
        await message.answer("Похоже вы отправили свой Brawl Stars ID не правильно😥\nПопробуйте еще раз.")

