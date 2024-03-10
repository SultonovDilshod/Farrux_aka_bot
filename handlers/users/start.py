from aiogram import types
import sqlite3
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command, Text
from keyboards.default.keyboards import main_menu_btn

from loader import db, dp, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    sms='Assalomu alaykum'
    await bot.send_message(chat_id=ADMINS[0], text=sms)
    await message.answer(
        f"👇👇👇\nSizning ushbu botda quyidagi imkoniyatlaringiz mavjud:", reply_markup=main_menu_btn)
    await message.answer("❗️❗️❗️ OGOHLANTIRISH:\n\nAgar siz kursant va tinglovchilar haqidagi ma'lumotlarni to'g'ri kiritgan "
                         "bo'lsangiz bazada xatoliklar yuzaga kelmaydi\\BUNDAY MASULYATLI ISHNI KURSANTGA ISHONIB TOPSHIRMANG")
