#  Декораторы

# from typing import Callable
# import time
#
#
# def timer(func: Callable, *args, **kwargs):
#     print('Запускается таймер')
#     start = time.time()
#     res = func(*args, **kwargs)
#     print(f'Функция {func.__name__} выполнялась {time.time() - start}')
#     return res
#
#
# def squares_sum(num):
#     nums = [i ** 2 for i in range(num)]
#     return nums
#
#
# def cubes_sum(num):
#     nums = [i ** 3 for i in range(num)]
#     return nums
#
#
# res = timer(cubes_sum, 1000000)
# res_2 = timer(squares_sum, 1000000)

###################################################################

# from typing import Callable
# import time
# import functools
#
#
# def timer(func: Callable) -> Callable:
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):  # ф-ция обертка
#         start = time.time()  # код для дополнения функционала
#         func(*args, **kwargs)  # вызов ф-ции которую передали
#         print(f'Функция {func.__name__} {func.__doc__} выполнилась за {time.time() - start}')
# код для доп. функционала
#     return wrapper  # возвращение ф-ции обертки
#
#
# @timer
# def squares_sum(num):
#     """
#     Квадраты чисел
#     :param num:
#     :return:
#     """
#     nums = [i ** 2 for i in range(num)]
#
#     return nums
#
#
# @timer
# def cubes_sum():
#     """
#     Кубы чисел
#     :return:
#     """
#     nums = [i ** 3 for i in range(1000000)]
#     return nums
#
#
# squares_sum(1000000)
# cubes_sum()

###################################################################

# def get_or_post(method):
#     def wrapper_func(func):
#         def wrapper():
#             res = func()
#             print(f'Запрос с методом {method} на ресурс {res} выполнен')
#         return wrapper
#     return wrapper_func
#
#
# @get_or_post('POST')
# def request():
#     url = 'http://test.com'
#     params = 'ru'
#     request_body = {}
#     return url, params, request_body
#
#
# request()

###################################################################

# from typing import Callable
#
#
# def beauty_output(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         for i in result:
#             print(f'|{i}|')
#     return wrapper
#
#
# @beauty_output
# def names_output(names):
#     return names
#
#
# names_output(['Nikita', 'Ivan', 'Maria'])

###################################################################

# from typing import Callable
# import datetime
# import time
# import functools
#
#
# def logging(func: Callable) -> Callable:
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#             print(f'{func.__name__} {func.__doc__}')
#         except BaseException as error:
#             with open('function_errors.log', 'a') as file:
#                 file.write(f'{func.__name__} | {datetime.datetime.now()} | {error.__doc__}\n')
#
#     return wrapper
#
#
# def timer(func: Callable) -> Callable:
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):  # ф-ция обертка
#         start = time.time()  # код для дополнения функционала
#         func(*args, **kwargs)  # вызов ф-ции которую передали
#         print(f'Функция {func.__name__} {func.__doc__} выполнилась за {time.time() - start}')
#         # код для доп. функционала
#     return wrapper  # возвращение ф-ции обертки
#
#
# @timer
# @logging
# def concatenate(a, b):
#     return a + b
#
#
# @timer
# @logging
# def division(a, b):
#     return a / b
#
#
# concatenate(1, 1)
# division(5, 0)

###################################################################

# Написать декоратор который вызывает фун-ию два раза

# from typing import Callable
#
#
# def concole_func(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         for i in range(1):
#             result = func(*args, **kwargs)
#             result_2 = func(*args, **kwargs)
#             print(f'{result}')
#             print(f'{result_2}')
#     return wrapper
#
#
# @concole_func
# def print_func(names):
#     return names
#
#
# print_func(['Nikita', 'Ivan', 'Maria'])

###################################################################

# Замедление кода

# import time
#
#
# def fun_sleep(timeout, retry=3):
#     def wrapper_fun(func):
#         def wrapper(*args, **kwargs):
#             retries = 0
#             while retries <= retry:
#                 try:
#                     value = func(*args, **kwargs)
#                     if value is None:
#                         return
#                 except:
#                     print(f'Сон на {timeout} секунд')
#                     time.sleep(timeout)
#                     retries += 1
#
#         return wrapper
#     return wrapper_fun
#
#
# @fun_sleep(3)
# def request(a, b):
#     return a + b
#
#
# request(21, 10)

###################################################################

# Декоратор проверяющий доступ к функции

# from typing import Callable
#
#
# def password(func: Callable) -> Callable:
#     def wrapper(*args, ** kwargs):
#
#
#
# @password
# def concatenate(a, b):
#     return a + b


# concatenate(5, 10)
