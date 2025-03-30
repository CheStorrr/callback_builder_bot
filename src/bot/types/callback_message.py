from dataclasses import dataclass 
from aiogram.types import Message, PhotoSize, InlineKeyboardButton, Video

from typing import Optional

@dataclass
class CallbackMessageType:
    text: Optional[str]
    photo: Optional[list[PhotoSize]]
    video: Optional[Video]
    caption: Optional[str]