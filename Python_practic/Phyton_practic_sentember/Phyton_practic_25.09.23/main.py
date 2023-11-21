# import re
# # data = {}
# data = {'2023': 100, '2023/01': 100, '2022': 10, '2022/02': 10}
#
#
# def add_money() -> None:
#     date = input('(yyyy/mm)->')
#     if re.match(r'\d{4}/\d{2}', date):
#         money = float(input(f'Ваша прибыль за {date}: '))
#         year, month = date.split('/')
#         data.setdefault(year, 0)
#         data.setdefault(date, 0)
#         data[date] += money
#         data[year] += money
#     else:
#         print('Формат даты неверный!')
#
#
# def get_month_cost() -> None:
#     date = input('yyyy/mm -> ')
#     if re.match(r'\d{4}/\d{2}', date):
#         if date in data.keys():
#             print(f'Ваша прибыль за {date} составила: {data[date]}')
#         else:
#             print('Такого месяца нет!')
#     else:
#         print('Неверный формат даты!')
#
#
# def get_year_cost() -> None:
#     year = input('Введите год: ')
#     if re.match(r'\d{4}', year) and year in data.keys():
#         print(f'Ваша прибыль за {year} равна {data[year]}')
#     else:
#         print('Такого года нет!')
#
#
# def main() -> None:
#     while True:
#         choice = input('1-Внести прибыль за период в формате yyyy/mm:\n'
#                        '2-Получить прибыль за конкретный месяц (yyyy/mm):\n'
#                        '3-Получить прибыль за конкрентный год (yyyy) -> ')
#         if choice == '1':
#             add_money()
#         elif choice == '2':
#             get_month_cost()
#         elif choice == '3':
#             get_year_cost()
#         else:
#             print('Такой команды нет!')
#
#
# main()

#####################################################################

# l = ['Введите имя и фамилию нового контакта (через пробел): ', 'Введите номер телефона: ']
# data = {}
#
# while True:
#     print('Выберите номер действия: ')
#     print('1. Добавить контакт')
#     print('2. Найти человека')
#     a = input('-> ')
#
#     if a == '1':
#         ss = str()
#         for i in l:
#             s = input(i)
#             ss += ' ' + s
#         ss = ss.split()
#         key = (ss[0], ss[1])
#         if key in data:
#             print('Такой человек уже есть в контактах.')
#         else:
#             data[key] = ss[2]
#             print('Текущий словарь контактов:', data)
#
#     if a == '2':
#         a = input('-> ')
#         for k in data.keys():
#             if a == k[1]:
#                 print(k[0], k[1], data[k])


data = {}


def surname() -> None:
    name = input('Введите имя и фамилию контакта (через пробел): ').split()
    if name in data:
        phone = input('Введите номер телефона: ')
        data[name] = phone
        print(f'\nТекущий словарь контактов')
    else:
        print('Такой человек уже есть в контактах!')


def search_surname() -> None:
    search = input('Введите фамилию искомого контакта -> ').title()
    for item, number in data.items():
        if search == item[1]:
            print(item[0], item[1], number)
            break
        else:
            print('Такого человека в контактах нет!')


def main() -> None:
    while True:
        choice = input('Выберите действие:\n'
                       '1-Добавить контакт\n'
                       '2-Найти человека\n')
        if choice == '1':
            surname()
        elif choice == '2':
            search_surname()
        else:
            print('Такой команды нет!')


main()

#####################################################################

# def info_man(name, age):
#     print(name, age)
#
#
# data = {'name': 'Ivan', 'age': 22}
#
# info_man(**data)

# def info_man_2(age, name):
#     print(name, age)
#
#
# list_info = ['Ivan', 18, 10]
#
# info_man_2(*list_info)

# def info_man(name, age):
#     print(name, age)
#
#
# data = {'name': 'Ivan', 'age': 22}
#
# info_man(**data)

# names_list = ['Ivan', 'Anna', 'Maria', 'Sasha']
#
# names_dict = {key: [] for key in names_list}
# names_dist = {i + 1: names_list[i] for i in range(len(names_list))}
# names_dist = {i: [j for j in i] for i in names_list}
# print(names_dict)
