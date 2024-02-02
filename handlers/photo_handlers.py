import yadisk
from aiogram import types, Router, F

from disk.connect import client

photo_router = Router()


@photo_router.message(F.photo)
async def message_handler(message: types.Message):
    photo_id = message.photo[-1].file_id
    photo_unique_id = message.photo[-1].file_unique_id
    caption = message.caption
    file = await message.bot.get_file(photo_id)
    file_path = file.file_path
    src = f'/{caption}/' + photo_unique_id
    try:
        await client.get_meta(caption)
        try:
            await client.upload(await message.bot.download_file(file_path), src)
            await message.answer('Фото сохранено.')
        except yadisk.exceptions.PathExistsError:
            await message.answer('Файл уже существует.')
    except yadisk.exceptions.PathNotFoundError:
        await client.mkdir(f'/{caption}/')
        await client.upload(await message.bot.download_file(file_path), src)
        await message.answer(f'Папка {caption} создана, фото сохранено.')
