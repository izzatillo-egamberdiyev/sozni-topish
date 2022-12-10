# Dasturchi: Egamberdiyev Izzatillo
# Sana: 10.12.2022
# Mohirdev.uz python kursi topshirig'i   

from random import randint

#  Men o'ylagan sonni robot topadi
def sonni_topish():
    urunish1 = 0
    son = randint(1,10)
    print("Men 1 dan 10 gacha bo'lgan sonlardan birini tanladim. Topishga urunib ko'ring")
    while True:      
        raqam = int(input("Son tanlang "))
        urunish1 +=1
        if son == raqam:
            print(f"Yutdingiz siz  {urunish1} marta topdingiz")
            break
        elif son > raqam:
            print("Men tanlagan son bundan kattaroq")
        elif son < raqam:
            print("Men tanlagan son bundan kichikroq")
    return urunish1



# Robot o'ylagan sonni men topaman
def sonni_taxminlash():
    urunishlar = 0
    start = 1
    finish = 10
    while True:
        urunishlar += 1
        if start != finish:
            son = randint(start,finish)
        else:
            son = finish
        answer = input(f"Siz {son} ni o'yladingiz. To'g'ri bo'lsa  (t), sizning son kattaroq bo'lsa (+), kichikroq bo'lsa (-) yuboring ".lower())
        if answer == '-':
            finish = son - 1
        elif answer == "+":
            start = son + 1
        elif answer == 't':
            print(f"{urunishlar} martada topdim")
            break
        else:
            print("Noto'g'ri belgi kiritdingiz! Qaytab tahmin qilaman")
            urunishlar -= 1
    return urunishlar
            

def sonni_top():
    odam = sonni_topish()
    tanlov = input("Endi siz son o'ylang men topishga urunib ko'raman. Rozi bo'lsangiz 1, aks xolda istalgan tugmani bosing: ")
    if tanlov == '1':
        print("Ajoyib. Men o'ylagan soningizni tahmin qilishni boshladim\n")
        robot = sonni_taxminlash()
        if odam > robot:
            print(f"O'yinda men g'olib bo'ldim.\nHisob: {odam}:{robot}")
        else:
            print(f"O'yinda siz g'olib bo'ldingiz\nHisob: {odam}:{robot}")
    else:
        print("Oyinimiz yakunlandi. E'tiboringiz uchun rahmat")
    
sonni_top()