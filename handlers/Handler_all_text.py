from aiogram.types import Message
from aiogram import Bot
from uttils.text import *

async def random_text(message: Message, bot: Bot):
    user_lang = message.from_user.language_code
    data = await handler_all_text(user_lang)
    text = data[1]
    await message.answer(text)

async def hello(message: Message, bot: Bot):
    user_lang = message.from_user.language_code
    data = await handler_all_text(user_lang)
    text = data[2]
    await message.answer(text)