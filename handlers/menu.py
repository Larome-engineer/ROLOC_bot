import roloc_create
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from data.services_dicts import complex_dict
from aiogram.fsm.state import State, StatesGroup
from keyboards.services_keyboard.web_design_kb import web_design_builder
from keyboards.services_keyboard.polygraphy_kb import polygraphy_builder
from keyboards.services_keyboard.graph_design_kb import graph_design_builder

menu_router = Router()


class FormState(StatesGroup):
    design_type = State()  # Вид дизайна
    cost = State()  # Стоимость
    speed = State()  # Скорость
    email = State()  # Почта
    phone = State()  # Номер телефона
    name = State()  # Имя человека
    communication = State()  # Предпочтительные коммуникации
    files = State()  # Файлы если есть
    wishes = State()  # Пожелания


class ComplexState(StatesGroup):
    design_type = State()  # Вид дизайна
    cost = State()  # Стоимость
    speed = State()  # Скорость
    email = State()  # Почта
    phone = State()  # Номер телефона
    name = State()  # Имя человека
    communication = State()  # Предпочтительные коммуникации
    files = State()  # Файлы если есть
    wishes = State()  # Пожелания


@menu_router.callback_query(F.data.startswith('serv'))
async def services_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer()

    action = call.data.split("_")[1]

    if action == "wd":
        await call.message.edit_text(
            text='💻 <strong>Выберите категорию веб-дизайна</strong>',
            reply_markup=web_design_builder.as_markup()
        )
        await state.set_state(FormState.design_type)

    elif action == "p":
        await call.message.edit_text(
            text='📰 <strong>Выберите категорию полиграфии</strong>',
            reply_markup=polygraphy_builder.as_markup()
        )
        await state.set_state(FormState.design_type)

    elif action == "gp":
        await call.message.edit_text(
            text='🖍 <strong>Выберите категорию графического дизайна</strong>',
            reply_markup=graph_design_builder.as_markup()
        )
        await state.set_state(FormState.design_type)

    elif action == "rs":
        await roloc_create.roloc_bot.send_poll(
            chat_id=call.from_user.id,
            question="🗂 Выберите опции из комплекса",
            options=list(complex_dict.values()),
            is_anonymous=False,
            allows_multiple_answers=True
        )
        await state.set_state(FormState.design_type)
