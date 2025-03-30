from dotenv import load_dotenv 
from os import getenv 

from typing import Optional

load_dotenv()

class Config:
    bot_token: Optional[str] = getenv("BOT_TOKEN")
