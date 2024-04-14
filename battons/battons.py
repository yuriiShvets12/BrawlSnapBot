from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types, Router, F, Bot
from dotenv import load_dotenv
from database import bd as db
from uttils.text import *
import os


rp = Router()
load_dotenv()

bot = Bot(token = os.getenv("TOKEN_API"))

#Набор кнопок для команды /Brawl_Stars
async def communication(user_lang) -> InlineKeyboardMarkup:
    data = await battons_communication(user_lang)
    text_1 = data[1]
    text_2 = data[2]
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text = text_1, callback_data = "photo"))
    builder.row(InlineKeyboardButton(text = text_2, callback_data = "change"))
    return builder.as_markup()

async def brawl_stars_name(user_id) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(1, 4):
        profile_name = str(await getattr(db, f'get_brawl_name_{i}')(user_id))
        if profile_name in ["False", "None"]:
            profile_name = "+"
            callback_data = f"add_brawl_id_{i}"
        else:
            callback_data = f"brawl_id_{i}"
        builder.row(InlineKeyboardButton(text=profile_name, callback_data=callback_data))
    builder.row(InlineKeyboardButton(text="◀️Back", callback_data="back"))
    return builder.as_markup()

async def change_brawl_stars_name(user_id) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(1, 4):
        profile_name = str(await getattr(db, f'get_brawl_name_{i}')(user_id))
        if profile_name not in ["False", "None"]:
            callback_data = f"new_id_{i}"
            builder.row(InlineKeyboardButton(text=profile_name, callback_data=callback_data))
    builder.row(InlineKeyboardButton(text="◀️Back", callback_data="back"))
    return builder.as_markup()

#Кнопка для донатика
async def donate() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text = "🎉Send donation🎉", callback_data = "donate"))
    builder.row(InlineKeyboardButton(text = "❌Cancel", callback_data = "cancel"))
    return builder.as_markup()

#Кнопки для выбора валюты
async def currency() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text = "🇺🇦", callback_data = "UAH"),
                InlineKeyboardButton(text = "🇷🇺", callback_data = "RUB"),
                InlineKeyboardButton(text = "🇺🇸", callback_data = "USD"),
                InlineKeyboardButton(text = "🇮🇩", callback_data = "PLN"),
    )
    return builder.as_markup()



