from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN, ADMIN


from sql_requests.HelloMessage import HelloMessage
from sql_requests.CheckingSubscribe import Checking


bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

User = HelloMessage()
Check = Checking()


@dp.message_handler(content_types=["new_chat_members"])
async def greeting_messages(message: types.Message):
    msg = User.get_hello_message()
    if msg:
        await bot.send_message(message.chat.id, msg)
    else:
        user_name = message.new_chat_members[0].first_name
        await bot.send_message(message.chat.id, f"Добро пожаловать, {user_name}")


@dp.message_handler(commands='greeting')
async def change_greeting(message: types.Message):
    if message.from_user.id in ADMIN:
        User.delete_hello_message()
        new_greeting = message.text.replace('/greeting', '')[1:]
        User.add_hello_message(new_greeting)
        await bot.send_message(message.chat.id, f'Новое приветствие: \n"{new_greeting}"')


@dp.message_handler(commands='off')
async def off_check(message: types.Message):
    if message.from_user.id in ADMIN:
        Check.delete_row()
        Check.off_check()
        await message.reply('Выключил')


@dp.message_handler(commands='on')
async def on_check(message: types.Message):
    if message.from_user.id in ADMIN:
        Check.delete_row()
        Check.on_check()
        await message.reply('Включил')


@dp.message_handler(commands='change')
async def change_channel(message: types.Message):
    if message.from_user.id in ADMIN:
        new_channel = message.text.replace('/change', '')[1:]
        Check.change_channel(new_channel)
        await bot.send_message(message.chat.id, f'Изменения внесены"')


@dp.message_handler(lambda message: message.chat.type != 'private')
async def check_members(message: types.Message):
    if message.from_user.id not in ADMIN:
        result = Check.get_status()
        channel = Check.get_channel()
        answer = await bot.get_chat_member(channel, message.from_user.id)
        if result and answer.status != 'member':
            await message.delete()
            await bot.send_message(message.chat.id, f'@{message.from_user.username}\n\nВам нужно подписаться на: \n{channel}')


if __name__ == '__main__':
    executor.start_polling(dp)
