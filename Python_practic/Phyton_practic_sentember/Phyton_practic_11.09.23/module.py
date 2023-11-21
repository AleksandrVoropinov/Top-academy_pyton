
# if __name__ == '__main__':
#     print('Я module')

# def summa(a, b, c):
#     return a + b + c
#
# print(summa(10, 10, 14))

# def print(string):
#     return
#
# print('Hello')

# value_1 = 10
#
# def my_function():
#     value_2 = 0
#     print(value_1)
#
# my_function()


# value_1 = 10  # Переменная внутри функции и глобальная это разные переменные
#
# def my_function():
#     value_1 = 0  # Переменная внутри функции и глобальная это разные переменные
#     print(value_1)
#
# my_function()
# print(value_1)

# value_1 = 10
#
# def my_function():
#     global value_1 и nonlocal value_1  # поиск глобальной и локальной переменной
#     value_1 = 0
#     print(value_1)
#
# my_function()
# print(value_1)

# val_1 = 1
#
# def func_1():
#    val_2 = 2
#    def func_2():
#        val_3 = 3
#        print(val_3)
#    print(val_2)
#    func_2()
#
# print(val_1)
# func_1()

# print(globals())
# import math
# print(globals())

# def check_is_happy_num(number: str) -> bool:
#     """
#     Проверяет является ли число счастливым.
#     :param number:
#     :return:
#     """
#     left: int = int(number[0]) + int(number[1]) + int(number[2])
#     right: int = int(number[3]) + int(number[4]) + int(number[5])
#     if left == right:
#         return True
#     return False
#
#
# print(check_is_happy_num('123420'))

# from typing import List
#
#
# def average_age(people: List[List]) -> float:
#     """
#     Функция среднего возраста
#     :param people: List[List]
#     :return: float
#     """
#     average: int = sum([i_human[1] for i_human in people])
#     return round(average / len(people), 1)
#
#
# people_list = [
#     ['Ivan', 35],
#     ['Petr', 27],
#     ['Anna', 18],
# ]
# print(average_age(people_list))

# Задание 2

from typing import List


# def number(num_1: int, num_2: int) -> None:
#     return[i for i in range(num_1, num_2 + 1) if i % 2 != 0]
#
#
# print(number(10,100))



# Задание 3

# from typing import List
#
# def print_symbol(lenght: int, direction: bool, symbol: str) -> None:
#     if direction:
#         print(symbol * lenght)
#     else:
#         for _ in range(lenght):
#             print(symbol)
#
#
# print_symbol(5, True, '*')
# print_symbol(5, False, '/')

# Задание 4

def simple_nums (start: int, end: int) -> None:
    for i in range(start,end):
        simple = True
        for j in range()
