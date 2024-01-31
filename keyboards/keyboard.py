from aiogram.types import (
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.loadDB import load_json


# class Pagination(CallbackData):
#     action: str
#     page: int


def folders_menu(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Создать папку:', callback_data='create_folder')
    )
    for folder in load_json():
        builder.row(
            InlineKeyboardButton(text=folder, callback_data=f'{folder}'),
            width=1
        )
    return builder.as_markup()
