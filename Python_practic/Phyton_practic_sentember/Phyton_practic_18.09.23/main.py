# def function_1(a, b, *args):  #  Добавляем кортеж неименованых аргументов имеющий последовательность - *args
#     print(a, b, args)
#
# function_1(1, 2, 4, 5, 6, 8)

#################################################################

# def summa(*args):
#     container = 0
#     for i_arg in args:
#         container += i_arg
#     return container
#     try:
#        return sum(args)
#     except TypeError:
#         return 'Неверный формат данных!'
#
# print(summa(1, 2, 3, '4', 5, 6, 7, 8))

#################################################################

# <input name='surname'>
# <input name='email'>

# def get_form(**kwargs):  # Аргументы по ключу **kwargs - именнованый
#     print(kwargs['name'])  # В квадратных скобочках вводим нужный нам ключ
#     print(kwargs['email'])
#
# get_form(name='Ivanov', email='ivanov@mail.ru')  # Получаем словарь который имеет ключ и значение

#################################################################

# def get(request, *args, **kwargs):
#     print(f'Сделан запрос на {request}')
#     print(f'Параметры запроса {kwargs["cache_control"]}')
#     print(f'Относительный путь: {args[0]}')
#
#
# get('http://test.ru', '/page_1', cache_control='no-cache', content_type='text/html')

#################################################################

# Написать ф-ию принимающую номер группы, степень, год выпуска, и студентов
# Вывести данные:
# номер группы, степень, год выпуска,
# 1. Студент
# 2. Студент

# def get_info_group(group_num, step, years, *args):
#     count = 1
#     print(f'Номер группы: {group_num}')
#     print(f'Степень: {step}')
#     print(f'Год выпуска: {years}')
#     for i in args:
#         print(count, i)
#         count += 1
#     for i in range(len(args)):
#         print(f'{i + 1}, {args[i]}')
#
# get_info_group('ФГБУ-23', 'Бакалавр', 2024, 'Иванов', 'Петров', 'Куренков')

#################################################################

# <input name="email" name='email' required>
# <input name="tel" name='phone' required>
# <input name="type" name='name'>
# <input name="text" name='surname'>

# def try_to_get_value(value, data):
#     try:
#         print(data[value])
#     except KeyError:
#         return
#
#
# def try_to_get_value(**kwargs):
#     try:
#         print(f'Email: {kwargs["email"]}')
#         print(f'Tel: {kwargs["phone"]}')
#     except KeyError:
#         print('Email и телефон обязательны к заполнению!')
#         return
#     try_to_get_value('name', kwargs)
#     try_to_get_value('eamil', kwargs)
#
# try_to_get_value(email='alex@mail.ru', phone='+79999999999', name='Alex', surname='Voropinov')


# def registration(**kwargs):
#     try:
#         print(f'Email: {kwargs["email"]}')
#         print(f'Tel: {kwargs["phone"]}')
#     except KeyError:
#         print('Email и телефон обязательны к заполнению!')
#         return
#     try:
#         print(f'Name: {kwargs["name"]}')
#     except KeyError:
#         return
#     try:
#         print(f'Surname: {kwargs["surname"]}')
#     except KeyError:
#         return
#
#
# registration(email='alex@mail.ru', phone='+79999999999', name='Alex', surname='Voropinov')

# def registration(**kwargs):
#     try:
#         if kwargs['email'] != 0 and kwargs['tel'] != 0:
#             print(f'Email: {kwargs["email"]}')
#             print(f'Tel: {kwargs["phone"]}')
#             if 'name' in kwargs:
#                 print(f'Name: {kwargs["name"]}')
#             else:
#                 pass
#             if 'surname' not in kwargs:
#                 pass
#             else:
#                 print(f'Surname: {kwargs["surname"]}')
#     except KeyError:
#         print('Выведены не все данные!')
#
#
# registration(email='alex@mail.ru', phone='+79999999999', name='Alex', surname='Voropinov')

#################################################################

# Анонимные функции

# square = lambda x, y: x ** 2  # lambda - вызов анонимной функции
#
# print(square(5, 2))

# nums_list = [1, 2, 3, 4, 5, 6, 7, 8]
# square_nums_list = [i ** 2 for i in nums_list]
# print(square_nums_list)

# nums_list = [1, 2, 3, 4, 5, 6, 7, 8]
# square_nums_list = list(map(lambda x: x ** 2, nums_list))
# print(square_nums_list)

# for i in square_nums_list:
#     print(i)

# nums_list = [1, 2, 3, 4, 5, 6, 7, 8]
# square_nums_list = map(lambda x: x ** 2, nums_list)
# print(next(square_nums_list))
# print(next(square_nums_list))
# print(next(square_nums_list))
# print(next(square_nums_list))

#################################################################
# import time
#
# class Iterator:
#
#     def __init__(self, n, end):
#         self._n = n
#         self._end = end
#
#     def __iter__(self):
#         print('__iter__')
#         return self
#
#     def __next__(self):
#         if self._n >= self._end:
#             raise StopIteration
#         print('__next__')
#         time.sleep(1)
#         self._n += 1
#         print(self._n)
#
#
# for i in Iterator(0, 8):
#     pass

#################################################################

# nums_list = [1, 2, 3, 4, 5, 6, 7, 8]
# square_nums_list = [i ** 2 for i in nums_list if i > 4]
# print(square_nums_list)
#
# filtered_list = list(filter(lambda x: x > 4, nums_list))
# print(filtered_list)

# names_list = ['Ivan', 'Petya', 'Irina']
#
# filtered_list = list(filter(lambda x: x[0].lower() == 'i' and len(x) <= 4, names_list))
# print(filtered_list)

#################################################################

# Нужно отфильтровать список map, filter () остаться долждны только трех значные цифры

# nums = [123, 14575, 35, 8, 147, 489]
#
# filtered_list = list(filter(lambda x: len(str(x)) == 3, nums))
# print(filtered_list)
# filtered_list_1 = list(map(int, (filter(lambda x: len(x) == 3, map(str, nums)))))
# print(filtered_list_1)
# filtered_list_2 = list(filter(lambda x: 99 < x < 1000, nums))
# print(filtered_list_2)

#################################################################

# sorted(iterible, key=)

students = [
    ['Student 1', 4.8],
    ['Student 2', 4.7],
    ['Student 9', 4.9],
    ['Student 4', 4.8],
    ['Student 10', 4.1],
    ['Student 6', 3.8],
    ['Student 7', 4.4]
]

students_filtered = sorted(students, key=lambda x: x[1])
print(students_filtered)
students_filtered_1 = sorted(students, key=lambda x: int(x[0].split()[1]))
print(students_filtered_1)
