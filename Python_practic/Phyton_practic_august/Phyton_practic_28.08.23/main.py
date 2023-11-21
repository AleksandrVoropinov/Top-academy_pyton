# number = int(input('Введите число: '))
#
# factorial = 1
#
# while number >= 1:
#     factorial *= number
#     number -= 1
#
# print(factorial)

##############################################################################################

# summa = 0
# while True:
#     number = int(input('Введите число или 0 чтобы закончить цикл: '))
#     if number == 0:
#         break
#     summa += number
# print(summa)

##############################################################################################

# debt = 1000
# trice = 3
#
# while debt > 0:
#     money = int(input(f'Ваш долг состовляет {round(debt, 2)}, сколько вы готовы внести? '))
#     if money <= 0:
#         print('Сумма не может быть меньше либо равна нулю!')
#         continue
#     if trice > 0:
#         debt -= money
#     else:
#         print('Теперь начисляются проценты!')
#         debt *= 1.1
#         debt -= money
#     trice -= 1
# print('Вы закрыли долг!')

##############################################################################################

#import random


# flag = True
#
# print('Программа на проверку знания таблицы умножения.')
#
# level_hard = int(input('Выберите уровень сложности: \n 1 - легкий \n 2 - сложный \n '))
# if level_hard == 1:
#     a = 1
#     b = 10
# else:
#     a = 5
#     b = 12

# while flag:
#     if level_hard == 1:
#         num_1 = random.randint(1, 9)
#         num_2 = random.randint(1, 9)
#
#     else:
#         num_1 = random.randint(5, 12)
#         num_2 = random.randint(5, 12)
#
#     result = num_1 * num_2
#     answer = int(input(f'{num_1} * {num_2} = '))
#     # if answer == result:
#     #     print('Ответ правильный!')
#     while answer != result:
#         print('Ответ неверный, хотите попробывать еще раз? ')
#         answer = int(input(f'{num_1} * {num_2} = '))
#     if answer == result:
#         print('Ответ правильный!')
#     else:
#         print('Ответ неправильный!')
#
#     choice = input('Продолжаем? Да/Нет -> ')
#     if choice == 'Нет':
#         flag = False

##############################################################################################

# import random
#
#
# guess_number = random.randint(1, 500)
# trice = 10
# guessed = False
#
# while not guessed:
#     if trice == 0:
#         print('У вас закончилось число попыток!')
#         break
#     else:
#         trice -= 1
#     number = int(input('Угадайте число от 1 до 500: '))
#     if number == guess_number:
#         print('Вы угадали!')
#         guessed = True
#     elif number > guess_number:
#         print('Загаданное число меньше!')
#     elif number < guess_number:
#         print('Загаданное число больше!')
#     # trice -= 1 можно расположить в конце

##############################################################################################

# num_1 = int(input('Введите первое число x: '))
# num_2 = int(input('Введите второе число y: '))
# step = 1
#
# while num_2 >= 0:
#     step *= num_1
#     num_2 -= 1
#
# print(step)

##############################################################################################

# result = 0
#
# for i in range(100, 1000):
#
#     a = i // 100
#     b = (i % 100) // 10
#     c = i % 10
#
#     if a == b or a == c or b == c:
#         result += 1
#
# print(result)

##############################################################################################

# result = 0
#
# for i in range(100, 10000):
#     a = i // 1000
#     b = i % 1000 // 100
#     c = i % 100 // 10
#     d = i % 10
#
#     if a != b or a != c or a != d or b != c or b != d or c != d:
#         result += 1
#
# print(result)
