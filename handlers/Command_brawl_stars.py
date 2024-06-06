from uttils import parser_profile_photo_and_name as pars
from handlers.All_fsms_context import BrawlStarsID
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import types, Router
from database import bd as db
from aiogram import F, Bot
from uttils.text import *
import os

from dotenv import load_dotenv

rp = Router()
load_dotenv()
bot = Bot(token = os.getenv("TOKEN_API"))



# Обработчик команды Brawl Stars. Получает разметку от функции communication и отправляет ее пользователю.
async def brawl_stars_command_handler_as_ru(call: CallbackQuery, bot: Bot):
    user_lang = "ru"
    data = await command_start(user_lang)
    text = data[1]
    from battons.battons import communication
    markup = await communication(user_lang)
    await bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = text, reply_markup = markup)

# Обработчик кнопки с выбором сохраненных Brawl Stars ID. Удаляет предыдущее сообщение и отправляет новое с выбором Brawl Stars ID.
async def batton(call: CallbackQuery, bot: Bot):
    user_lang = "ru"
    data = await command_start(user_lang)
    text = data[1]
    from battons.battons import brawl_stars_name
    user_id = call.from_user.id
    markup = await brawl_stars_name(user_id)
    await bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = text, reply_markup = markup)
    

# Обработчик кнопки для отправки фотографии профиля.
async def handler_batton_send_profile_photo(call: CallbackQuery, bot:Bot):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = int(call.data.split("_")[-1])
    brawl_id = str(await getattr(db, f'get_brawl_id_{nume}')(user_id))
    await pars_profile_photo(call.message, brawl_id, user_id)
    

# Обработчик кнопки для добавления Brawl Stars ID. Устанавливает состояние и сохраняет user_id и nume.
async def handler_batton_add_brawl_id(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(BrawlStarsID.brawl_id)
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = int(call.data.split("_")[-1])
    user_lang = call.from_user.language_code
    data = await command_brawl_stars(user_lang)
    text = data[5]
    await call.message.answer(text)
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
        cleaned_brawl_id = brawl_id.lstrip('#')
        brawl_name = await pars.pars_profile_name(cleaned_brawl_id)
        if brawl_name == None or brawl_name == "None":
            os.remove(f"profile_names\{cleaned_brawl_id}.html")
            raise Exception("Это искусственная ошибка")
        else:
            await db.__getattribute__(f"save_brawl_stars_name_{nume}")(brawl_name, user_id)
            await db.__getattribute__(f"save_brawl_stars_id_{nume}")(user_id, cleaned_brawl_id)
            await pars_profile_photo(message, cleaned_brawl_id, user_id)
            os.remove(f"profile_names\{cleaned_brawl_id}.html")
            await state.clear()  
    except (AttributeError, Exception):
        user_lang = message.from_user.language_code
        data = await command_brawl_stars(user_lang)
        text = data[6]
        await message.answer(text)

# Функция для парсинга фотографии профиля. Если происходит ошибка BadRequest, вызывается функция bad_brawl_id.
async def pars_profile_photo(message: Message, profile_id, user_id):
    await pars.pars_profile_photo(profile_id)
    path_to_profile_photo = f"D:\Project\Tg-Brawl-Bot\profile_photos\{profile_id}.webp"
    await message.answer_photo(photo = types.FSInputFile(path = path_to_profile_photo))
    if os.path.exists(path_to_profile_photo):
        os.remove(path_to_profile_photo)

# Обработчик кнопки "Изменить". Удаляет предыдущее сообщение и отправляет новое с выбором Brawl Stars ID.
async def handler_batton_change(call: CallbackQuery, bot: Bot):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    from battons.battons import change_brawl_stars_name
    user_id = call.from_user.id
    markup = await change_brawl_stars_name(user_id)
    user_lang = call.from_user.language_code
    data = await command_brawl_stars(user_lang)
    text = data[4]
    await call.message.answer(text, reply_markup = markup)

# Функция для изменения Brawl Stars ID пользователя. Устанавливает состояние и сохраняет user_id и nume.
async def change_brawl_id(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(BrawlStarsID.new_brawl_id)
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = int(call.data.split("_")[-1])
    user_lang = call.from_user.language_code
    data = await command_brawl_stars(user_lang)
    text = data[7]
    await call.message.answer(text)
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
        user_lang = message.from_user.language_code
        data = await command_brawl_stars(user_lang)
        text_1 = data[8]
        text_2 = data[9]
        text_3 = data[6]
        if brawl_name is None:
            raise ValueError(text_1)
        await db.__getattribute__(f"save_brawl_stars_name_{nume}")(brawl_name, user_id)
        os.remove(f"profile_names\{new_brawl_id}.html")
        await message.answer(text_2)
        await state.clear()
    except (AttributeError, ValueError):
        await message.answer(text_3)

