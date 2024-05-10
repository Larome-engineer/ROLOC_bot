from data.links import links
from aiogram.types import InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

start = InlineKeyboardButton(text='Начнём! 🧩', callback_data='start_1')
web_app = InlineKeyboardButton(text='Веб-приложение 📱', web_app=WebAppInfo(url=links['web_app']))
about_us = InlineKeyboardButton(text='Подробнее о нас 🌐', callback_data='start_2')
need_help = InlineKeyboardButton(text='Мне нужна помощь 🆘', callback_data='start_3')
close = InlineKeyboardButton(text='Закрыть 🚫', callback_data='start_4')

start_builder = InlineKeyboardBuilder().row(start, web_app, about_us, need_help, close, width=1)
