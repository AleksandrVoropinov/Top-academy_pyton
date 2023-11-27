# Задание 1
# При старте приложения запускаются три потока.
# Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список
# заполнен оба потока запускаются. Первый поток находит
# сумму элементов списка, второй поток среднеарифмети-
# ческое значение в списке. Полученный список, сумма и
# среднеарифметическое выводятся на экран.

import random
import threading


def fill_list(lst):
    for _ in range(10):
        lst.append(random.randint(1, 100))


def calculate_sum(lst):
    sum_lst = sum(lst)
    print("Сумма элементов списка:", sum_lst)


def calculate_average(lst):
    average = sum(lst) / len(lst)
    print("Среднеарифметическое значение списка:", average)


lst = []
thread1 = threading.Thread(target=fill_list, args=(lst,))
thread2 = threading.Thread(target=calculate_sum, args=(lst,))
thread3 = threading.Thread(target=calculate_average, args=(lst,))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Список:", lst)
