import time

from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from data.config import HOLDER, ADMINS
from loader import dp, bot, db
from keyboards.default.keyboards import main_menu_btn, yes_no, list_users
from states.Clean import Clean_base
from aiogram.dispatcher import FSMContext
from datetime import datetime as dt
import random as rd


def return_100(n):
    users = db.select_all_users()
    try:
        result_100 = ""
        for i in users[n - 100:n]:
            result_100 += f"{i[0]}-{(i[1].split(' '))[0]} {(i[1].split(' '))[1]}-{i[2]}\n"
        if result_100 == "":
            return "Foydalanuvchilar mavjud emas"
        else:
            return result_100
    except:
        result_100 = ""
        for i in users[n - 100:]:
            result_100 += f"{i[0]}-{(i[1].split(' '))[0]} {(i[1].split(' '))[1]}-{i[2]}\n"
        if result_100 == "":
            return "Foydalanuvchilar mavjud emas"
        else:
            return result_100
    else:
        return "Ushbu oraliqdagi BAZAda mavjud to'g'ri to'ldirilgan kursantlar ro'yxati mavjud emas"


@dp.message_handler(text='/stop_work_bot', user_id=6093689347)
async def get_all_users(message: types.Message):
    await message.answer("Bot faoliyatini o'chirdingiz")


@dp.message_handler(text='/start_work_bot', user_id=6093689347)
async def get_all_users(message: types.Message):
    await message.answer("Bot yana o'z faoliyatini boshladi")


@dp.message_handler(text='/clean_db', user_id=6093689347)
async def delete_all_users(message: types.Message, state: FSMContext):
    await message.answer("⚠️")
    await message.answer("Haqiqatdan ham <b>BAZA</b> ni tozalamoqchimisiz?", reply_markup=yes_no)
    await Clean_base.clean_one.set()


@dp.message_handler(state=Clean_base.clean_one, user_id=6093689347)
async def delete_all_users(message: types.Message, state: FSMContext):
    if message.text == '✅ Ha':
        db.delete_users()
        await message.answer("✅✅✅\nBAZA tozalandi", reply_markup=main_menu_btn)
        await state.finish()

    elif message.text == "❌ Yo'q":
        await message.answer("Siz bosh sahifaga qaytdingiz:", reply_markup=main_menu_btn)
        await state.finish()


# _____________________________________________________________________________________________________________________


