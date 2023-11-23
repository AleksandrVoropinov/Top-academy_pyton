# Конкурентность, параллелизм

# import threading
#
#
# def hello_from_thread():
#     print(f'hello from thread {threading.current_thread()}!')
#
#
# hello_thread = threading.Thread(target=hello_from_thread)
# hello_thread.start()
# total_threads = threading.active_count()
# thread_name = threading.current_thread().name
#
# print(f'Python execute {total_threads} threads')
# print(f'Thread name {thread_name}')
#
# hello_thread.join()
#
#
# if __name__ == "__main__":
#     hello_from_thread()

###############################################################

# from multiprocessing import Process
# import os
#
#
# def hello_from_process():
#     print(f'hello from child process {os.getpid()}!')
#
#
# if __name__ == '__main__':
#     hello_process = Process(target=hello_from_process)
#     hello_process.start()
#     print(f'parent process {os.getpid()}')
#     hello_process.join()

###############################################################

# Задание 1
# Пользователь с клавиатуры вводит значения в список.
# После чего запускаются две потока. Первый поток нахо-
# дит максимум в списке. Второй поток находит минимум
# в списке. Результаты вычислений выводятся на экран.

# import threading
#
#
# def find_max(arr):
#     max_value = max(arr)
#     print('Максимальный элемент: ', max_value)
#
#
# def find_min(arr):
#     min_value = min(arr)
#     print('Минимальный элемент: ', min_value)
#
#
# arr = []
# num = int(input('Введите кол-во элементов: '))
# for i in range(num):
#     arr.append(int(input('Введите элемент: ')))
#
# if __name__ == "__main__":
#     thread1 = threading.Thread(target=find_max, args=(arr,))
#     thread2 = threading.Thread(target=find_min, args=(arr,))
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()

###############################################################

# Задание 2
# Пользователь с клавиатуры вводит значения в спи-
# сок. После чего запускаются две потока. Первый поток
# находит сумму элементов в списке. Второй поток находит
# среднеарифметическое в списке. Результаты вычислений
# выводятся на экран

# import threading
#
#
# def sum_list(lst):
#     try:
#         total = sum(lst)
#         print('Сумма элеменетов в списке: ', total)
#     except ValueError:
#         print('Ошибка: список содержит некоректные значения!')
#
#
# def average_list(lst):
#     try:
#         average = sum(lst) / len(lst)
#         print('Среднеарифметическое в списке: ', average)
#     except ZeroDivisionError:
#         print('Ошибка список пуст!')
#
#
# lst = input('Введите значение через пробел: ').split()
# try:
#     lst = [int(x) for x in lst]
# except ValueError:
#     print('Ошибка введены некоректные значения!')
#
#
# if __name__ == "__main__":
#     sum_thread = threading.Thread(target=sum_list, args=(lst,))
#     avg_thread = threading.Thread(target=average_list, args=(lst,))
#
#     sum_thread.start()
#     avg_thread.start()
#
#     sum_thread.join()
#     avg_thread.join()

###############################################################

# Реализуйте клиент — серверное приложение, позво-
# ляющее обмениваться сообщениями в формате один к
# одному. Для начала общения необходимо установить
# соединение. После соединение используется текстовый
# формат. В беседе участвуют только два человека. После
# завершения беседы сервер переходит к ожиданию нового
# участника разговора.

import socket


def start_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f'Сервер ожидает на {host} : {port}')

    while True:
        conn, address = server_socket.accept()
        print(f'Соединение установленно с {address}')

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f'Клиент {data=}')
            message = input('-> ')
            conn.send(message.encode())

        conn.close()
        print('Соединение закрыто!')


if __name__ == "__main__":
    start_server()

