from aiogram import types, Router
from aiogram.filters import CommandStart

main_handler = Router()


@main_handler.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Отправь мне фото и укажи в описании куда ты хочешь его сохранить: ')

