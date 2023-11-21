# Задание 1
# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).

import json


def add_data(data, country, capital):
    data[country] = capital


def remove_data(data, country):
    del data[country]


def find_data(data, country):
    if country in data:
        return data[country]
    else:
        return "Страна не найдена!"


def edit_data(data, country, capital):
    if country in data:
        data[country] = capital
    else:
        return "Страна не найдена!"


def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


countries = {}

add_data(countries, "Russia", "Moscow")
add_data(countries, "USA", "Washington D.C.")
print(find_data(countries, "Russia"))
print(find_data(countries, "China"))

edit_data(countries, "USA", "New York")
print(find_data(countries, "USA"))

remove_data(countries, "Russia")
print(find_data(countries, "Russia"))

save_data(countries, "countries.json")
loaded_data = load_data("countries.json")
print(loaded_data)

# Задание 2
# Есть некоторый словарь, который хранит названия
# музыкальных групп(исполнителей) и альбомов. Назва-
# ние группы используется в качестве ключа, название
# альбомов в качестве значения. Необходимо реализовать:
# добавление данных, удаление данных, поиск данных,
# редактирование данных, сохранение и загрузку данных
# (используя упаковку и распаковку).

# import json
#
#
# def add_group(albums, group, album):
#     if group in albums:
#         albums[group].append(album)
#     else:
#         albums[group] = [album]
#
#
# def delete_group(albums, group):
#     if group in albums:
#         del albums[group]
#
#
# def search_album(albums, album):
#     result = []
#     for group, albums_list in albums.items():
#         if album in albums_list:
#             result.append(group)
#     return result
#
#
# def edit_album(albums, group, old_album, new_album):
#     if group in albums and old_album in albums[group]:
#         albums[group].remove(old_album)
#         albums[group].append(new_album)
#
#
# def save_data(albums, filename):
#     with open(filename, 'w') as file:
#         json.dump(albums, file)
#
#
# def load_data(filename):
#     with open(filename, 'r') as file:
#         albums = json.load(file)
#     return albums
#
#
# albums = {}
# add_group(albums, 'Metallica', 'Master of Puppets')
# add_group(albums, 'Pink Floyd', 'The Dark Side of the Moon')
# print(albums)
#
# delete_group(albums, 'Metallica')
# print(albums)
#
# add_group(albums, 'Led Zeppelin', 'Led Zeppelin IV')
# print(albums)
#
# edit_album(albums, 'Pink Floyd', 'The Dark Side of the Moon', 'Wish You Were Here')
# print(albums)
#
# save_data(albums, 'albums.json')
# loaded_albums = load_data('albums.json')
# print(loaded_albums)
