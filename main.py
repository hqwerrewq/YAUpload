import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import find_dotenv, load_dotenv

from handlers.main_handlers import main_handler
from handlers.photo_handlers import photo_router
from utils.commands import set_commands

load_dotenv(find_dotenv())

storage = MemoryStorage()


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router=main_handler)
    dp.include_router(router=photo_router)
    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
