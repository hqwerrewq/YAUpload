from aiogram.fsm.state import StatesGroup, State


class CreateFolderStates(StatesGroup):
    folder_name = State()
