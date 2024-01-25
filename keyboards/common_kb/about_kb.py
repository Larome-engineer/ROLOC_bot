from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.common_kb.common_btn.social_media_btn import *
from keyboards.common_kb.common_btn.back_btn import back_to_start

about_builder = InlineKeyboardBuilder().row(vk, telegram, website, back_to_start, width=1)
