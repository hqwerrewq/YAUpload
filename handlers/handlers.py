import json

from aiogram import types, Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards.keyboard import folders_menu
from utils.states import CreateFolderStates

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Hello, I\'m Telegram')


@router.message(F.photo)
async def photo(message: types.Message):
    await message.answer('Выберите куда сохранить.', reply_markup=folders_menu())


@router.callback_query(F.data == 'create_folder')
async def folder_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Назвиние папки: ')
    await state.set_state(CreateFolderStates.folder_name)


@router.message(CreateFolderStates.folder_name)
async def create_folder(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await state.clear()
    add_to_json = json.load(open('C:/telegram-bot/data/db.json'))
    add_to_json['folders'].append(data['name'])
    with open('C:/telegram-bot/data/db.json', 'w') as f:
        json.dump(add_to_json, f, indent=2, ensure_ascii=False)
    await message.answer('Выберите куда сохранить.', reply_markup=folders_menu())
