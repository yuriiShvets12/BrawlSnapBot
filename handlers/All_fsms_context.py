from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class BrawlStarsID(StatesGroup):
    brawl_id = State()
    nume = State()
    user_id = State()
    new_brawl_id = State()

class Donate(StatesGroup):
    start_to_work = State()
    price = State()
    