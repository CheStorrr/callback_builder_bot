from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.fsm.context import FSMContext

from ..states import WaitLinkState
from ..types import CallbackMessageType
from ..services import DialogReader

router = Router(name=__name__)

@router.message(WaitLinkState.link)
async def get_link_handler(
    message: Message,
    state: FSMContext,
    dialog: DialogReader
):
    
    builder = InlineKeyboardBuilder()
    data = message.text.splitlines()
    for line in data:
        try:
            text, link = line.split(' - ')
            builder.button(
                text=text,
                url=link 
            )
        except:
            await message.answer(
                text=dialog.get_dialog("error_link_build")
            )
            return

    data = await state.get_data()
    message_type: CallbackMessageType = data["message_type"]

    await state.clear()
    
    if message_type.text:
        await message.answer(
            text=message_type.text,
            reply_markup=builder.as_markup()
        )

        return 
    
    elif message_type.photo:
        await message.answer_photo(
            photo=message_type.photo[0].file_id,
            caption=message_type.caption,
            reply_markup=builder.as_markup()
        )
        return 
    
    elif message_type.video:
        await message.answer_video(
            video=message_type.video.file_id,
            caption=message_type.caption,
            reply_markup=builder.as_markup()
        )
        return
    
    else: 
        await message.answer(
            text=dialog.get_dialog("error_link_build")
        )


@router.message()
async def text_handler(
    message: Message,
    state: FSMContext,
    dialog: DialogReader
):
    
    message_type = CallbackMessageType(
        text=message.text,
        photo=message.photo,
        video=message.video,
        caption=message.caption
    )
    data = {
        "message_type": message_type
    }
    await state.set_state(WaitLinkState.link)
    await state.set_data(data)
    await message.answer(
        text=dialog.get_dialog("state_build")
    )
