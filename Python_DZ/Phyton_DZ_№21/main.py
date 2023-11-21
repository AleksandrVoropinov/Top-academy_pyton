# Декораторы
# 1. Написать декоратор который с вероятностью 0,1 будет выбрасывать случайное исключение
# 2. Декоратор проверяющий тип данных, который вернула ф-я (число или строка)

import random


def random_exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            if random.random() < 0.1:
                raise Exception('Произошло случайное исключение: ')
            else:
                return func(*args, **kwargs)
        except Exception as e:
            print('Произошло исключение: ', str(e))
    return wrapper


@random_exception_decorator
def some_function():
    print('Это какая-то функция')


some_function()


def type_check_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int) or isinstance(result, float):
            print('Функция вернула число: ')
        elif isinstance(result, str):
            print('Функция вернула строку: ')
        else:
            print('Функция вернула другой тип: ')
        return result
    return wrapper


@type_check_decorator
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 10)
print(result)


@type_check_decorator
def get_name():
    return 'Alexsandr'


result = get_name()
print(result)
