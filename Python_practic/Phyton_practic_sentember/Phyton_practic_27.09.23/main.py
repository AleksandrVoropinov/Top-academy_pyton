# Кортежи

# tuple_1 = (['Ivan'], 15)
# tuple_2 = tuple_1 + ('Petr', 15)
# print(tuple_1[0])
# print(tuple_2 * 2)
# print(tuple_1 + ('Petr', 15))
# tuple_2[0][0] = 'Maria'
# print(tuple_2)  # Метод .opp и .append несработают
# print(tuple_2.conunt(15))
# print(tuple_2.index(15))

#############################################################

# import sys
#
# tuple_1 = ('Ivan', 25)  # O(n)
# list_1 = ['Ivan', 25]  # O(n)
# dict_1 = {'Ivan': 25}  # O(1)
#
# print(sys.getsizeof(tuple_1))
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(dict_1))

#############################################################

# dict_1 = {('Ivan', 'Ivanov'): 25}
# print(dict_1[('Ivan', 'Ivanov')])

# list_1 = ['Ivan', 'Ivanov']
# print(tuple(list_1))
# list_1 = ('Ivan', 'Ivanov')
# print(list(list_1))

# a = 10, 20  # Сделает кортеж
# print(a)

#############################################################

# zip - функция берет по индексам и не показывает ошибку

# list_1 = ['Moscow', 'Berlin']
# list_2 = [1000000, 2000000]
#
# print(dict(zip(list_1, list_2)))
# print(tuple(zip(list_1, list_2)))
# print(list(zip(list_1, list_2)))

#############################################################

# import re
#
# dictionary = {}
#
#
# def add_competition() -> None:
#     competition = input('Название соревнования: ')
#     date = input('Дата проведения yyyy/mm/dd HH:MM: ')
#     if re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}', date) and (competition, date) not in dictionary.keys():
#         dictionary.update({(competition, date): []})
#         print('Соревнование добавлено!')
#         return
#     print('Невалидный ввод!')
#
#
# def add_members() -> None:
#     competition = input('Название соревнования: ')
#     date = input('Дата проведения yyyy/mm/dd HH:MM: ')
#     if re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}', date) and (competition, date) in dictionary.keys():
#         choice = input('Добавить участника или убрать? add/del: ')
#         members = dictionary[(competition, date)]
#         if choice == 'add':
#             input_members = input('Введите участников (через пробел ,): ').split(', ')
#             dictionary[(competition, date)] = members + input_members
#             print('Участники добавлены!')
#         elif choice == 'del':
#             del_members = input('Введите участников (через пробел ,): ').split(', ')
#             for i_members in del_members:
#                 members.remove(i_members)
#             dictionary[(competition, date)] = members
#             print('Участники удалены!')
#             return
#         else:
#             print('Ошибка ввода!')
#
#
# def info() -> None:
#     competition = input('Название соревнования: ')
#     date = input('Дата проведения yyyy/mm/dd HH:MM: ')
#     if re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}', date) and (competition, date) in dictionary.keys():
#         print(f'{competition} {date}')
#         for index, i_member in enumerate(dictionary[(competition, date)]):
#             print(f'{index + 1} {i_member}')
#         return
#     print('Ошибка ввода!')
#
#
# def main() -> None:
#     while True:
#         choice = input('1-Добавить соревнование\n'
#                        '2-Ввести участников соревнования\n'
#                        '3-Вывод данных по конкретному соревнованию: ')
#         if choice == '1':
#             add_competition()
#         elif choice == '2':
#             add_members()
#         elif choice == '3':
#             info()
#
#
# main()

#############################################################

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# # string = 'привет'
# # coded = 'сткджф'
#
#
# def caesar_code(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in text.lower()]
#     return ''.join(decrypted_list)
#
#
# text = input('Введите текст: ')
# shift = int(input('Введите сдвиг: '))
# print(caesar_code(text, shift))

#############################################################

# site = {
#     'body': {
#         'div': {
#             'ul': {
#                 'li_1': {},
#                 'li_2': {
#                     'a': {
#                         'href': 'какая-то ссылка'
#                     }
#                 }
#             }
#         }
#     }
# }
#
#
# def get(key, dictionary, level=1):
#     if key in dictionary.keys():
#         print(dictionary[key])
#         print(level)
#         # return
#     for value in dictionary.keys():
#         if isinstance(dictionary[value], dict):
#             get(key, dictionary[value], level + 1)
#
#
# print(get('href', site))

#############################################################

fruit_tuple = ['banana', 'apple', 'bananamango', 'mango', 'starwberry-banana']
fruit = input('Введите название фрукта: ')
count = 0

for i_fruit in fruit_tuple:
    if fruit in i_fruit:
        fruit += 1
print(count)
print(fruit_tuple.count(fruit))
