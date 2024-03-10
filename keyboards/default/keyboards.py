from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏥 Qo'shish")],
        [KeyboardButton(text="📝 O'chirish")],
        [KeyboardButton(text='📋 Bazani tozalash')],
    ], resize_keyboard=True
)

yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✅ Ha')],
        [KeyboardButton(text="❌ Yo'q")]
    ], resize_keyboard=True
)
list_users = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='100'), KeyboardButton(text='200'), KeyboardButton(text='300'), KeyboardButton(text='400')],
        [KeyboardButton(text='500'), KeyboardButton(text='600'), KeyboardButton(text='700'), KeyboardButton(text='800')],
        [KeyboardButton(text='900'), KeyboardButton(text='1000'), KeyboardButton(text='1100'), KeyboardButton(text='1200')],
        [KeyboardButton(text='1300'), KeyboardButton(text='1400'), KeyboardButton(text='1500'), KeyboardButton(text='1600')],
    ], resize_keyboard=True
)
