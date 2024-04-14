from aiogram import Bot
from aiogram.types import CallbackQuery
from uttils.text import *

async def help(call: CallbackQuery, bot: Bot):
    user_lang = call.from_user.language_code
    data = await command_help(user_lang)
    text = data[1]
    await call.answer(f"{text}😊👍.")


