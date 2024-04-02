from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.fsm.context import FSMContext
from handlers.All_fsms_context import Donate
from aiogram import Bot, types
import os


# Эта функция используется для обработки команды /donate. Она генерирует разметку для кнопки пожертвования и отправляет сообщение пользователю.
async def donate(message: Message, bot: Bot):
    from battons.battons import donate
    markup = await donate()
    await message.answer("Спасибо за пожертвование!", reply_markup = markup)

# Эта функция срабатывает, когда пользователь нажимает на кнопку пожертвования. Она устанавливает состояние 'Donate.price' и просит пользователя ввести сумму пожертвования.
async def processing_donate(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(Donate.price)
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await call.message.answer("Напиши сумму которую хотел бы пожертвовать:")

# Эта функция отправляет счет пользователю после того, как он ввел сумму пожертвования. Если введенное значение не является числом, функция отправляет сообщение об ошибке.
async def send_invoice(message: Message, state: FSMContext, bot: Bot):
    try:
        await state.update_data(price = int(message.text) * 100)
        data = await state.get_data()
        price = data["price"]
        await bot.send_invoice(
            chat_id = message.from_user.id,
            title = "Donate",
            description = "Спасибо за пожертвование!",
            provider_token = os.getenv("TOKEN_PAY"),
            payload = "donate",
            currency = "pln",
            prices = [
                LabeledPrice(
                    label = "Пожертвование",
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
        await message.answer("Похоже вы отправили не сумму😥\nПопробуйте еще раз.")

# Эта функция обрабатывает предварительный запрос на оплату. Если полезная нагрузка счета не соответствует 'some-product', функция отправляет сообщение об ошибке.
async def pre_checkout_query_handler(pre_checkout_query: types.PreCheckoutQuery, state: FSMContext, bot: Bot):
    if pre_checkout_query.invoice_payload != 'some-product':
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=False, error_message="Sorry, we're having a temporary problem with this product.")
    else:
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Эта функция выполняется после успешной оплаты и отправляет пользователю сообщение с благодарностью за пожертвование.
async def successful_payment(message: types.Message):
    await message.answer("Спасибо за ваше пожертвование!")
