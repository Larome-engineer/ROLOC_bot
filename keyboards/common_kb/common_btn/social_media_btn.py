from aiogram.types import InlineKeyboardButton
from data.links import links

vk = InlineKeyboardButton(text='VK', callback_data='socialVK', url=links['vk'])
telegram = InlineKeyboardButton(text='Telegram', callback_data='socialLinkTG', url=links['telegram'])
website = InlineKeyboardButton(text='Website', callback_data='socialWS', url=links['website'])
