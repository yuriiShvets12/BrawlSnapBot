from aiogram import Bot
from aiogram.types import Message


#Список команд для команды /start
cmd_list = "\n1. /start - Запустить/перезапустить бота\n2. /brawl_stars - Взаимодействие с твоим Brawl Stars id\n3. /donate - Отправить донат на указанную сумму."

async def start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"🚀 Привет! Вот полный список команд, которые сейчас доступны:{cmd_list}")