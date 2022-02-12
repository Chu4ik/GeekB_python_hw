#1)
# a = 2
# b = 2
# print(a + b)

# Name = input(' Введите Ваше имя: ')
# Profession = input(' Введите Вашу профессию: ')
# Age = input(' Введите Ваш возраст: ')
# print (f"Меня зовут {Name}, Я - {Profession}, мне - {Age}")

#2)
# sec = int(input('Введите время в секундах: '))
# hours = sec//3600
# minutes = sec%3600//60
# seconds = sec%3600%60
# print(f"{hours}:{minutes}:{seconds}")
#поработать над форматированием и выводом - нули перед минутами и секундами???!!!

#3)
# n = input("Введите число 'n': ")
# score_2 = n + n
# score_3 = n + score_2
# print(int(score_3) + int(score_2) + int(n))

#4)
# score = int(input("Введите любое целое положительное число: "))
# if score < 9:
#     print("Вы ввели недопустимое число")
# else:
#     r = 1
#     while score > 0:
#         d = score % 10
#         score //= 10
#         if d >= r:
#             r = d
#     print("Самая большая цифра: ", r)

#5) + #6)
# indicator_1 = int(input("Введите сумму выручки: "))
# indicator_2 = int(input("Введите сумму издержек: "))
# fin_rez = indicator_1 - indicator_2
# profitability = (round(fin_rez / indicator_1, 2))
# if fin_rez >= 0:
#     print("Ваша прибыль составила: ", fin_rez)
#     print("Ваш рентабельность составила: ", profitability) #подумать как вывести в %
#     indicator_3 = int(input("Введите количество сотрудников: "))
#     print("Прибыль на одного сотрудника составила: ", int(fin_rez / indicator_3))
# else:
#     print("Ваш убыток составил: ", fin_rez)


#7)
# distance_km = int(input("Введите раасстояние за первый день: "))
# normative_km = 3
# Day = 1
#
# while distance_km < normative_km:
#     distance_km = distance_km * 1.1
#     Day = Day + 1
#     print(f"{Day} день - результат {round(distance_km, 2)}") #убрать нули после запятой!!!
#     if distance_km >= normative_km :
#         print(f"На {Day} день спортсмен достигнет результат — не менее 3 км")