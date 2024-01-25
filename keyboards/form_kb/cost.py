from data.services_dicts import cost_dict
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

cost_list = list(cost_dict.keys())

cost1 = InlineKeyboardButton(text=cost_dict['cost1'], callback_data=cost_list[0])
cost2 = InlineKeyboardButton(text=cost_dict['cost2'], callback_data=cost_list[1])
cost3 = InlineKeyboardButton(text=cost_dict['cost3'], callback_data=cost_list[2])

cost_builder = InlineKeyboardBuilder().row(cost1, cost2, cost3, width=1)
