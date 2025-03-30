from aiogram import BaseMiddleware 
from aiogram.types import (
    TelegramObject,
    Message    
)

from typing import (
    Callable,
    Awaitable,
    Dict,
    Any     
)

from ..services import DialogReader

class DependencyMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[
            [TelegramObject, Dict[str, Any]], Awaitable[Any]
        ],
        event: TelegramObject,
        data: Dict[str, Any]        
    ):
        dialog_reader = DialogReader()

        if isinstance(event, Message):
            if event.text:
                dialog_reader.get_dialog(
                    trigger=event.text
                )

        data['dialog'] = dialog_reader

        await handler(event, data)
