#     1- topshiriq
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, 
# lug'at ko'rinishida qaytaruvchi funksiya yozing. 
# Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
def registration(name, lastName, birthday, phone, born=None, mail=None):
    info = {
        'name' : name,
        'lastName' : lastName,
        'birthday' : birthday,
        'age' : 2020 - int(birthday),
        'born' : born,
        'mail' : mail,
        'phone' : phone,
    }
    return info

# print(registration(name="Izzatillo", lastName="Egamberdiyev", birthday=2002, mail='liderkoder', phone="+998997933976"))

#  2 - topshiriq
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

# def kattasi(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max

def max_num(num1,num2,num3):
    numbers = sorted([num1,num2,num3])
    return numbers[-1]

# print(max_num(2,9,1))

# Tub sonlar
def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar