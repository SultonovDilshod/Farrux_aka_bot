# TEST ishlashni tekshirish

# from sqlite import DataBase
#
# def test():
#     db = DataBase()
#     db.create_table_users()
#     db.add_user("Dilshod", "120q", "+55115195")
#     db.add_user("Halim", "220q", "+55115195")
#     db.add_user("Kalim", "320q", "+55115195")
#     db.add_user("Charim", "420q", "+55115195")
#     db.add_user("Alim", "520q", "+55115195")
#
#     users = db.select_all_users()
#     print(f"Barcha foydalanuvchilar: {users}")
#
#     user = db.select_user(student_name="Dilshod")
#     print(f"Bitta foydalanuvchini ko'rish {user}")
#
#
# test()


# Exceldan db ga o'girish


from sqlite import DataBase
import pandas as pd

df = pd.read_excel('kun.xlsx')
db = DataBase()
db.create_table_users()

for i, n in df.iterrows():
    db.add_user(str(n['name']), str(n['group']), str(n['date']))
print('Finish')





# # ID raqam generatsiya qilish

# from datetime import datetime as dt
# now_time = dt.now()
# sec = str(now_time.time())
# id = (int(f"{sec[:2]}{sec[3:5]}{now_time.second}{now_time.month}{now_time.day}{now_time.microsecond}")+25022002)*14
#
# print(id)

