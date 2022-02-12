#1
# my_list = [45, 'один', 10 + 2j, True, 10.56]
# #если необходимо проверить весь список целиком
# for el in my_list:
#     print(type(el))
# если необходимо отдельно определить какой либо элемент в списке, подставляем в [..]
# номер индекса элемента из списка от 0 до 4
# print(type(my_list[0]))


#2
# list_1 = input("Введите элементы списка через запятую: ").split(',')
# for el in range(0, len(list_1)-1, 2):
#     list_1[el], list_1[el+1] = list_1[el+1], list_1[el]
# print(list_1)

#3
# list_timeyear = ['зима','зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']
# month = int(input("Введите номер месяца от 1 до 12: ")) - 1
# print(list_timeyear[month])

# dict_timeyear = {1:"зима",2:"зима",3:"весна",4:"весна",5:"весна",6:"лето",7:"лето",8:"лето",9:"осень",10:"осень",11:"осень",12:"зима"}
# month = int(input("Введите номер месяца от 1 до 12: "))
# print(dict_timeyear.setdefault(month))

#4
# my_string = input("Введите несколько слов через пробел: ").split()
#
# for index, value in enumerate (my_string):
#     my_string[index] = value[0:10]
#
# for el in enumerate (my_string, start=1): #как вывести 10 символов???
#     print(el)

#5
# my_list = [7, 5, 3, 3, 2]
# new_list = int(input("Введите любое натуральное число: "))
# my_list.append(new_list)
# my_list.sort(reverse = True)
# print(my_list)

#6
catalog = [
    (1, {"Named": "Computer", "price": 20000,"amount": 5,"ед.": 'шт'}),
    (2, {"Named": "Printer","price": 6000,"amount": 2,"ед.": 'шт'}),
    (3, {"Named": "Scanner","price": 2000,"amount": 7,"ед.": 'шт'}),
    (4, {"Named": "Keyboard","price": 200,"amount": 4,"ед.": 'шт'}),
    (5, {"Named": "Mouse","price": 200,"amount": 9,"ед.": 'шт'})
]
print(dict(1))


