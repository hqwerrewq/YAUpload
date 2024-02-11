import yadisk
from aiogram import types, Router, F

from disk.connect import client

photo_router = Router()
photo_list = {}


@photo_router.message(F.photo)
async def message_handler(message: types.Message):
    caption = message.caption

    if caption is not None:
        photo_list.update({'path': caption})

    photo_id = message.photo[-1].file_id
    photo_unique_id = message.photo[-1].file_unique_id
    file = await message.bot.get_file(photo_id)
    file_path = file.file_path

    try:
        upload_src = f'/{photo_list['path']}/' + photo_unique_id
        path = f'/{photo_list['path']}/'
    except KeyError:
        upload_src = f'/Test/' + photo_unique_id
        path = f'Мои Файлы'

    try:

        await client.get_meta(path)

        try:

            await client.upload(await message.bot.download_file(file_path), upload_src)
            await message.answer('Фото сохранено.')

        except yadisk.exceptions.PathExistsError:

            await message.answer(f"Файл {photo_unique_id} уже существует.")

    except yadisk.exceptions.PathNotFoundError:

        await client.mkdir(path)
        await client.upload(await message.bot.download_file(file_path), upload_src)
        await message.answer(f'Папка {path} создана.')
