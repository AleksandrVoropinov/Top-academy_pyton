# Задание 1

# number = int(input('Введите число: '))
# summ = 0
# while number != 0:
#     summ += number
#     number = int(input('Введите число: '))
# print(summ)

# Задание 2

# password = int(input('Введите пароль: '))
# while password != 453:
#     print('Пароль неверный!')
#     password = int(input('Попробуйте повторно ввести пароль: '))
# print('Вы ввели верный пароль!')

# Задание 3

# money = int(input('Укажите размер зарплаты: '))
# while money < 500000:
#     saving = int(input('Сколько хотели бы отложить? '))
#     money += saving
# print('Вы отложили ', money, 'рублей.')

# Задание 4

# number = input('Введите определеный код состоящий из цифр: ')
# summ = 0
# for digit in number[::-1]:
#     if digit == '5':
#         print('Обнаружен разрыв!')
#         break
#     summ += int(digit)
# print('Сумма цифр: ', summ)

# Задание 5

# import time
#
# count = 10
# while count != 0:
#     time.sleep(1)
#     print(count)
#     count -= 1
# print('Время вышло!')

# Задание 6

# hour_count = int(input("Который час? "))
# if not 0 <= hour_count <= 24:
#     print("Неверное число")
# else:
#     if not hour_count:
#         hour_count += 24
#     for _ in range(hour_count):
#         print("Ку-ку!")

# Задание 7

# second_up = int(input('Введите кол-во секунд: '))
# for second in range(second_up, 1, -2):
#     print(second // 2 * 2)
#
# print('1')
# print('Я иду искать!!!')

# Задание 8

# text = input('Введите текст: ')
# first_sym = 'Ы'
# second_sym = 'ы'
# firstSymCount = 0
# secondSymCount = 0
#
# for symbol in text:
#     if symbol == first_sym:
#         firstSymCount += 1
#     if symbol == second_sym:
#         secondSymCount += 1
#
# print('Больших букв Ы: ', firstSymCount)
# print('Маленьких букв ы: ', secondSymCount)

# Задание 9

# text = input('Введите текст: ')
# text == text.upper()
# print(f'{text.title()}')

# Задание 10

# Задание 11

# s = input()
# a = s[:s.find('h')]
# b = s[s.find('h'):s.rfind('h') + 1]
# c = s[s.rfind('h') + 1:]
# s = a + b[::-1] + c
# print(s)
