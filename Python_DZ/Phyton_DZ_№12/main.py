# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/

# a = float(input('Введите число: '))
# b = float(input('Введите число: '))
# c = input('Выберите операцию + - * /: ')
# if b == 0 and (c in ['/']):
#     print('Деление на 0!')
# elif c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     print(a / b)

# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчи-
# тать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

# import random
#
# n = 10
# matrix = [random.randint(-10, 10) for i in range(n)]
# print(matrix)
# min_element = matrix[0]
# max_element = matrix[0]
# neg_count = 0
# pos_count = 0
# zero_count = 0
#
# for i in range(n):
#     if matrix[i] < min_element:
#         min_element = matrix[i]
#     if matrix[i] > max_element:
#         max_element = matrix[i]
#     if matrix[i] < 0:
#         neg_count += 1
#     elif matrix[i] > 0:
#         pos_count += 1
#     else:
#         zero_count += 1
#
# print("Максимальный элемент: ", max_element)
# print("Минимальный элемент: ", min_element)
# print("Количество положительных элементов: ", pos_count)
# print("Количество отрицательных элементов: ", neg_count)
# print("Количество нулей: ", zero_count)
