from data.config import ADM_ID
from aiogram import types, Router
from roloc_create import roloc_bot
from aiogram.fsm.context import FSMContext
from handlers.common.start import HelpState

help_router = Router()


@help_router.message(HelpState.name)
async def set_name(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(HelpState.text)
    await roloc_bot.send_message(
        chat_id=msg.from_user.id,
        text='📝 Опишите Вашу проблему'
    )


@help_router.message(HelpState.text)
async def set_text(msg: types.Message, state: FSMContext):
    await state.update_data(text=msg.text)
    await state.set_state(HelpState.communication)
    await roloc_bot.send_message(
        chat_id=msg.from_user.id,
        text='📱 Отправьте Ваши контактные данные'
    )


@help_router.message(HelpState.communication)
async def set_communication(msg: types.Message, state: FSMContext):
    tg_data = [
        msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name
    ]

    await state.update_data(communication=msg.text)
    data_list = await state.get_data()

    await state.clear()
    await roloc_bot.send_message(
        chat_id=ADM_ID,
        text=f"ПОМОЩЬ 🆘\n\n📩 <u><code>{tg_data[0]}</code></u> ({tg_data[1]} {tg_data[2]})\n"
             f"Имя: {data_list['name']}\n"
             f"Контакты: {data_list['communication']}\n\n"
             f"Текст: {data_list['text']}"
    )
    await roloc_bot.send_message(
        chat_id=msg.from_user.id,
        text='<strong>🕔 Ваша заявка обработана!</strong>\n\n'
             '<em>С Вами свяжутся в течении некоторого времени</em>'
    )
