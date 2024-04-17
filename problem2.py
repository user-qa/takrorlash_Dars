# 2. with context manageri orqali test.txt fayl oching va uni ichiga 1 dan 100 gacha bo'lgan sonlarni yozing.


# Bu solutiondan foydalanganda 1 dan 100gacha har birini alohida qatorga yozadi. Va bundan boshqa narsa qolmaydi.
# with open('1_dan_100_gacha_sonlar.txt', 'w') as file:
#     for i in range (1, 101):
#         file.write(str(i) + '\n')

# Bu solutiondan foydalanganda 1 dan 100gacha ketma-ket yozadi. Va bundan boshqa narsa qolmaydi.
# with open('1_dan_100_gacha_sonlar.txt', 'w') as file:
#     for i in range (1, 101):
#         file.write(str(i))


# Bu kod append qilib ketaveradi. Nechi marta run qilinsa shuncha append bo'ladi
# with open('1_dan_100_gacha_sonlar.txt', 'a') as file:
#     for i in range (1, 101):
#         file.write(str(i))