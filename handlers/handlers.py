from aiogram import types, F, Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from disk.connect import client

router = Router()
dp = Dispatcher()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer('Привет, отправь файл что бы сохранить его.')


@router.message()
async def message_handler(msg: Message):
    file_id = msg.document.file_id
    file = await msg.bot.get_file(file_id)
    file_path = file.file_path
    src = '/test/' + msg.document.file_name

    await client.upload(await msg.bot.download_file(file_path), src)
