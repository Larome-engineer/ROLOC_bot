from data.config import BOT_TOKEN
from aiogram import Bot, Dispatcher

roloc_bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()