from aiogram.types import InlineKeyboardButton
from data.services_dicts import service_dict
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.common_kb.common_btn.back_btn import back_to_menu

serv_list = list(service_dict['p_dict'])

business_card = InlineKeyboardButton(text=service_dict['p_dict']["ss_ps1"], callback_data=serv_list[0])
poster = InlineKeyboardButton(text=service_dict['p_dict']["ss_ps2"], callback_data=serv_list[1])
flyer = InlineKeyboardButton(text=service_dict['p_dict']["ss_ps3"], callback_data=serv_list[2])
banner = InlineKeyboardButton(text=service_dict['p_dict']["ss_ps4"], callback_data=serv_list[3])
packaging = InlineKeyboardButton(text=service_dict['p_dict']["ss_ps5"], callback_data=serv_list[4])
mag_menu = InlineKeyboardButton(text=service_dict['p_dict']["ss_ps6"], callback_data=serv_list[5])
certificate = InlineKeyboardButton(text=service_dict['p_dict']["ss_ps7"], callback_data=serv_list[6])
sticker = InlineKeyboardButton(text=service_dict['p_dict']["ss_ps8"], callback_data=serv_list[7])
postcard = InlineKeyboardButton(text=service_dict['p_dict']["ss_ps9"], callback_data=serv_list[8])

polygraphy_builder = InlineKeyboardBuilder()
polygraphy_builder.row(
    business_card, poster, flyer, banner, packaging, mag_menu, certificate, sticker, postcard, back_to_menu, width=1
)
