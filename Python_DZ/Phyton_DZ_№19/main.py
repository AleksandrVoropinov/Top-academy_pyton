# Задание 1
# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.

# array_1 = [1, 5, 12, 32, 47, 70, 99]
# array_2 = [5, 7, 12, 47, 99]
# array_3 = [3, 5, 12, 20, 31, 47, 80, 99]
#
# res = tuple(set(array_1) & set(array_2) & set(array_3))
# print(res)

# Задание 2
# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка.

# array_1 = [1, 5, 12, 32, 47]
# array_2 = [5, 7, 12, 99, 47]
# array_3 = [3, 5, 12, 20, 31]
#
#
# def find_unique_elements(array_1, array_2, array_3):
#
#     intersection = set(array_1) & set(array_2) & set(array_3)
#     unique_1 = []
#     unique_2 = []
#     unique_3 = []
#
#     # Проверяем каждый элемент каждого списка
#     for num in array_1:
#         if num not in intersection:
#             unique_1.append(num)
#
#     for num in array_2:
#         if num not in intersection:
#             unique_2.append(num)
#
#     for num in array_3:
#         if num not in intersection:
#             unique_3.append(num)
#
#     return unique_1, unique_2, unique_3
#
#
# result = find_unique_elements(array_1, array_2, array_3)
# print(result)


# Задание 3
# Есть три кортежа целых чисел необходимо найти эле-
# менты, которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.

# array_1 = [1, 5, 12, 32, 47]
# array_2 = [5, 7, 12, 99, 47]
# array_3 = [3, 5, 12, 20, 31]
#
# result = []
#
# for i in range(len(array_1)):
#     if array_1[i] == array_2[i] == array_3[i]:
#         result.append(array_1[i])
#
# print(result)
