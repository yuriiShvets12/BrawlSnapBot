from aiogram import Bot
from aiogram.types import Message
from uttils.text import *


async def start(message: Message, bot: Bot):
    user_lang = message.from_user.language_code
    data = await command_start(user_lang)
    text = data[1]
    await bot.send_message(message.from_user.id, text)
