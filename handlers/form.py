import os
from data.config import ADM_ID
from service.get_service import *
from roloc_create import roloc_bot
from handlers.menu import FormState
from aiogram import types, Router, F
from service.app_form import create_form
from aiogram.fsm.context import FSMContext
from aiogram.types import ContentType as Ct
from middleware.album import AlbumMiddleware
from data.services_dicts import complex_dict
from keyboards.form_kb.cost import cost_builder
from keyboards.form_kb.speed import speed_builder
from keyboards.form_kb.complete import end_builder
from aiogram.utils.media_group import MediaGroupBuilder
from data.msg_vars import wishes_msg, add_files, cost_things, speed_things

form_router = Router()


@form_router.poll_answer()
@form_router.message(FormState.design_type)
async def comp_handler(pa: types.PollAnswer, state: FSMContext):
    if await state.get_state() is None:
        return
    else:
        opt = []
        for i in pa.option_ids:
            if i in complex_dict.keys():
                opt.append(complex_dict.get(i))

        await state.update_data(design_type=f"Комплекс: {', '.join(opt)}")
        await state.set_state(FormState.cost)
        await roloc_bot.send_message(
            chat_id=pa.user.id,
            text=cost_things,
            reply_markup=cost_builder.as_markup()
        )


@form_router.message(FormState.design_type)
@form_router.callback_query(F.data.startswith("ss"))
async def form_handler(call: types.CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        return
    else:
        service = get_service_by_callback(call.data.split("_")[1])

        await state.update_data(design_type=service)
        await state.set_state(FormState.cost)
        await call.message.edit_text(
            text=cost_things,
            reply_markup=cost_builder.as_markup()
        )
    await call.answer()


@form_router.message(FormState.cost)
@form_router.callback_query(F.data.startswith("cost"))
async def cost_state(call: types.CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        return
    else:
        await state.update_data(cost=get_cost_by_callback(call.data))
        await state.set_state(FormState.speed)
        await call.message.edit_text(
            text=speed_things,
            reply_markup=speed_builder.as_markup()
        )
    await call.answer()


@form_router.message(FormState.speed)
@form_router.callback_query(F.data.startswith("speed"))
async def speed_state(call: types.CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        return
    else:
        await state.update_data(speed=get_speed_by_callback(call.data))
        await state.set_state(FormState.email)
        await call.message.edit_text(
            text="📩 <strong>Отправьте email</strong>",
        )
    await call.answer()


@form_router.message(FormState.email)
async def email_state(msg: types.Message, state: FSMContext):
    if await state.get_state() is None:
        return
    if msg.photo or msg.video or msg.voice or msg.audio \
            or msg.document or msg.video_note or msg.story:
        await msg.answer("❗️Медиафайлы на данном этапе не принимаются")
        await state.set_state(FormState.email)
        await msg.answer(
            text="📩 <strong>Отправьте email</strong>",
        )
    else:
        await state.update_data(email=msg.text)
        await state.set_state(FormState.phone)
        await msg.answer('📞 <strong>Отправьте номер телефона</strong>')


@form_router.message(FormState.phone)
async def phone_state(msg: types.Message, state: FSMContext):
    if await state.get_state() is None:
        return
    if msg.photo or msg.video or msg.voice or msg.audio \
            or msg.document or msg.video_note or msg.story:
        await msg.answer("❗️Медиафайлы на данном этапе не принимаются")
        await state.set_state(FormState.phone)
        await msg.answer('📞 <strong>Отправьте номер телефона</strong>')
    else:
        await state.update_data(phone=msg.text)
        await state.set_state(FormState.name)
        await msg.answer('👤 <strong>Отправьте Ваше имя</strong>')


@form_router.message(FormState.name)
async def name_state(msg: types.Message, state: FSMContext):
    if await state.get_state() is None:
        return
    if msg.photo or msg.video or msg.voice or msg.audio \
            or msg.document or msg.video_note or msg.story:
        await msg.answer("❗️Медиафайлы на данном этапе не принимаются")
        await state.set_state(FormState.name)
        await msg.answer('👤 <strong>Отправьте Ваше имя</strong>')
    else:
        await state.update_data(name=msg.text)
        await state.set_state(FormState.communication)
        await msg.answer('📱 <strong>Где Вам будет удобнее связаться?</strong>\n\n'
                         '<em>▫️ Можете отправить несколько способов связи одним сообщением</em>')


@form_router.message(FormState.communication)
async def communication_state(msg: types.Message, state: FSMContext):
    if await state.get_state() is None:
        return
    if msg.photo or msg.video or msg.voice or msg.audio \
            or msg.document or msg.video_note or msg.story:
        await msg.answer("❗️Медиафайлы на данном этапе не принимаются")
        await state.set_state(FormState.communication)
        await msg.answer('📱 <strong>Где Вам будет удобнее связаться?</strong>\n\n'
                         '<em>▫️ Можете отправить несколько способов связи одним сообщением</em>')

    else:
        await state.update_data(communication=msg.text)
        await state.set_state(FormState.wishes)
        await msg.answer(wishes_msg)


@form_router.message(FormState.wishes)
async def wishes_state(msg: types.Message, state: FSMContext):
    if await state.get_state() is None:
        return
    if msg.photo or msg.voice or msg.document or msg.audio or msg.video or msg.story or msg.video_note:
        await msg.answer("❗️Медиафайлы на данном этапе не принимаются")
        await state.set_state(FormState.wishes)
        await msg.answer(wishes_msg)
    else:
        await state.update_data(wishes=msg.text)
        await state.set_state(FormState.files)
        await msg.answer(
            text=add_files,
            reply_markup=end_builder.as_markup()
        )


form_router.message.middleware(AlbumMiddleware())


@form_router.message(FormState.files)
@form_router.message(F.сontent_type.in_([Ct.PHOTO, Ct.VOICE, Ct.DOCUMENT]))
async def files_state(msg: types.Message, state: FSMContext, album: list = None):
    if await state.get_state() is None:
        return
    else:
        if await state.get_state() is None:
            return

        app_id = await __perform_pdf(msg.from_user.id, state)
        if msg.photo:
            try:
                photo_ids = []
                media_group = MediaGroupBuilder(caption=f"📄 AppForm {app_id}")
                for msg in album:
                    photo_ids.append(msg.photo[-1].file_id)
                for photo_id in photo_ids:
                    try:
                        media_group.add_photo(
                            media=photo_id
                        )
                    except ValueError:
                        print("Тут ValueError")
                await roloc_bot.send_media_group(
                    chat_id=ADM_ID,
                    media=media_group.build(),

                )
            except TypeError:
                await roloc_bot.send_photo(
                    chat_id=ADM_ID,
                    photo=msg.photo[-1].file_id,
                    caption=f'📄 AppForm {app_id}'
                )

        elif msg.voice:
            await roloc_bot.send_voice(
                chat_id=ADM_ID,
                voice=msg.voice.file_id,
                caption=f'📄 AppForm {app_id}'
            )

        elif msg.document:
            await roloc_bot.send_document(
                chat_id=ADM_ID,
                document=msg.document.file_id,
                caption=f'📄 AppForm {app_id}'
            )


@form_router.message(FormState.files)
@form_router.callback_query(F.data.contains("end"))
async def none_files_state(call: types.CallbackQuery, state: FSMContext):
    if await state.get_state() is None:
        await call.answer()
    else:
        if await state.get_state() is None:
            return

        await roloc_bot.delete_message(call.from_user.id, call.message.message_id)
        await __perform_pdf(call.from_user.id, state)

    await call.answer()


async def __perform_pdf(msg: int, state: FSMContext):

    form_dict = await state.get_data()
    await state.clear()

    app_data = create_form(
        form_type=form_dict['design_type'],
        cost=form_dict['cost'],
        status='В обработке',
        pay='Не оплачена',
        speed=form_dict['speed'],
        name=form_dict['name'],
        email=form_dict['email'],
        phone=form_dict['phone'],
        communication=form_dict['communication'],
        wishes=form_dict['wishes'],
    )

    await roloc_bot.send_document(
        chat_id=ADM_ID,
        document=types.FSInputFile(f'{app_data[0]}')
    )
    await roloc_bot.send_message(
        chat_id=msg,
        text='<strong>🕔 Ваша заявка обработана!</strong>\n\n'
             '<em>С Вами свяжутся в течении некоторого времени</em>'
    )

    os.remove(app_data[0])
    return app_data[1]
