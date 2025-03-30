from aiogram import Bot, Dispatcher 
from aiogram.fsm.storage.memory import MemoryStorage
from .config import Config 

from .middlewares import (
    DependencyMiddleware,
)

from .routers import include
import asyncio, logging 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=Config.bot_token)


async def main():

    dp = Dispatcher(
        storage=MemoryStorage()
    )

    dp.message.middleware(
        DependencyMiddleware()    
    )
    include(dp=dp)

    await dp.start_polling(bot)

asyncio.run(main())