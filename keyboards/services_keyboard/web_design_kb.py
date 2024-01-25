from aiogram.types import InlineKeyboardButton
from data.services_dicts import service_dict
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.common_kb.common_btn.back_btn import back_to_menu

serv_list = list(service_dict['wd_dict'])

single_page_site = InlineKeyboardButton(text=service_dict['wd_dict']['ss_wds1'], callback_data=serv_list[0])
multi_page_site = InlineKeyboardButton(text=service_dict['wd_dict']['ss_wds2'], callback_data=serv_list[1])
online_store = InlineKeyboardButton(text=service_dict['wd_dict']['ss_wds3'], callback_data=serv_list[2])
taplink = InlineKeyboardButton(text=service_dict['wd_dict']['ss_wds4'], callback_data=serv_list[3])
single_block_site = InlineKeyboardButton(text=service_dict['wd_dict']['ss_wds5'], callback_data=serv_list[4])

web_design_builder = InlineKeyboardBuilder()
web_design_builder.row(
    single_page_site, multi_page_site, online_store, taplink, single_block_site, back_to_menu, width=1
)
