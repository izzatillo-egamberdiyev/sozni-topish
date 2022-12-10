aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shunday yozdik
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

#Kavdrat va kubni xisoblash
son = input("Istalgan sonni kiriting: ")
son = int(son)
kv = son ** 2
kub = son ** 3
print(f"{son} ning kvadrati: {kv}, kubi esa: {kub}")

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
yosh = input("Yoshingizni kiriting: ")
yosh = int(yosh)
t_yil = 2022 - yosh
print("Siz ", t_yil, " da tug'ilgansiz")

#Foydalanuvchidan ikki son kiritshni so'rab
#kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
son1 = input("Son kiriting: ")
son2 = input("Son kiriting: ")
son1 = int(son1)
son2 = int(son2)
print(f"""{son1} + {son2} = {son1 + son2}
{son1} - {son2} = {son1 - son2}
{son1} : {son2} = {son1 / son2}
{son1} x {son2} = {son1 * son2}
      """)