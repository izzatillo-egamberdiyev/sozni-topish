matn = "matn, o‘ziga Xos tarzda, bir nechta jumlalardan tarkib topadi."
print(matn.upper()) #Barcha xarflar kotta
print(matn.lower()) #Barca xarflar kichik
print(matn.capitalize()) #eng birinchi so'z 1-xarf kotta
print(matn.title()) #BARCHA SO'ZNI 1- XARFI KOTTA

#Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
#lstrip() — matn boshidagi bo'shliqni,
#rstrip() – matn oxiridagi bo'shliqni,
#strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")