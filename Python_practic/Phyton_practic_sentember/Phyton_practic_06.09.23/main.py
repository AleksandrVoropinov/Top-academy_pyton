# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8]
# print(list_1 + list_2)  # Объединение списков
# print(list_1 * 2)  # Дублирование элементов списка

# list_1.extend(list_2)  # Расширение списка элементами второго списка
# print(list_1)

############################################################################

# list_1 = ['1', '2', '3', '4']
# string = ' '
# new_string = string.join(list_1)
# print(new_string)
# for i in list_1:
#     string += f'{i}'
# print(string)

############################################################################

# List comprehensions

# list_1 = [i for i in range(1, 10)]  # Наполнение списка
# for i in range(1, 10):
#     list_1.append(i)
# print(list_1)

############################################################################

# import sys

# list_1 = [i for i in range(1, 10)]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(list_2))

# list_1 = [i for i in range(1, 10) if i % 2 == 0]
# list_1 = [i * i for i in range(1, 10) if i % 2 != 0]  # Либо i ** 2
# print(list_1)

# list_2 = [i for i in range(1, 5) for _ in range(5)]  # Дубликат чисел в списке
# list_2 = [[i for i in range(1, 5)] for _ in range(5)]  # Дубликаты списков
# list_3 = [i * j for i in range(1, 5) for j in range(1, 6)]
# print(list_3)

# list_4 = [35, 7, 4, 87, 65]
# list_5 = [num for num in list_4 if num % 7 == 0]
# print(list_5)

############################################################################

# import string
# letters = string.ascii_letters
#
# input_text = 'hell@o m#y na!me is Al$ex'
# letters_list = [letter for letter in input_text if (letter in letters or letter.isspace())]
# print(''.join(letters_list).upper())

############################################################################

# import string
#
# digits = string.digits
#
# input_text = 'fweff1234few 12sdfsd908sdf2'
# digits_list = [i for i in input_text if i in digits]
# print(''.join(digits_list), len(digits_list))

############################################################################

# students = [
#     ['Петров', 4.5],
#     ['Иванов', 4.2],
#     ['Сидоров', 4.1],
#     ['Петрова', 3.5],
#     ['Иванова', 4.9],
# ]
#
# students_2 = [student for student in students if student[1] >= 4.5]
# print(students_2)

############################################################################


