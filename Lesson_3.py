#1
# a = int(input("Введите делимое: "))
# b = int(input("Введите делитель: "))
#
# if b == 0:
#     print("Делитель не может быть равен нулю")
# else:
#     def my_division(a, b):
#         return a / b
#     print(my_division(a, b))

#2
# def my_func(**kwargs):
#     return kwargs
# print(my_func(
#     F_Name = 'Ivanov', S_Name = 'Ivan',
#     Born_year = 2000, Town = 'Moscow',
#     Email = 'john_doe@mail.ru', Tel = 88000777))
# Можно было сделать кортеж, через *args - на мой взгляд НЕ информативно и НЕ читабельно)))

#3
# a = int(input("Введите число 1: "))
# b = int(input("Введите число 2: "))
# c = int(input("Введите число 3: "))
#
# def my_func(a, b, c):
#     list = [a,b,c]
#     list.sort(reverse = True)
#     return list [0] + list [1]
# print(f"Сумма двух наибольших чисел равна: {my_func(a, b, c)}")

#4
# a = int(input("Введите действительное положительное число x: "))
# b = int(input("Введите целое отрицательное число y: "))
#
# if b >= 0:
#     print('Число НЕ отрицательное')
# else:
#variant_1
#     def my_func(a,b):
#         b = - b
#         result = 1
#         for i in range(b):
#             result *= a
#         return 1 / result
#     print(my_func(a, b))
#     print("{:.50f}".format(my_func(a, b))) # вариант если не подходит экспоненциальная запись
#variant_2
#     b = - b
#     result = 1 / (a ** b)
#     print(result)
#     print("{:.50f}".format(result)) # вариант если не подходит экспоненциальная запись

#5
# switch = True
# result = 0
# while switch == True:
#     list = input("Введите числа через пробел: ").split()
#     try:
#         def my_func(list):
#             intlist = [int(item) for item in list]
#             return sum(intlist)
#         result = result + my_func(list)
#         print(result)
#     except:
#         print ("Введен неверный символ!")
#         switch = False

#6
# list_1 = input("Введите текст на латинице через пробел: ")
# def int_func(x):
#         print(x.title())
#         return x
# int_func(list_1)
# Не понятно из условий , нужно ли разбивать строку по разделителю в список и менять букву в каждом элементе списка?
#7 (но я нашел решение))))
# list_1 = input("Введите текст на латинице через пробел: ").split()
# def int_func(list_1):
#     for el, value in enumerate(list_1):
#         list_1 [el] = str.title(value)
#     list_1 = " ".join(list_1)
#     print(list_1)
#     return  list_1
# int_func(list_1)








