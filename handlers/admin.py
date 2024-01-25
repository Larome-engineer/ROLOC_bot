from service.admin import *
from aiogram import Router, F
from data.config import ADM_ID
from roloc_create import roloc_bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from keyboards.common_kb.start_kb import start_builder
from data.services_dicts import status_dict, pay_dict
from keyboards.admin import status_builder, admin_builder, st_builder, pay_builder

from data.msg_vars \
    import hello_msg, get_num, select_status, select_new_status, successful_status, select_new_pay, successful_pay

admin_router = Router()


class FormID(StatesGroup):
    f_id = State()


class ChangeStatus(StatesGroup):
    f_id = State()
    c_status = State()


class ChangePay(StatesGroup):
    f_id = State()
    c_pay = State()


@admin_router.callback_query(F.data.startswith("adm"))
async def admin_menu(call: CallbackQuery, state: FSMContext):
    call_data = call.data.split("_")[1]
    match call_data:
        case "1":
            await call.message.edit_text(
                text=get_num,
            )
            await state.set_state(FormID.f_id)
        case "2":
            await call.message.edit_text(
                text=select_status,
                reply_markup=status_builder.as_markup()
            )
        case "3":
            await call.message.edit_text(
                text=get_num,
            )
            await state.set_state(ChangeStatus.f_id)
        case "4":

            await call.message.edit_text(
                text=get_num,
            )
            await state.set_state(ChangePay.f_id)
        case "5":
            await call.message.edit_text(
                text=hello_msg,
                reply_markup=start_builder.as_markup()
            )

    await call.answer()


@admin_router.callback_query(F.data.startswith("status"))
async def get_by_status(call: CallbackQuery):
    call_data = call.data.split("_")[1]
    if call_data == "1":
        status = status_dict['status1']
    else:
        status = status_dict['status2']
    await call.message.edit_text(
        text=get_all_by_status(status),
        reply_markup=admin_builder.as_markup()
    )
    await call.answer()


@admin_router.message(ChangeStatus.f_id)
async def change_status_start(msg: Message, state: FSMContext):
    if await state.get_state() is None:
        return
    else:
        await state.update_data(f_id=int(msg.text))
        await roloc_bot.send_message(
            chat_id=ADM_ID,
            text=select_new_status,
            reply_markup=st_builder.as_markup()
        )


@admin_router.message(ChangeStatus.c_status)
@admin_router.callback_query(F.data.startswith("st"))
async def change_status_end(call: CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        return
    else:
        call_data = call.data.split("_")[1]
        if call_data == "1":
            status = status_dict['status1']
        else:
            status = status_dict['status2']

        s_data = await state.get_data()
        change_status(status, s_data['f_id'])
        await call.message.edit_text(
            text=successful_status,
            reply_markup=admin_builder.as_markup()
        )

        await state.clear()

    await call.answer()


@admin_router.message(ChangePay.f_id)
async def change_pay_start(msg: Message, state: FSMContext):
    if await state.get_state() is None:
        return
    else:
        await state.update_data(f_id=int(msg.text))
        await roloc_bot.send_message(
            chat_id=ADM_ID,
            text=select_new_pay,
            reply_markup=pay_builder.as_markup()
        )


@admin_router.message(ChangePay.c_pay)
@admin_router.callback_query(F.data.startswith("pay"))
async def change_pay_end(call: CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        return
    else:
        call_data = call.data.split("_")[1]
        if call_data == "1":
            pay = pay_dict['pay1']
        else:
            pay = pay_dict['pay2']

        s_data = await state.get_data()
        change_pay_info(pay, s_data['f_id'])
        await call.message.edit_text(
            text=successful_pay,
            reply_markup=admin_builder.as_markup()
        )

        await state.clear()

    await call.answer()


@admin_router.message(FormID.f_id)
async def get_id(msg: Message, state: FSMContext):
    if await state.get_state() is None:
        return
    else:
        await state.clear()
        await roloc_bot.send_message(
            chat_id=ADM_ID,
            text=get_by_id(int(msg.text)),
            reply_markup=admin_builder.as_markup()
        )
