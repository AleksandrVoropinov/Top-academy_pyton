#Пользователь вводит целое число - текущее время в часах. Если количество часов находится между 7 и 10,
#то программа должна вывести строку " Пора вставать!", иначе выведится строка " Ты проспал! ".
#Если введеное число отрицательное или больше 23, то программа должна вывести строку "Ошибка".
# Задание 1

# num = int(input("Введите число: "))
#
# if 7 <= num <= 10:
#     print("Пора вставать!")
#
# if num < 0 or num > 23:
#     print("Ошибка!")
#
# else:
#     print("Ты прорспал!")

# Задание 2

# num_1 = int(input("Введите результат по русскому языку: "))
# num_2 = int(input("Введите результат по математике: "))
# num_3 = int(input("Введите результат по физике: "))
#
# result = num_1 + num_2 + num_3
#
# if result >= 250:
#     print('Вы поступили')
# else:
#     print('Вы не поступили')

# ЦИКЛЫ
# import time
#
# for i in range(10):
#     time.sleep(1)
#     print(i)

# for _ in range(10):
#     print('Привет!')
#
# for i in 'phyton':
#     print(i + '*', end='')
#
# for i in '10':
#     if i == 3:
#         break
#     print(i)
# else:
#     print('ok')
#
# for i in range(0, 5):
#     if i == 3:
#         continue
#     print(i)
# else:
#     print('ok')
#
# for i in range(0, 5):
#     if i == 3:
#         exit(0)
#     print(i)
# else:
#     print('ok')

# start = int(input('Введите начало: '))
# end = int(input('Введите конец: '))
#
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(f'{i} является четным!')

# Пользователь вводит начало и конец диапазона, нужно вывести
# все числа в обратном порядке.

# start = int(input('Введите начало: '))
# end = int(input('Введите конец диапазона: '))
#
# for i in range(end, start - 1, - 1):
#     print(i)

#  = 1 + 2 + 3 + ... + 197 + 198 + 199 + 200

# summa = 0
# for i in range(1, 200):
#     summa += i
# print(f'Сумма ряда равна: {summa}')

# Факториал
# 3! = 1 * 2 * 3 = 6

# number = int(input('Введите число:'))
#
# factorial = 1
# for i in range(2, number + 1):
#     factorial *= i
# print(f'Факториал числа {number} равен {factorial}')

# Вывести таблицу умножения

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print()
#
# correct_pin = 1547
#
# for i in range(3):
#     pin = int(input('Введите ПИН-КОД: '))
#     if pin == correct_pin:
#         print('Ваш пин-код верный!')
#         break
#     else:
#         print(f'Повторите попытку!, Это ваша {i + 1} попытка')
#
# else:
#     print('Вы три раза ввели неправильный пин-код, ваша карта заблокирована!')

# Задание 1

# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
# summa = 0
# count = 0
# for i in range(start, end + 1):
#     summa += i
#     count += 1
# print(f'Сумма ряда равна: {summa}')
# print(f'Среднее арифметическое равно: {summa / count }')

# Задание 2 и 3

# line = int(input('Введите длину линии: '))
# Simbol = input('Введите символ: ')
#
# for i in range(line):
#     print(Simbol, end='')

# Задание 4

# num = int(input('Введите число: '))
#
# for i in range(1, 10):
#     result = i * num
#     print(f'{i} * {num} = {result}')

# Задание 5

# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
# num = int(input('Введите число: '))
#
# for i in range(start, end + 1):
#     if i == num:
#         print(f'!{i}!', end=' ')
#         continue
#     print(i, end=' ')
#
# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
# num = int(input('Введите число: '))
#
# for i in range(start, end + 1):
#     if i == num:
#         print(f'!{i}!', end=' ')
#     else:
#         print(i, end=' ')
