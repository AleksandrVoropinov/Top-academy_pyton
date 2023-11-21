# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# class Book:
#
#     def __init__(self):
#         self.title = ''
#         self.year_of_issue = 0
#         self.publisher = ''
#         self.genre = ''
#         self.author = ''
#         self.price = 0.0
#
#     def input_data(self):
#         self.title = input('Введите название книги: ')
#         self.year_of_issue = int(input('Введите год выпуска: '))
#         self.publisher = input('Введите издателя: ')
#         self.genre = input('Введите жанр: ')
#         self.author = input('Введите автора: ')
#         self.price = float(input('Введите цену: '))
#
#     def output_data(self):
#         print('Название книги: ', self.title)
#         print('Год выпуска: ', self.year_of_issue)
#         print('Издатель: ', self.publisher)
#         print('Жанр: ', self.genre)
#         print('Автор: ', self.author)
#         print('Цена: ', self.price)
#
#     def __str__(self):
#         return f'{self.title} {self.year_of_issue} {self.publisher} {self.genre} {self.author} {self.price}'
#
#
# book = Book()
# book.input_data()
# book.output_data()

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# class Stadium:
#
#     def __init__(self):
#         self.name_of_the_stadium = ''
#         self.opening_date = ''
#         self.country = ''
#         self.city = ''
#         self.capacity = 0
#
#     def input_data(self):
#         self.name_of_the_stadium = input('Введите название стадиона: ')
#         self.opening_date = input('Введите дату открытия: ')
#         self.country = input('Введите страну: ')
#         self.city = input('Введите город: ')
#         self.capacity = int(input('Введите вместимость: '))
#
#     def output_data(self):
#         print('Название стадиона: ', self.name_of_the_stadium)
#         print('Дата открытия: ', self.opening_date)
#         print('Старна: ', self.country)
#         print('Город: ', self.city)
#         print('Вместимость: ', self.capacity)
#
#     def __str__(self):
#         return f'{self.name_of_the_stadium} {self.opening_date} {self.country} {self.city} {self.capacity}'
#
#
# stadium = Stadium()
# stadium.input_data()
# stadium.output_data()
