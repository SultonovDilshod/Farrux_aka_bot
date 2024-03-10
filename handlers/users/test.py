import time

from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from data.config import HOLDER, ADMINS
from loader import dp, bot, db
from keyboards.default.keyboards import main_menu_btn, yes_no
from states.Clean import Clean_base
from aiogram.dispatcher import FSMContext

users = db.select_all_users()


try:
    result_100 = ""
    for i in users[0:100]:
        result_100 += f"{i[0]}-{(i[1].split(' '))[0]} {(i[1].split(' '))[1]}-{i[2]}\n"
    print(result_100)
except:
    print("1-100 oraliqdagi BAZAda mavjud to'g'ri to'ldirilgan kursantlar ro'yxati mavjud emas")

