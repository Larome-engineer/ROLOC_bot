from roloc_create import roloc_bot
from data.msg_vars import about_msg
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from keyboards.common_kb.about_kb import about_builder

about_router = Router()


@about_router.message(Command('about'))
async def about_handler(msg: types.Message, state: FSMContext):
    await state.clear()
    await roloc_bot.send_message(
        chat_id=msg.chat.id,
        text=about_msg,
        reply_markup=about_builder.as_markup()
    )


@about_router.callback_query(F.data.startswith('social'))
async def about_callback(call: types.CallbackQuery):
    await call.answer()


