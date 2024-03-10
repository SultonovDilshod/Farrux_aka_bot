from aiogram import types
import sqlite3
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command, Text
from keyboards.default.keyboards import main_menu_btn
from states.start_log_two import Start_log_two
from aiogram.dispatcher import FSMContext
from loader import db, dp, bot
from data.config import ADMINS


@dp.message_handler(text="📝 O'chirish", user_id=ADMINS)
async def answer_phone(message: types.Message):
    await message.answer("Kursant ID raqamini kiriting:")
    await Start_log_two.option_one_two.set()


@dp.message_handler(state=Start_log_two.option_one_two)
async def answer_phone(message: types.Message, state: FSMContext):
    try:

        i = db.select_user(student_id=message.text)
        db.delete_user(int(i[0]))
        result = f"Quyidagi foydalanuvchi o'chrildi\n" \
                 f"👤 --- TMC ID: {i[0]}\n" \
                 f"♦️ F.I.O: {i[1]}\n" \
                 f"♦️ Guruhi: {i[2]}\n" \
                 f"♦️ Sanasi: {i[3]}\n"

        await message.answer(result)
    except:
        await message.answer("Kursant ID raqami xato.\nIltmos /allusers_list orqali ID raqamni aniqlashtiring",
                             reply_markup=main_menu_btn)
    await state.finish()
