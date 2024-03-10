from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Commands: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/@mr_sultonov_d - Barcha muammolarning yechimi 🤓"
            )
    
    await message.answer("\n".join(text))
