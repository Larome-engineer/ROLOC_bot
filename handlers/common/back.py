from aiogram import types, Router, F
from data.msg_vars import services_msg, hello_msg
from keyboards.common_kb.start_kb import start_builder
from keyboards.common_kb.services_kb import services_builder

back_to_router = Router()


@back_to_router.callback_query(F.data == 'back_serv')
async def back_to_menu(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text=services_msg,
        reply_markup=services_builder.as_markup()
    )


@back_to_router.callback_query(F.data == 'back_start')
async def back_to_menu(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text=hello_msg,
        reply_markup=start_builder.as_markup()
    )
