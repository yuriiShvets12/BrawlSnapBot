from aiogram import Bot, types
from aiogram.types import Message, CallbackQuery
from uttils.text import *


async def start(message: Message):
    user_lang = "ru"
    data = await command_start(user_lang)
    text = data[1]
    from battons.battons import batton_for_command_start_as_ru
    markup = await batton_for_command_start_as_ru()
    await message.reply(text = text, reply_markup = markup)

async def start_as_ru(call: CallbackQuery, bot: Bot):
    user_lang = "ru"
    data = await command_start(user_lang)
    text = data[1]
    from battons.battons import batton_for_command_start_as_ru
    markup = await batton_for_command_start_as_ru()
    await bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = text, reply_markup = markup)

async def start_as_us(call: CallbackQuery, bot: Bot):
    user_lang = "en"
    data = await command_start(user_lang)
    text = data[1]
    from battons.battons import batton_for_command_start_as_us
    markup = await batton_for_command_start_as_us()
    await bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = text, reply_markup = markup)