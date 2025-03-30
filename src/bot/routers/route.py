from aiogram import Dispatcher

from .start import router as StartRouter 
from .message import router as MessageRouter

def include(dp: Dispatcher):
    dp.include_routers(
        StartRouter,
        MessageRouter    
    )