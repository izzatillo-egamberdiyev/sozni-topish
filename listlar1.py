#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
ismlar = ['Nurmuhammad', 'Abbos']
print(ismlar[0], " ahvollar qalay?\n", ismlar[1], " bilan gaplashdingmi?")
#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, 
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
t_shaxslar = ["Amir Temur","Ibn Sino"]
z_shaxslar = ["Muhammadali Eshonqulov", "Davronbek Turdiyev",2]
tarixiy = t_shaxslar.pop(1)
zamonaviy = z_shaxslar.pop(0)
print(f"Men tarixiy shaxslardan {tarixiy} bilan, Zamonaviy shaxslardan esa {zamonaviy} bilan suhbatlashishni hohlardim! ")

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
print(mevalar)