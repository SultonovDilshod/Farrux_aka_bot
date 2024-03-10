from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("info", "Bot haqida to'liq informatsiya"),
            types.BotCommand("help", "Yordam ko'rsatish"),
            types.BotCommand("allusers_list", "Yordam ko'rsatish"),
        ]
    )
