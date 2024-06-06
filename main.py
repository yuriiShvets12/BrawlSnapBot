from handlers.Command_start import start_as_ru, start_as_us, start
from handlers.All_fsms_context import BrawlStarsID, Donate
from handlers.Handler_all_text import random_text, hello
from aiogram.filters import Command, CommandStart
from aiogram import Bot, Dispatcher, F, Router
from uttils.menu_on_bot import set_start_menu
from handlers.Command_brawl_stars import *
from handlers.Command_donate import *
from aiogram.types import ContentType
from dotenv import load_dotenv
from database import bd as db
import asyncio
import os


load_dotenv()
rp = Router

bot = Bot(token = os.getenv("TOKEN_TEST"))
dp = Dispatcher()


async def start_bot(bot: Bot):
    await db.db_start()
    print("Бот запущен!!!\n#-----------#")

#Подключение к бд и вывод сообщения про то что бот запустился.
dp.startup.register(start_bot)
#Регистрация команды /start
dp.message.register(start, CommandStart())
dp.callback_query.register(start_as_us, F.data == "lang_us")
dp.callback_query.register(start_as_ru, F.data.in_(["lang_ru", "back"]))
#-------------------------------------------------------------------------------------------#
dp.callback_query.register(brawl_stars_command_handler_as_ru, F.data == "brawl_stars_id")
dp.callback_query.register(batton, F.data == "photo")
dp.callback_query.register(handler_batton_add_brawl_id, F.data.contains("add_brawl_id_"))
dp.message.register(fsm_context_batton_add_brawl_id, BrawlStarsID.brawl_id)
dp.callback_query.register(handler_batton_send_profile_photo, F.data.contains("brawl_id_"))
dp.callback_query.register(handler_batton_change, F.data == "change")
dp.callback_query.register(change_brawl_id, F.data.contains("new_id_"))
dp.message.register(new_profile_bs_id, BrawlStarsID.new_brawl_id)
#-------------------------------------------------------------------------------------------#
dp.message.register(donate, Command("donate"))
dp.callback_query.register(start_as_ru, F.data == "cancel")
dp.callback_query.register(country, F.data == "donate")
dp.callback_query.register(processing_donate, F.data.in_(["UAH", "RUB", "USD", "PLN"]))
dp.message.register(send_invoice, Donate.price)
dp.pre_checkout_query.register(pre_checkout_query_handler)
dp.message.register(successful_payment, F.content_type == ContentType.SUCCESSFUL_PAYMENT)
#-------------------------------------------------------------------------------------------#
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
    