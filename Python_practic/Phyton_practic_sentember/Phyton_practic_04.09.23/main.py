# import sys

# my_list_1 = []  # пустой список
# my_list_2 = list()  # пустой список

# print(my_list_1)
# print(my_list_2)
# print(sys.getsizeof(my_list_1))
# print(sys.getsizeof(my_list_2))

###############################################################################

# import sys
#
# my_list_1 = ['Moscow', 'Samara', 'Ekaterinburg', 'Novosibirsk', ]
# my_list_2 = list(('Moscow', 'Samara', 'Ekaterinburg', 'Novosibirsk'))
#
# print(my_list_1)
# print(my_list_2)
# print(sys.getsizeof(my_list_1))
# print(sys.getsizeof(my_list_2))

###############################################################################
# import sys
#
# my_list_1 = ['Moscow', 'Samara', 'Ekaterinburg', 'Novosibirsk', ]
#
# print(my_list_1[0])
# print(my_list_1[1:])
# print(my_list_1[::2])
# print(my_list_1[::-1])

###############################################################################

# import sys

# my_list_1 = ['Moscow', 'Samara', 'Novosibirsk', 'Ekaterinburg', 'Ekaterinburg', ]

# my_list_1.append('Vladivostok')  # Добавляет в конец списка
# my_list_1.append('Vladivostok')
# my_list_1.remove('Vladivostok')  # Удалет первое нахождение в списке
# del_city = my_list_1.pop(0)  # Удаляет последний элемент и по индексу
# my_list_1.insert(0, 'Chelyabinsk')  # Добавляет в список элемент по указаному индексу

# print(my_list_1.index('Ekaterinburg'))  # Возвращает индекс элемента
# print(my_list_1.count('Ekaterinburg'))  # Возвращает кол-во конкретного элемен
# print(my_list_1, del_city)
# my_list_1[3] = 'Vladivostok'  # Присваивание индекса элементу
# my_list_1.reverse()  # [::-1]
# print(my_list_1)

###############################################################################

# my_list_1 = ['Moscow', 'Samara', 'Novosibirsk', 'Ekaterinburg', ]

# for i_city in my_list_1:
#     print(f'Город:{i_city}')

# for index in range(len(my_list_1)):
#     print(f'{index + 1} Город: {my_list_1[index]}')

###############################################################################

# Задание 1

# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
# my_list = []
#
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         my_list.append(i)
#
# print(my_list)

###############################################################################

# basket_1 = ['Bayern', 'Man Utd', 'Juventus', 'Barcelona']
# basket_2 = ['Real Madrid', 'Man City', 'Milan', 'Porto']
#
# for index in range(len(basket_1)):
#     if index % 2 != 0:
#         print(f'{basket_1[index]} - {basket_2[index - 1]}')
#         print(f'{basket_1[index - 1]} - {basket_2[index]}')

###############################################################################

# numbers = [15, 9, 8, 17, 79, 5, 1, 4]
# numbers.sort(reverse=True)  # Сортировка списка
# numbers_sorted = sorted(numbers)  # Копия списка
# print(id(numbers_sorted), id(numbers))

# letters = ['a', 'z', 't', 'b', 'r']
# print(sorted(letters))

###############################################################################

# string = 'hello phyton java ruby'
#
# print(string.split('*'))

# numbers = input('Введите числа через пробел: ').split()

# for i_num in numbers:
#     numbers[numbers.index(i_num)] = int(i_num)  # перевели из строки в числа

# for index, value in enumerate(numbers):  # нужно два значения для enumerate
#     numbers[index] = int(value)

# numbers_int = list(map(int, input('Введите числа через пробел: ').split()))
# print(numbers_int)

###############################################################################

# films = ['Побег из Шоушенка', 'Зеленая миля', 'Поймай если сможешь', 'Волк с Уолл-стрит', ]
# liked_films = []
#
# while True:
#     choice = input('1-Посмотреть список избранных фильмов\n'
#                    '2-Добавить фильм в избранное\n'
#                    '3-Удалить фильм из избранного - >')
#     if choice == '1':
#         print(f'Ваш список избранного кино: {liked_films}', *liked_films)  # Убирает квадратные скобки в консоли
#     elif choice == '2':
#         film = input('Введите название фильма: ')
#         if film in films:
#             if film not in liked_films:
#                 liked_films.append(film)
#                 print('Ваш фильм добавлен!')
#             else:
#                 print('Такой фильм у вас уже есть!')
#
#         else:
#             print('Такого фильма в нашей библиотек нет, добавим его позже...')
#     elif choice == '3':
#         film = input('Введите название фильма: ')
#         if film in liked_films:
#             liked_films.remove(film)
#         else:
#             print('Такого фильма у нас нет!')
#     else:
#         print('До новых встреч!')
#         break

###############################################################################

# numbers = [1, 25, 78, 7, 8, -9]
#
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))

###############################################################################

# Задание 2

# numbers = input('Введите числа через пробел: ').split()
# numbers_search = input('Введите число которое хотите узнать кол-во повторений: ')
# numbers_count = 0
#
# for i_num in numbers:
#     if fine_numbers == i_num:
#         numbers_count += 1
#
#     print(numbers_count)

# Задание 3

# list_num = list(map(int, input(' Введите элементы списка: ').split()))
#
# print(f'Сумма всех элементов равна: {sum(list_num)}')
# print(f'Среднеарифметическое равно: {sum(list_num)/len(list_num)}')



