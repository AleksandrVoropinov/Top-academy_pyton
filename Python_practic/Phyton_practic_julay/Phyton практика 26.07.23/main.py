# age = int(input('Введите ваш возраст: '))
# if 18 <= age <= 70:
#     print('Вы можете зарегистрироваться!')
# else:
#     print('Вам нельзя регистрироваться!')
#####################################################

# weekday = int(input('Введите номер дня недели: '))
# if weekday == 1:
#     print('Понедельник')
# if weekday == 2:
#     print('Вторник')
# if weekday == 3:
#     print('Среда')
# if weekday == 4:
#     print('Четверг')
# if weekday == 5:
#     print('Пятница')
# if weekday == 6:
#     print('Суббота')
# if weekday == 7:
#     print('Воскресенье')
# else:
#     print('Такого дня недели несуществует!')
#####################################################

# weekday = int(input('Введите номер дня недели: '))
# if weekday == 1:
#     print('Понедельник')
# elif weekday == 2:
#     print('Вторник')
# elif weekday == 3:
#     print('Среда')
# elif weekday == 4:
#     print('Четверг')
# elif weekday == 5:
#     print('Пятница')
# elif weekday == 6:
#     print('Суббота')
# elif weekday == 7:
#     print('Воскресенье')
# else:
#     print('Такого дня недели несуществует!')
#####################################################

# email = 'world@mail.ru'
# password = '1234dodo'
#
# email_input = input('ВВедите свой email: ')
# password_input = input('Введите пароль: ')
# authorization = False
#
# if email_input == email:
#     if password_input == password:
#         authorization = True
#         # print('Вы авторизовались')
#     else:
#         print('Пароль неверный!')
# else:
#     print('email указан неверно!')
#
# match(authorization):
#     case True:
#         print('Пользователь успешно авторизовался!')
#     case False:
#         print('Пользователь не авторизовался!')
#     case _:
#         print('Else')
#####################################################

# number = int(input('Введите число: '))
#
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')
#
# if number % 2 != 0:
#     print('Нечетное')
# else:
#     print('Четное')
#
# if number % 6 == 0:
#     print('Число кратно 6')
# else:
#     print('Число некратно 6')
#####################################################

# from math import sqrt
# print('a*x^2 + b*x + c')
# a = float(input('Введите коэффициент a: '))
# b = float(input('Введите коэффициент b: '))
# c = float(input('Введите коэффициент c: '))
# # ** возведение в степень
# D = b**2 - 4 * a * c
# if D < 0:
#     print('Корней нет')
# elif D == 0:
#     x = -b / (2 * a)
#     print(f'x = {x}')
# else:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#     print(f'x1={round(x1, 2)} x2={round(x2, 2)}')
#####################################################

# number_1 = int(input('1-ое число: '))
# number_2 = int(input('2-ое число: '))
#
# try:
#     print(number_1 / number_2)
# # except BaseException:
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# else:
#     print('Программа выполнилась без ошибок!')
# finally:
#     print('Запустился блок finally')

# if number_2 == 0:
#     print('На 0 делить нельзя!')
# else:
#     print(number_1 / number_2)
#####################################################

# try:
#     raise ValueError('Вызвана ошибка специально')
# except FileNotFoundError:
#     print('Обработана ошибка')


# try:
#     raise ValueError
# except ValueError:
#     print('Обработчик ошибки ValueError 1')
# except BaseException:
#     print('Обработчик ошибки ValueError 2')
#
# try:
#     raise ValueError
# except KeyError:
#     print('Обработчик ошибки ValueError 1')
# except ValueError:
#     print('Обработчик ошибки ValueError 2')
#####################################################

# try:
#     year = int(input('Введите год: '))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('Високосный год')
#     else:
#         print('Не високосный год')
#     raise TypeError
# except (ValueError, TypeError):
#     print('Год должен быть числом!')
#####################################################

# number = int(input('Введите число: '))
#
# if number % 7 == 0:
#     print('Поздравляем число кратно 7')
# else:
#     print('Число не кратно 7!')
#####################################################

# number_1 = int(input('Введите 1-ое число: '))
# number_2 = int(input('Введите 2-ое число: '))
#
# if number_1 > number_2:
#     print(number_1)
# else:
#     print(number_2)
#####################################################

# number_1 = int(input('Введите 1-ое число: '))
# number_2 = int(input('Введите 2-ое число: '))
#
# if number_1 < number_2:
#     print(number_1)
# else:
#     print(number_2)
#####################################################
try:
    num1 = int(input("введите число 1\n"))
    num2 = int(input("введите число 2\n"))
    x = [num1, num2]
    c = int(input("выберите действие: 1 - найти максимум, 2 - найти минимум, 3 - найти среднее \n"))

    if c == 1:
        print('Максимум из 2х: ', max(x))
    elif c == 2:
        print('Минимум из 2х: ', min(x))
    elif c == 3:
        print('Среднее из 2х: ', sum(x) / len(x))
    else:
        print("введите число от 1 до 3")
except ValueError:
    print('Ошибка!')
#####################################################


