from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

mainMenu = InlineKeyboardMarkup(row_width=1)
mainMenu_2 = InlineKeyboardMarkup(row_width=1)
btnStep_1 = InlineKeyboardButton(text='Вариант 1', callback_data='btnStep_1')
btnStep_2 = InlineKeyboardButton(text='Вариант 2', callback_data='btnStep_2')
mainMenu.insert(btnStep_1)
mainMenu.insert(btnStep_2)
mainMenu_2.insert(btnStep_2)

