from aiogram.types import InlineKeyboardButton
from keyboards.common_kb.start_kb import close
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ADMIN_MENU
get_by_id = InlineKeyboardButton(text="Получить заявку по 🆔", callback_data="adm_1")
get_by_status = InlineKeyboardButton(text="Получить заявки по статусу", callback_data="adm_2")
change_status = InlineKeyboardButton(text="Изменить статус заявки", callback_data="adm_3")
change_pay_info = InlineKeyboardButton(text="Изменить платежную информацию", callback_data="adm_4")
user_menu = InlineKeyboardButton(text="Перейти в меню пользователя 📲", callback_data="adm_5")

admin_builder = InlineKeyboardBuilder() \
    .row(get_by_id, get_by_status, change_status, change_pay_info, user_menu, close, width=1)

# FOR_CHECK_STATUS
completed = InlineKeyboardButton(text='Исполнена ✅', callback_data='status_1')
unfulfilled = InlineKeyboardButton(text='В обработке 🕔', callback_data='status_2')
status_builder = InlineKeyboardBuilder().row(completed, unfulfilled, width=1)

# FOR_CHANGE_STATUS
completed_2 = InlineKeyboardButton(text='Исполнена ✅', callback_data='st_1')
unfulfilled_2 = InlineKeyboardButton(text='В обработке 🕔', callback_data='st_2')
st_builder = InlineKeyboardBuilder().row(completed_2, unfulfilled_2, width=1)

# FOR_CHANGE_PAY
paid = InlineKeyboardButton(text='✅ Оплачено', callback_data='pay_1')
not_paid = InlineKeyboardButton(text='❌ Не оплачено', callback_data='pay_2')
pay_builder = InlineKeyboardBuilder().row(paid, not_paid, width=1)
