from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.fsm.context import FSMContext
from handlers.All_fsms_context import Donate
from aiogram import Bot, types
import os
from uttils.text import *

# Эта функция используется для обработки команды /donate. Она генерирует разметку для кнопки пожертвования и отправляет сообщение пользователю.
async def donate(message: Message):
    user_lang = message.from_user.language_code
    data = await command_donate(user_lang)
    text = data[1]
    from battons.battons import donate
    markup = await donate()
    await message.answer(text, reply_markup = markup)

async def country(call: CallbackQuery, bot: Bot):
    user_lang = call.from_user.language_code
    data = await command_donate(user_lang)
    text = data[2]
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    from battons.battons import currency
    markup = await currency()
    await call.message.answer(text, reply_markup = markup)

# Эта функция срабатывает, когда пользователь нажимает на кнопку пожертвования. Она устанавливает состояние 'Donate.price' и просит пользователя ввести сумму пожертвования.
async def processing_donate(call: CallbackQuery, state: FSMContext, bot: Bot):
    user_lang = call.from_user.language_code
    data = await command_donate(user_lang)
    text = data[3]
    await state.set_state(Donate.price)
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await state.update_data(currency_on_invoice_message = call.data)
    await call.message.answer(text)

# Эта функция отправляет счет пользователю после того, как он ввел сумму пожертвования. Если введенное значение не является числом, функция отправляет сообщение об ошибке.
async def send_invoice(message: Message, state: FSMContext, bot: Bot):
    try:
        user_lang = message.from_user.language_code
        data = await command_donate(user_lang)
        text_1 = data[4]
        text_2 = data[5]
        await state.update_data(price = int(message.text) * 100)
        data = await state.get_data()
        price = data["price"]
        currency_on_invoice_message = data["currency_on_invoice_message"]
        await bot.send_invoice(
            chat_id = message.from_user.id,
            title = "Donate",
            description = text_1,
            provider_token = os.getenv("TOKEN_PAY"),
            payload = "donate",
            currency = currency_on_invoice_message,
            prices = [
                LabeledPrice(
                    label = text_2,
                    amount = price,
                )
            ],
            start_parameter = "donate",
            provider_data = None,
            need_name = False,
            need_phone_number = False,
            need_email = False,
            need_shipping_address = False,
            send_phone_number_to_provider = False,
            send_email_to_provider = False,
            is_flexible = False,
            disable_notification = False,
            reply_to_message_id = None,
            allow_sending_without_reply = False,
            reply_markup = None,
            protect_content = False
        )
        await state.clear()
    except ValueError:
        user_lang = message.from_user.language_code
        data = await command_donate(user_lang)
        text = data[6]
        await message.answer(text)

# Эта функция обрабатывает предварительный запрос на оплату. Если полезная нагрузка счета не соответствует 'some-product', функция отправляет сообщение об ошибке.
async def pre_checkout_query_handler(pre_checkout_query: types.PreCheckoutQuery, state: FSMContext, bot: Bot):
    if pre_checkout_query.invoice_payload != 'some-product':
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=False, error_message="Sorry, we're having a temporary problem with this product.")
    else:
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Эта функция выполняется после успешной оплаты и отправляет пользователю сообщение с благодарностью за пожертвование.
async def successful_payment(message: types.Message):
    user_lang = message.from_user.language_code
    data = await command_donate(user_lang)
    text = data[7]
    await message.answer(text)
