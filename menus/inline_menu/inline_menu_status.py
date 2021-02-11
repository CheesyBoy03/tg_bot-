from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

status = 'off'

off_status = InlineKeyboardButton('Выключить', callback_data='off')
on_status = InlineKeyboardButton('Включить', callback_data='on')

inline_menu_check_status = InlineKeyboardMarkup().add(off_status, on_status)
