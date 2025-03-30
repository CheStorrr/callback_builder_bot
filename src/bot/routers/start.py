from aiogram import Router 
from aiogram.filters import CommandStart
from aiogram.types import Message
from ..services import DialogReader

router = Router(name=__name__)

@router.message(CommandStart())
async def start_command(
    message: Message,
    dialog: DialogReader
):
    await message.answer(
        text=dialog.answer
    )