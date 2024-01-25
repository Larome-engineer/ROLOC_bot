from aiogram.types import InlineKeyboardButton
from data.services_dicts import service_dict
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.common_kb.common_btn.back_btn import back_to_menu

serv_list = list(service_dict['gp_dict'])

logo = InlineKeyboardButton(text=service_dict['gp_dict']['ss_gps1'], callback_data=serv_list[0])
modeling = InlineKeyboardButton(text=service_dict['gp_dict']['ss_gps2'], callback_data=serv_list[1])
font_creating = InlineKeyboardButton(text=service_dict['gp_dict']['ss_gps3'], callback_data=serv_list[2])
smm_sm = InlineKeyboardButton(text=service_dict['gp_dict']['ss_gps4'], callback_data=serv_list[3])
bb_gl = InlineKeyboardButton(text=service_dict['gp_dict']['ss_gps5'], callback_data=serv_list[4])

graph_design_builder = InlineKeyboardBuilder()
graph_design_builder.row(logo, modeling, font_creating, smm_sm, bb_gl, back_to_menu, width=1)
