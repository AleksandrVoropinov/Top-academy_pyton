#  Теория множеств

# a = set()
# a.add('apple')
# a.add('banana')
# print(a)
# print('banana' in a)
# a.remove('apple')  #  Удаляет выбраный вами элемент
# a.discard('apple')  # Тоже удаляет объект но без вызова исключения
# a.pop()  # Удаляет рандомный элемент
# b = {'orange', 'watermelon', 'apple'}
# print(b)
# print(a)
# print(a.intersection(b))  # Пересечение
# print(a.difference(b))  # Разница
# c = a.union(b)
# print(c)
# print(a.union(b))  # Объединение
# a.clear()  # Очистить множества - удаляет все элементы
# print(a)
# a.update(b)  # Обновляет множество - изменяет текущее
# print(a)
# for item in a:
#     print(item)
# print(*a)  # распаковка множеств также работает
# print('*'.join(a))  # Можно брать элементы и добавлять в любую строку

#########################################################################

# set_1 = {'Name', 18, 'key', 'value'}  # Могут хранится только простые типы данных (числа, строки)
# print(set_1)
# import sys

# list_1 = ['apple', 'orange']
# set_1 = {'apple', 'orange'}

# print(sys.getsizeof(list_1))
# print(sys.getsizeof(set_1))
# print(set_1.update(list_1))

#########################################################################

# В файле записан какой-то текст нужно посчитать
# кол-во всех уникальных символов

# data = {}
#
# with open('file.txt', 'r', encoding='utf - 8') as file:
#     text = file.read()
#     char = set(text)
#     file.seek(0)
#     for char in text:
#         if char.isalpha():
#             data[char] = text.count(char)
#     sorted_dict = sorted(data, key=lambda x: data[x], reverse=True)
#     print(data['о'])
# print(sorted_dict)

#########################################################################

#  Нужно проверить может ли строка стать полиндромом

# text = 'aabbbaaab'
#
#
# def check(text):
#     data = {}
#     for i in text:
#         data.setdefault(i, 0)
#         data[i] += 1
#     count = 0
#     for j in data.values():
#         if j % 2 != 0:
#             count += 1
#     if count <= 1:
#         print('Может')
#     else:
#         print('Неможет')
#
#
# check(text)

#########################################################################

# Генераторы

# import sys

# list_1 = [i for i in range(100)]  # Хранится множество значений
# generation = (i for i in range(100))  # Хранится только одно значение - генераторное выражение т.е только текущие
# for i in generation:
#     print(i)
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(generation))


# def custom_range(start, end):
#     for i in range(start, end):
#         yield i
#
#
# for i in custom_range(10, 20):
#     print(i)

# class Generator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.cur = start
#
#     def __iter__(self):
#         print('__iter__')
#         return self
#
#     def __next__(self):
#         if self.cur == self.end:
#             raise StopIteration
#         self.cur += 1
#         return self.cur
#
#
# for i in Generator(10, 20):
#     print(i)

#########################################################################

# with open('file_1.txt', 'r') as file:
#     words = (i_word for i_word in file.readlines())  # Генератор можно преобразовать в ту
                                                     # структуру данных которая необходимо
# for i in words:
#     print(i.strip())

# через генераторную фун-цию

# def words():
#     with open('file_1.txt', 'r') as file:
#         for i in file.readlines():
#             yield  i
#
#
# for i in words():
#     print(i.strip())

# Реализовать бесконечный генератор


# def generation():
#     num = 1
#     while num:
#         num += 1
#         yield num
#
#
# for i in generation():
#     print(i)

# Есть список имен, необходимо отфильтровать имена которые содержат букву А,
# через генераторное выражение

# list_1 = ['Анатолий', 'Евгений', 'Василий']
#
# gen = (i for i in list_1 if 'а' not in i)
# print(*gen)
