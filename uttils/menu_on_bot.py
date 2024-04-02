from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_start_menu(bot: Bot):
    commands = [
        BotCommand(
            command='/start',
            description='Запускаем бота',
        ),
        BotCommand(
            command='/brawl_stars',
            description='Взаимодействие с твоим Brawl Stars ID',
        ),
        BotCommand(
            command='/donate',
            description='Отправить донат проекту',
        ),
        BotCommand(
            command='/help',
            description='Помощь в роботе с ботом',
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())