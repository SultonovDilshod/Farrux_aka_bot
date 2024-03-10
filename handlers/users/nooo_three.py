from aiogram import types
import sqlite3
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command, Text
from keyboards.default.keyboards import main_menu_btn, yes_no
from states.start_log_three import Start_log_three

from aiogram.dispatcher import FSMContext

from loader import db, dp, bot
from data.config import ADMINS


@dp.message_handler(text='📋 Bazani tozalash', user_id=ADMINS)
async def answer_phone(message: types.Message):
    await message.answer("‼️‼️‼️\n\nHaqiqatdan ham bazani butunlay tozalamoqchimisiz", reply_markup=yes_no)
    await Start_log_three.option_one_three.set()


@dp.message_handler(state=Start_log_three.option_one_three)
async def answer_phone(message: types.Message, state: FSMContext):
    if message.text == '✅ Ha':
        await message.answer("✅ ✅ ✅ \n\nBu qaror nozik bo'lganligi uchun @mr_sultonov_d ga aloqaga chiqing."
                             "Chunki bu bazani qaytadan tiklashning iloji yo'q", reply_markup=main_menu_btn)

    elif message.text == "❌ Yo'q":
        await message.answer("❌ Ma'lumot tasdiqlanmadi", reply_markup=main_menu_btn)
    await state.finish()

