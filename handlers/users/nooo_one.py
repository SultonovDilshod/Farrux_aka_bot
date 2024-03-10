from aiogram import types
import sqlite3
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command, Text
from keyboards.default.keyboards import main_menu_btn, yes_no
from states.start_log import Start_log
from aiogram.dispatcher import FSMContext

from loader import db, dp, bot
from data.config import ADMINS

from datetime import datetime as dt


@dp.message_handler(text="🏥 Qo'shish", user_id=ADMINS)
async def qushish_one(message: types.Message):
    await message.answer("✅ Jarayon boshlandi")
    await message.answer("1️⃣ Iltimos kursant ism va familyasini kiriting:\n\n<i>Karimov Karimjon Karimjon o'g'li</i>")
    await Start_log.option_one.set()


@dp.message_handler(state=Start_log.option_one)
async def answer_phone(message: types.Message, state: FSMContext):
    await message.answer("2️⃣ Iltimos kursant guruhini kiriting:\n\n<i>120</i>")
    student_full_name = message.text
    await state.update_data(
        {"student_full_name": student_full_name}
    )
    await Start_log.option_two.set()


@dp.message_handler(state=Start_log.option_two)
async def answer_phone(message: types.Message, state: FSMContext):
    await message.answer("3️⃣ Iltimos kursant tug'ulgan sanani quyidagi formatda kiriting:\n\n<i>25.02.2002</i>")
    student_group = message.text
    await state.update_data(
        {"student_group": student_group}
    )
    await Start_log.option_three.set()


@dp.message_handler(state=Start_log.option_three)
async def answer_phone(message: types.Message, state: FSMContext):
    student_birthday = message.text
    # now_time = dt.now()
    # sec = str(now_time.time())
    # given_id = (int(f"{sec[:2]}{sec[3:5]}{now_time.second}{now_time.month}{now_time.day}{now_time.microsecond}") + 25022002) * 14
    #
    await state.update_data(
        {"student_birthday": student_birthday}
    )
    data = await state.get_data()
    student_full_name = data.get('student_full_name')
    student_group = data.get('student_group')
    student_birthday = data.get('student_birthday')

    await message.answer(f"Kiritilgan ma'lumotlarni tasdiqlaysizmi:\n\n"
                         f"Full name: {student_full_name}\n"
                         f"Group: {student_group}\nDate of birth: {student_birthday}", reply_markup=yes_no)
    await Start_log.option_four.set()


@dp.message_handler(state=Start_log.option_four)
async def answer_phone(message: types.Message, state: FSMContext):
    if message.text == '✅ Ha':
        data = await state.get_data()
        # given_id = data.get('given_id')
        student_full_name = data.get('student_full_name')
        student_group = data.get('student_group')
        student_birthday = data.get('student_birthday')

        try:
            db.add_user(student_name=student_full_name, student_group=student_group,
                        student_birth=student_birthday)
            await message.answer("✅ Ma'lumotlar muvaffaqiyatli kiritildi", reply_markup=main_menu_btn)
            await message.answer(f"2️⃣ FIO: {student_full_name}\n"
                                 f"3️⃣ Guruhi: {student_group}\n"
                                 f"4️⃣ Tug'ilgan sanasi: {student_birthday}")
        except sqlite3.IntegrityError as err:
            await message.answer("‼️‼️‼️\n\nKechirasiz siz xatolikka yo'l qo'ydingiz. Qaytadan urinib ko'ring")
            await state.finish()



    elif message.text == "❌ Yo'q":
        await message.answer("❌ Ma'lumot tasdiqlanmadi", reply_markup=main_menu_btn)
    await state.finish()
