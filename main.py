from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

from menus.main_menu import main_menu
from menus.back_btn import menu_with_back_button

from menus.inline_menu.inline_menu_status import inline_menu_check_status


bot = Bot(TOKEN)
dp = Dispatcher(bot)


# TODO: Сделать возможность самостоятельного добавления текста для приветствия [не доделано]
@dp.message_handler(content_types=["new_chat_members"])
async def check_messages(message: types.Message):
    print(message)
    user_name = message.new_chat_members[0].first_name
    await bot.send_message(message.chat.id, f"Добро пожаловать, {user_name}!")


@dp.message_handler(lambda message: message.text != 'Проверка подписки')
async def verification_of_subscription(message: types.Message):
    link = '@TestProjectEva'
    admins = await bot.get_chat_administrators(link)
    is_admin = False

    for admin in admins:
        if message.from_user.id == admin.user.id:
            is_admin = True

    if is_admin:
        await bot.send_message(message.chat.id, 'Вая смари какой админ', reply_markup=main_menu)


# TODO: функция должна проверять статус проверки (брать из базы данных) [не доделано]
@dp.message_handler(lambda message: message.text == 'Проверка подписки')
async def subscription_verification_status(message: types.Message):
    await bot.send_message(message.chat.id, f"🔹 {message.text} 🔹", reply_markup=menu_with_back_button)
    await bot.send_message(message.chat.id, 'Статус проверки: Включен', reply_markup=inline_menu_check_status)


# TODO: Сделать запрос к БД для отключения проверки подписки [не доделано]
@dp.callback_query_handler(lambda call: call.data == 'off')
async def view_call(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)


# TODO: Сделать запрос к БД для включения проверки подписки [не доделано]
@dp.callback_query_handler(lambda call: call.data == 'on')
async def view_call(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)


if __name__ == '__main__':
    executor.start_polling(dp)
