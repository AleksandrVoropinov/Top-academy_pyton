# string = 'Hello'
# encode_string = string.encode(encoding='utf8')
# print(encode_string)
# decoded_string = encode_string.decode(encoding='utf8')
# print(decoded_string)

########################################################################

# string = 'abcdefg'
# print(len(string))  # len длина строки
# print(string[0])    # получение символа строки по индекусу
# print(string[-1])
# print(string[len(string) - 1])  # полученние последнего символа строки
# print(string[0:3])
# print(string[:3])
# print(string[3:])   # срез - получение отрезка строки
# print(string[0:5:2])  # срез - получение отрезка строки c шагом
# print(string[-1:-4:-1])  # отрицательный срез - получение отрезка строки c шагом
# print(string[::-1])   # перевернули строку

########################################################################

# example = '0123456789'
# print(example[:3])
# print(example[3:6])
# print(example[-1:-4:-1])
# print(example[::2])
# print(example[::-1])
# print(example[-5:-8:-1])
# print(example[-2:-8:-2])
# print(example[-6:-10:-1])

########################################################################

# text = 'phyton is a programming language '
# print(text.capitalize())  # первый символ строки в верхний регистр
# print(text.title())       # каждый первый символ слова с большой буквы
# print(text.count('p'))    # считает количество последовательностей символов и слов в строке
# print(text.lower())       # переводит всю строку в нижний регистр
# print(text.upper())       # все символы в верхний регистр
# print(text.replace(' ', '-'))  # замена всех пробелов либо букв
# print(text.index('n'))    # узнать индекс любого элемента
# print(text.find('ж'))     # find не выдаст ошибку -1, есть rfind и lfind сторона с которой начнется поиск
# print(text.index('lang'))
# print(len(text))
# print(text.rstrip())      # убирает пробел справа
# print(text.lstrip())      # убирает пробел слева
# print(text.strip())       # с двух сторон убирает пробел
# print(text.swapcase())      # замена больших символов на маленькие а маленькие на большие

########################################################################

# string_2 = 'phyton123 ruby78'
# print(string_2.isalnum())  # проверяет есть ли пробелы в строке
# print(string_2.isalpha())  # проверяет состоит ли строка только из букв
# print(string_2.isdigit())  # проверяет состоит ли строка только из цифр
# print(string_2.islower())  # проверяет на нижний регистр
# print(string_2.isupper())  # проверяет на верхний регистр
# print(string_2.isascii())  # проверка на символ либо последовательность символа из таб. ASCII
# print('124'.isdecimal())   # проверка что число целое
# print('124'.isnumeric())   # проверка что число целое
# print(string_2.isspace())  # проверка если строка состоит только из пробелов

# string_2 = '+79512490388'
# print(string_2.startswith('+7'))  # проверяет начало строки

# string_2 = 'test@mail.ru'
# print(string_2.endswith('com'))  # проверка окончания строки
# print('@' in string_2)
# print(string_2.count('@') == 1)  # проверка на нахождения символа в строке

# string_3 = 'phyton ruby js'
# print(string_3.split('r'))  # разделение строки по конкретному символу

########################################################################

# string_2 = input('Введите текст: ')
#
# print(string_2.count('Ы'))
# print(string_2.count('ы'))

# string_2 = input('Введите текст: ')
#
# print(string_2.title())

########################################################################

# Email содержит (@, .ru, .com)
# Password содержит 8 символов, должен состоять как из букв так из цифр, без спец символов

# registration = False
#
# while not registration:
#     email = input('Введите свой Email: ')
#     password_1 = input('Введите пароль: ')
#     password_2 = input('Подтвердите пароль: ')
#     if ('@' in email) and (email.endswith('.com') or email.endswith('.ru')):
#         if password_1 == password_2:
#             if len(password_1) == 8 and password_1.isalnum()\
#                     and not password_1.isalpha() and password_1.isdigit():
#                 print('Вы зарегистрированы!')
#                 registration = True
#             else:
#                 print('Пароль должен быть длиной 8 символов и т.д.')
#
#         else:
#             print('Пароли должны совподать!')
#     else:
#         print('Eamil должен содержать @ и заканчиваться на .ru и .com')

########################################################################

# Регистрация по номеру телефонна

# registration = False
#
# while not registration:
#     tel = input('Введите телефон в формате +79*********: ')
#     if tel.startswith('+79') and len(tel) == 12 and tel[1:].isdigit():
#         name = input('Введите ваше имя: ')
#         surname = input('Введите вашу фамилию: ')
#         if name.isalpha() and surname.isalpha():
#             print(f'Ваше имя: {name.capitalize()}\n'
#                   f'Ваша фамилия: {surname.capitalize()}\n'
#                   f'Номер телефона: {tel}')
#             registration = True
#         else:
#             print('Невалидные имя и фамилия!')
#     else:
#         print('Невалидный номер телефона!')

########################################################################
# Задание 1
# string_2 = input('Введите текст: ')
# print(f'Развернутый текст: {string_2[::-1]}')

# # Задание 2
# string_2 = input('Введите текст: ')
# alpha = 0
# digit = 0
#  for i in string_2:
#     if i.isalpha():
#         alpha += 1
#     elif i.isdigit():
#         digit += 1
#  print(alpha,digit)

# Задание 3
# string_2 = input('Введите текст: ')
# string_1 = input('Введите искомый символ: ')
# print(f'Столько раз встречается в строке искомый вами символ: {string_2.count(string_1)}')

# Задание 4

# string_2 = input('Введите текст: ')
# string_1 = input('Введите искомое слово: ')
# print(f'Столько раз встречается искомое слово: {string_2.count(string_1)}')

# Задание 5

# string_1 = input('Введите текст: ')
# string_2 = input('Введите слово: ')
# string_3 = input('Введите заменяймое слово: ')
#
# print(f'Ваша строка с замененым словом: {string_1.replace(string_2)}{string_2.find, string_3}')

# Задание 11

# str_1 = 'werwer'
# str_2 = 'Werwer'
#
# if str_2.lower() in str_1.lower():
#     print('ok')
