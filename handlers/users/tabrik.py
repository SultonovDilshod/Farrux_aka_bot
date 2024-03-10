from datetime import datetime as dt

# t = '21.01.2002'
#
# day = t[:2]
# month = t[3:5]
# yosh = t[-4:]
# print(month)
# print(day)
# print(yosh)
#


# def ism():
#     tabrik = lambda name: f"Hello {name}"
#     now = dt.now()
#
#     FIO = "DIlshod"
#     birth = '21.01.2002'
#     if now.month == int(birth[3:5]) and now.day == int(birth[:2]):
#         words = tabrik(FIO)
#         print(words)
# ism()

import random as rd


def birt(name):
    a = f"Hurmatli qadrdonimiz {name}. Sizni tug'ilgan kuning bilan tabriklayman. Sizga sog'lik, farovonlik, farovonlik, baxt va omad tilayman. Har bir kuningiz rejalaringizni amalga oshirishga imkon bersin, har bir intilish shubhasiz muvaffaqiyat va farovonlikka olib kelsin. Ushbu bojxona tizimida general bo'lish nasib qilsin"
    b = f"Bizning aziz hamkasbimiz {name}. Tug'ilgan kuning bilan tabriklayman! Sizga olmos sog'liq, yorug'lik va quyoshli kunlar, barcha urinishlar va ishlarda muvaffaqiyat, moliyaviy barqarorlik va mustaqillik oilaviy qulaylik va iliqlik, tinchlik va qalbda sevgi va muhabbat tilayman. Bojxona tizimida esa general bo'lishingizni tilakdoshiman"
    c = f"Hurmatli {name}, tug`ilgan kuningiz bilan! Ko‘ngil hamisha ezgulikka ochiq, qalbi olijanob, ko‘rinishi go‘zal, xonadoni fayzu barakali bo‘lsin! Tananing sog'lom, ruhi kuchli bo'lishini tilab qolamiz! Bojxona tizimida esa general bo'lishingizni tilakdoshiman."
    d = f"Hamkasbimiz {name}, shukrona kuningiz muborak bo'lsin. Har yili bu 365 bo'sh sahifadan iborat kitob. Shunday ekan, har kuni hayotning barcha ranglarini ishlatib, asar yarating ... va har kuni yuzingizga nimadir yozganingizda tabassum paydo bo'lsin! Bu dunyodagi barcha go'zalliklarni ko'ring va barcha orzularingiz amalga oshsin. Tug'ilgan kuning bilan!!!"
    e = f"Hurmatli {name}, tug'ilgan kuning bilan tabriklayman! Sizga chin dildan eng yaxshi tilaklarimni tilayman. Shunday qilib, siz, aziz kichkina odamim, har bir zarradan, har bir hujayradan xursand bo'ling. Bu dunyodagi barcha yaxshiliklar va go'zalliklar sizning oyog'ingizda bo'lsin. Barcha orzular va orzular amalga oshsin. Bizning tizimni ham eng yorqin namunalaridan biri bo'ling!"
    f = f"Aziz va qadrli hamkasbimiz {name}, sizning bugungi shukrona kuningiz muborak bo'lsin! Har doim qalbingizda xotirjam bo'lsin, qalbingizda sevgi va baxt, iliq, yorqin muhit va uyda to'liq farovonlik bo'lsin. Yo'lda omad, ishda - foyda, har bir maqsadda - muvaffaqiyat kutsin. Hamma narsada uyg'unlik bo'lsin va hamma narsa siz uchun eng yaxshi tarzda ishlaydi."
    g = f"Qadrdonimiz {name}, sizning bugungi shukrona kuningiz muborak bo'lsin! Inson birdaniga hamma narsaga ega bo'lishi mumkin emas, shuning uchun ajoyib tug'ilgan kuningizda men tilayman:\n- ko'tarilish va pasayish;\n- og'riqsiz sevgi;\n- yo'qotmasdan mehr;\n- xiyonatsiz do'stlik;\n- hiyla-nayrangsiz farovonlik;\n- dori vositalarisiz salomatlik;\n- chegarasiz muvaffaqiyat;\n- hisobsiz yillar;\n- cheksiz baxt;\n- porasiz general bo'lish :) !"
    h = f"Hamkasbimiz {name}, sizning bugungi shukrona ayyomingiz muborak bo'lsin!  Faqat ijobiy haqiqatlar, energiya, ilhom, yaxshi sog'liq va farovonlik. Hech qachon umidingizni yo'qotmang va oxirigacha adolatli va munosib odamning pozitsiyasiga rioya qiling. Butun qalbingiz va nozik qalbingiz bilan seving, sajda qiling, vijdoningiz bilan yashang va sizga nasib etgan daqiqalardan insoniy zavqlaning."
    lt = [a, b, c, d, e, f, g, h]
    return rd.choice(lt)


birt("DIHSKOOOOOOOOOOOOOOO")
