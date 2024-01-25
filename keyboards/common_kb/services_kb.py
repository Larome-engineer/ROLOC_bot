from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.common_kb.common_btn.back_btn import back_to_start

web_design = InlineKeyboardButton(text='Веб-дизайн 💻', callback_data='serv_wd')
polygraphy = InlineKeyboardButton(text='Полиграфия 📰', callback_data='serv_p')
graph_design = InlineKeyboardButton(text='Графический Дизайн 🖍', callback_data='serv_gp')
range_service = InlineKeyboardButton(text='Комплекс Услуг (Несколько услуг сразу)', callback_data='serv_rs')

services_builder = InlineKeyboardBuilder()
services_builder.row(web_design, polygraphy, graph_design, range_service, back_to_start, width=1)
