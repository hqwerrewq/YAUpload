import yadisk
from aiogram import types, Router, F

from disk.connect import client

photo_router = Router()
photo_list = {
}


@photo_router.message(F.photo)
async def message_handler(message: types.Message):
    caption = message.caption
    if caption is not None:
        photo_list.update({'path': caption})
    photo_id = message.photo[-1].file_id
    photo_unique_id = message.photo[-1].file_unique_id
    file = await message.bot.get_file(photo_id)
    file_path = file.file_path
    src = f'/{photo_list['path']}/' + photo_unique_id

    try:
        await client.get_meta(photo_list['path'])
        try:
            await client.upload(await message.bot.download_file(file_path), src)
            await message.answer('Фото сохранено.')
        except yadisk.exceptions.PathExistsError:
            await message.answer(f"Файл {photo_unique_id} уже существует.")
    except yadisk.exceptions.PathNotFoundError:
        await client.mkdir(f'/{photo_list['path']}/')
        await client.upload(await message.bot.download_file(file_path), src)
        await message.answer(f'Папка {photo_list['path']} создана, фото сохранено.')
