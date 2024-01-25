import asyncio

from data.config import ADM_ID
from roloc_create import roloc_bot
from aiogram import types, Router, F
from aiogram.types import BotCommandScopeDefault
from aiogram.filters.command import CommandStart, BotCommand

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from data.msg_vars import services_msg, hello_msg, about_msg, close_msg, adm_msg

from keyboards.admin import admin_builder
from keyboards.common_kb.start_kb import start_builder
from keyboards.common_kb.about_kb import about_builder
from keyboards.common_kb.services_kb import services_builder

start_router = Router()


class HelpState(StatesGroup):
    name = State()
    text = State()
    communication = State()


async def set_commands(bot: roloc_bot):
    return await roloc_bot.set_my_commands(
        commands=[
            BotCommand(command='start', description='Начало работы'),
            BotCommand(command='about', description='Подробнее о нас'),
        ], scope=BotCommandScopeDefault()
    )


@start_router.message(CommandStart())
async def start_handler(msg: types.Message):
    if msg.from_user.id == int(ADM_ID):
        await roloc_bot.send_message(
            chat_id=msg.chat.id,
            text=adm_msg,
            reply_markup=admin_builder.as_markup()
        )
    else:
        await roloc_bot.send_message(
            chat_id=msg.chat.id,
            text=hello_msg,
            reply_markup=start_builder.as_markup()
        )
        await set_commands(roloc_bot)


@start_router.callback_query(F.data.startswith("start"))
async def start_callback(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split("_")[1]
    match action:
        case "1":
            await call.message.edit_text(
                text=services_msg,
                reply_markup=services_builder.as_markup()
            )
        case "2":
            await call.message.edit_text(
                text=about_msg,
                reply_markup=about_builder.as_markup()
            )
        case '3':
            await state.set_state(HelpState.name)
            await call.message.edit_text(
                text='👤 Как Вас зовут?',
            )
        case "4":
            await call.message.edit_text(
                text=close_msg,
            )
            await asyncio.sleep(5)
            await call.message.delete()
    await call.answer()
