from data.services_dicts import speed_dict
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

speed_list = list(speed_dict.keys())

speed1 = InlineKeyboardButton(text=speed_dict['speed1'], callback_data=speed_list[0])
speed2 = InlineKeyboardButton(text=speed_dict['speed2'], callback_data=speed_list[1])
speed3 = InlineKeyboardButton(text=speed_dict['speed3'], callback_data=speed_list[2])

speed_builder = InlineKeyboardBuilder().row(speed1, speed2, speed3, width=1)
