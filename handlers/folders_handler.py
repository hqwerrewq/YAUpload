import json

from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from disk.connect import client
from keyboards.keyboard import folders_menu
from utils.states import CreateFolderStates

folder_router = Router()


@folder_router.callback_query(F.data == 'create_folder')
async def folder_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Назвиние папки: ')
    await state.set_state(CreateFolderStates.folder_name)


@folder_router.message(CreateFolderStates.folder_name)
async def create_folder(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await state.clear()
    add_to_json = json.load(open('C:/telegram-bot/data/db.json'))
    for folders_name in add_to_json['folders']:
        if folders_name.lower() in data['name'].lower():
            await message.answer('Такая папка уже есть, укажите другое название: ', reply_markup=folders_menu())
            break
    else:
        await client.mkdir(f'/{data['name']}/')
        await client.close()
        add_to_json['folders'].append(data['name'])
        with open('C:/telegram-bot/data/db.json', 'w') as f:
            json.dump(add_to_json, f, indent=2, ensure_ascii=False)
        await message.answer('Выберите куда сохранить.', reply_markup=folders_menu())