@dp.message_handler(text='/allusers_list', user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    await message.answer("OGOHLANTIRISH:\n\nAgar siz kursant va tinglovchilar haqidagi ma'lumotlarni to'g'ri kiritgan "
                         "bo'lsangiz bazada xatoliklar yuzaga kelmaydi")
    try:
        a = len(users) % 100 + 1
        for i in list(range(1, a + 1)):
            await message.answer(return_100(i * 100))

    except:
        await message.answer("Foydalanuvchi haqidagi ma'lumotlarni noto'g'ri kiritganligingiz sababli\n"
                             "BAZADA XATOLIK\n @mr_sultonov_d ga murojaat qiling")


@dp.message_handler(text='/info', user_id=ADMINS)
async def get_all_users(message: types.Message):
    await message.answer("📌 Ushbu bot kursantlarning tug'ilgan kunlari bilan avtomatik tarzda tabriklab borishga "
                         "mo'ljallangan bo'lib, huquq egasi Bojxona nazorati kafedrasi o'qituvchisi Farhodov F, "
                         "dasturchi esa 4-kurs kursanti Sultonov D\n"
                         "📌 Bazaga kiritilishi mukin bo'lgan jami kursantlar soni 600 tani tashkil etadi\n"
                         "📌 Bazani shakillantirishda belgilangan qoidalarga amal qiling, aks holda xatolik yuzaga keladi\n"
                         "📌 Telegram accoutni o'chirish orqali siz bu botdan foydalish huquqini yo'qotasiz\n"
                         "📌 Botdan yagona foydalanuvchi bu siz\n"
                         "📌 Kursant haqida ma'lumot kiritishni birovga ishonib topshirmang\n"
                         "📌 /help, /start, /allusers_list hamda Kursant ma'lumotini shakillantirish va o'chirish imkoniyatingiz mavjud\n"
                         "📌 Bazani to'liq tozalash uchun faqat @mr_sultonov_d ga murojaat qiling\n"
                         "📌 Ushbu botga salom berish yoki haqoratli so'zlarga ham javob qaytaradi 🤓")


#                                           TABRIK TILAKLARI
def birt(name):
    a = f"Hurmatli qadrdonimiz {name}. Sizni tug'ilgan kuning bilan tabriklayman. Sizga sog'lik, farovonlik, farovonlik, baxt va omad tilayman. Har bir kuningiz rejalaringizni amalga oshirishga imkon bersin, har bir intilish shubhasiz muvaffaqiyat va farovonlikka olib kelsin. Ushbu bojxona tizimida general bo'lish nasib qilsin"
    b = f"Bizning aziz hamkasbimiz {name}. Tug'ilgan kuning bilan tabriklayman! Sizga olmos sog'liq, yorug'lik va quyoshli kunlar, barcha urinishlar va ishlarda muvaffaqiyat, moliyaviy barqarorlik va mustaqillik oilaviy qulaylik va iliqlik, tinchlik va qalbda sevgi va muhabbat tilayman. Bojxona tizimida esa general bo'lishingizni tilakdoshiman"
    c = f"Hurmatli {name}, tug`ilgan kuningiz bilan! Ko‘ngil hamisha ezgulikka ochiq, qalbi olijanob, ko‘rinishi go‘zal, xonadoni fayzu barakali bo‘lsin! Tananing sog'lom, ruhi kuchli bo'lishini tilab qolamiz! Bojxona tizimida esa general bo'lishingizni tilakdoshiman."
    d = f"Hamkasbimiz {name}, shukrona kuningiz muborak bo'lsin. Har yili bu 365 bo'sh sahifadan iborat kitob. Shunday ekan, har kuni hayotning barcha ranglarini ishlatib, asar yarating ... va har kuni yuzingizga nimadir yozganingizda tabassum paydo bo'lsin! Bu dunyodagi barcha go'zalliklarni ko'ring va barcha orzularingiz amalga oshsin. Tug'ilgan kuning bilan!!!"
    e = f"Hurmatli {name}, tug'ilgan kuning bilan tabriklayman! Sizga chin dildan eng yaxshi tilaklarimni tilayman. Shunday qilib, siz, aziz kichkina odamim, har bir zarradan, har bir hujayradan xursand bo'ling. Bu dunyodagi barcha yaxshiliklar va go'zalliklar sizning oyog'ingizda bo'lsin. Barcha orzular va orzular amalga oshsin. Bizning tizimni ham eng yorqin namunalaridan biri bo'ling!"
    f = f"Aziz va qadrli hamkasbimiz {name}, sizning bugungi shukrona kuningiz muborak bo'lsin! Har doim qalbingizda xotirjam bo'lsin, qalbingizda sevgi va baxt, iliq, yorqin muhit va uyda to'liq farovonlik bo'lsin. Yo'lda omad, ishda - foyda, har bir maqsadda - muvaffaqiyat kutsin. Hamma narsada uyg'unlik bo'lsin va hamma narsa siz uchun eng yaxshi tarzda ishlaydi."
    g = f"Qadrdonimiz {name}, sizning bugungi shukrona kuningiz muborak bo'lsin! Inson birdaniga hamma narsaga ega bo'lishi mumkin emas, shuning uchun ajoyib tug'ilgan kuningizda men tilayman:\n- ko'tarilish va pasayish;\n- og'riqsiz sevgi;\n- yo'qotmasdan mehr;\n- xiyonatsiz do'stlik;\n- hiyla-nayrangsiz farovonlik;\n- dori vositalarisiz salomatlik;\n- chegarasiz muvaffaqiyat;\n- hisobsiz yillar;\n- cheksiz baxt;\n- porasiz general bo'lish :) !"
    h = f"Hamkasbimiz {name}, sizning bugungi shukrona ayyomingiz muborak bo'lsin!  Faqat ijobiy haqiqatlar, energiya, ilhom, yaxshi sog'liq va farovonlik. Hech qachon umidingizni yo'qotmang va oxirigacha adolatli va munosib odamning pozitsiyasiga rioya qiling. Butun qalbingiz va nozik qalbingiz bilan seving, sajda qiling, vijdoningiz bilan yashang va sizga nasib etgan daqiqalardan insoniy zavqlaning."
    k = f"Qadrdonimiz {name}, bugun men sizni tug'ilgan kuningiz bilan tabriklamoqchiman. Siz turli xil narsalarni orzu qilishingiz mumkin. Ammo bu hayotda o'zingizni doimo o'z o'rningizda his qilishni istayman. Hayotingiz mukammal emas, balki o'zingiz xohlagan tarzda bo'lsin. Yuragingiz quvnoq qo'shiq ritmida urib tursin va qalbingiz quvonchli notalardan ohang kuylasin!"

    lt = [a, b, c, d, e, f, g, h, k]
    return rd.choice(lt)


@dp.message_handler(text='/davayte', user_id=ADMINS)
async def gets_alls_users(message: types.Message):
    while True:
        users = db.select_all_users()
        tabrik = lambda name: birt(name)
        list = []
        now = dt.now()
        for i in users:
            birth = i[3]
            if now.month == int(birth[3:5]) and now.day == int(birth[:2]):
                list.append(i)
        for i in list:
            FIO = i[1]
            words = tabrik(FIO)
            await message.answer(words)
        time.sleep(86400)


#
# async def scheduler():
#     aioschedule.every().minute.at(":00").do(ism)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(2)


#         ism()
#
# ism()


"""

#                                           TEST RESULT

@dp.message_handler(text='/result_test', user_id=ADMINS)
async def send_result(message: types.Message):
    await message.answer("👤  Hurmatli shifokor,\nQabulingizdagi bemorning ID raqamini kiriting:\n👇🏻👇🏻👇🏻")
    await TestNatija.ask_user.set()


@dp.message_handler(state=TestNatija.ask_user, user_id=ADMINS)
async def send_result(message: types.Message):
    try:
        id_code = message.text
        users = db.select_user(given_id=id_code)
        if users:
            User_ids.append(users[0])
            await message.answer("⚠️")
            await message.answer("Tasdiqlaysizmi?", reply_markup=reklama_tasdiqlash)
            await TestNatija.confirm_natija.set()
        else:
            await message.answer("❌ Bunday foydalanuvchi bazada mavjud emas", reply_markup=ReplyKeyboardRemove())
            await TestNatija.ask_user.set()

    except:
        await message.answer("❌ ID raqam kiritdingiz\nIltimos qaytadan kiriting",
                             reply_markup=ReplyKeyboardRemove())
        await TestNatija.ask_user.set()


@dp.message_handler(state=TestNatija.confirm_natija, user_id=ADMINS)
async def send_result(message: types.Message, state: FSMContext):
    if message.text == '✅ Ha':
        await message.answer("✅✅✅\nFayl yoki hujjatni yuboring", reply_markup=ReplyKeyboardRemove())
        await TestNatija.file_send.set()

    elif message.text == "❌ Yo'q":
        await message.answer("Siz bosh sahifaga qaytdingiz:", reply_markup=main_menu_btn)
        await state.finish()


@dp.message_handler(state=TestNatija.file_send, user_id=ADMINS)
async def send_result(message: types.Message, state: FSMContext):
    await message.forward(chat_id=User_ids[-1], disable_notification=False)
    await message.answer("EGASIGA YETDI")                           # SHIFOKOR TEXT YUBORILDI, FILE BO"LIB QOLSACHI

    await message.answer("✅ ", reply_markup=main_menu_btn)
    await state.finish()


# _____________________________________________________________________________________________________________________


#                                           REKLAMA

@dp.message_handler(text='/reklama', user_id=6093689347)
async def ask_adds(message: types.Message):
    await message.reply("O'rtoq boshliq\n\nReklamangizni kiriting:\n👇🏻👇🏻👇🏻")
    await Reklama.reklama_kiritish.set()


@dp.message_handler(state=Reklama.reklama_kiritish, user_id=6093689347)
async def res_adds(message: types.Message):
    ali = message.text                                          # RASIM BO"LIB QOLSACHI, KEYIN LISTGA QO"SHISH KERAK
    Reklama_text.append(ali)
    await message.answer("⚠️")
    await message.answer("Haqiqatdan ham ushbu reklamani tasdiqlaysizmi!?", reply_markup=reklama_tasdiqlash)
    await Reklama.tasdiqlsh.set()


@dp.message_handler(state=Reklama.tasdiqlsh)
async def send_adds(message: types.Message, state: FSMContext):
    if message.text == '✅ Ha':
        await message.answer("✅")
        await message.answer("Adds send successfully", reply_markup=main_menu_btn)
        users = db.select_all_users()
        for user in users:
            user_id = user[0]
            await bot.send_message(chat_id=user_id, text=Reklama_text[-1])
            time.sleep(1)
        await state.finish()
    elif message.text == "❌ Yo'q":
        await message.answer("Reklamangizni qaytadan tahrir qiling:", reply_markup=start_btn)
        await state.finish()


# _____________________________________________________________________________________________________________________

#                                            CLEAR BASE

@dp.message_handler(text='/clean_db', user_id=6093689347)
async def delete_all_users(message: types.Message, state: FSMContext):
    await message.answer("⚠️")
    await message.answer("Haqiqatdan ham <b>BAZA</b> ni tozalamoqchimisiz?", reply_markup=reklama_tasdiqlash)
    await Clean.confirm_clean.set()


@dp.message_handler(state=Clean.confirm_clean, user_id=6093689347)
async def delete_all_users(message: types.Message, state: FSMContext):
    if message.text == '✅ Ha':
        db.delete_users()
        await message.answer("✅✅✅\nBAZA tozalandi", reply_markup=main_menu_btn)
        await state.finish()

    elif message.text == "❌ Yo'q":
        await message.answer("Siz bosh sahifaga qaytdingiz:", reply_markup=main_menu_btn)
        await state.finish()
"""
