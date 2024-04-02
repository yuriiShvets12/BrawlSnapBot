from aiogram.types import Message
from aiogram import Bot

async def random_text(message: Message, bot: Bot):
    await message.answer("Я тебя не понимаю сори😥!")

async def hello(message: Message, bot: Bot):
    await message.answer("Привет бро🖐!")