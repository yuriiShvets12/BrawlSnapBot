from aiogram import Bot, Dispatcher, types, F, Router
from admin_cmd.admin_cm import admin_cmd
from dotenv import load_dotenv
from database import bd as db
import asyncio
import os
from handlers.Command_start import start
from aiogram.filters import Command, CommandStart
from handlers.Handler_all_text import random_text, hello
from uttils.menu_on_bot import set_start_menu
from handlers.Command_brawl_stars import *
from handlers.Command_donate import donate, processing_donate, send_invoice, pre_checkout_query_handler, successful_payment
from handlers.All_fsms_context import BrawlStarsID, Donate
from aiogram.types import ContentType

load_dotenv()
rp = Router

bot = Bot(token = os.getenv("TOKEN_API"))
dp = Dispatcher()


async def start_bot(bot: Bot):
    await db.db_start()
    print("Бот запущен!!!\n#-----------#")
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, admin_cmd) 

#Подключение к бд, запуск командной строки в vscode и вывод сообщения про то что бот запустился    
dp.startup.register(start_bot)
#Регистрация команды /start
dp.message.register(start, CommandStart())
dp.message.register(start, Command("help"))
#Регистрация команды и всех нужных обработчиков для команды /brawl_stars
dp.message.register(brawl_stars_command_handler, Command("brawl_stars"))
dp.callback_query.register(batton, F.data == "photo")
dp.callback_query.register(handler_batton_add_brawl_id, F.data.contains("add_brawl_id_"))
dp.message.register(fsm_context_batton_add_brawl_id, BrawlStarsID.brawl_id)
dp.callback_query.register(handler_batton_send_profile_photo, F.data.contains("brawl_id_"))
dp.callback_query.register(handler_batton_back, F.data.contains("back"))
dp.callback_query.register(handler_batton_change, F.data == "change")
dp.callback_query.register(change_brawl_id, F.data.contains("new_id_"))
dp.message.register(new_profile_bs_id, BrawlStarsID.new_brawl_id)
#Регистрация команды и всех нужных обработчиков для команды /donate
dp.message.register(donate, Command("donate"))
dp.callback_query.register(start, F.data == "cancel")
dp.callback_query.register(processing_donate, F.data == "donate")
dp.message.register(send_invoice, Donate.price)
dp.pre_checkout_query.register(pre_checkout_query_handler)
dp.message.register(successful_payment, F.content_type == ContentType.SUCCESSFUL_PAYMENT)
#Регистрация всех нужных обработчиков для обработки случайных сообщений или слова "Привет"
dp.message.register(hello, F.text == "Привет")
dp.message.register(random_text, F.text)



async def start_1():
    await set_start_menu(bot)
    try:
        await dp.start_polling(bot)
        await bot.delete_webhook(drop_pending_updates = True)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start_1())
    