from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile

from aiogram.utils import executor
import markups as nav

import os

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher(bot)

photo = InputFile('files/sleep.jpeg')


@dp.message_handler(text='/start')
async def command_start(message: types.message):
    await bot.send_message(message.from_user.id, 'Загружаем Слипи, твоего личного тренера по сну...')
    await bot.send_photo(message.from_user.id, photo=photo)
    await bot.send_message(message.from_user.id, '''Ты просыпаешься и осознаешь, что находишься в совершенно незнакомом месте.  
Это небольшая комната, похожая на отсек космического корабля. Её тускло освещает один маленький светильник. А из дальнего угла доносятся странные звуки...''',
                           reply_markup=nav.mainMenu)


@dp.message_handler(text='/help')
async def command_start(message: types.message):
    await bot.send_message(message.from_user.id, 'Помощи нет')


@dp.callback_query_handler(text='btnStep_1')
async def command_step_1(message: types.message):
    await bot.send_message(message.from_user.id, 'Ты выбрал вариант 1. Выбери новый вариант.',
                           reply_markup=nav.mainMenu)


@dp.callback_query_handler(text='btnStep_2')
async def command_step_2(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ты выбрал вариант 2. Выбери новый вариант.',
                           reply_markup=nav.mainMenu_2)


executor.start_polling(dp, skip_updates=True)
