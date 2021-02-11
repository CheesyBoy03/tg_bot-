from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

change_greeting = KeyboardButton('Поменять приветствие')
check_for_subscription = KeyboardButton('Проверка подписки')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(change_greeting, check_for_subscription)
