import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Assalomu alaykum hurmatli ADMIN!!!\n\n 📌 ILTOMISNOMA\n\n❗️❗️❗️\n"
                "Iltimos, belgilangan formatda va tartib qoidalarga amal qilgan holda ushbu bot imkoniyatlaridan"
                " foydalaning")

        except Exception as err:
            logging.exception(err)








