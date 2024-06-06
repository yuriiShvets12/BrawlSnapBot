from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_start_menu(bot: Bot):
    commands = [
        BotCommand(
            command = "/start",
            description = "Let's launch the bot",
        ),
        BotCommand(
            command = "/donate",
            description = "Send a donation to the project",
        ),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())