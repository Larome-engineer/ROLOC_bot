from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

end = InlineKeyboardButton(text='Завершить', callback_data="end")
end_builder = InlineKeyboardBuilder().row(end, width=1)
