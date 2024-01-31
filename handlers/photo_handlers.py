from aiogram import types, Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from disk.connect import client
from keyboards.keyboard import folders_menu
from utils.states import CreateFolderStates

photo_router = Router()


@photo_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Hello, I\'m Telegram')


@photo_router.message(F.photo)
async def message_handler(message: types.Message, state: FSMContext):
    await message.answer('Выберите куда сохранить.', reply_markup=folders_menu())
    await state.set_state(CreateFolderStates.save_photo)
    await state.update_data(file_id=message.photo[-1].file_id)
    await state.update_data(file_unique_id=message.photo[-1].file_unique_id)


@photo_router.callback_query()
async def save_photo(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(path=call.data)
    data = await state.get_data()
    await state.clear()
    file = await call.bot.get_file(data['file_id'])
    file_path = file.file_path
    src = f'/{data['path']}/' + data['file_unique_id']
    await client.upload(await call.bot.download_file(file_path), src)
