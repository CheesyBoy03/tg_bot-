from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

back_button = KeyboardButton('Назад')
menu_with_back_button = ReplyKeyboardMarkup(resize_keyboard=True).add(back_button)
