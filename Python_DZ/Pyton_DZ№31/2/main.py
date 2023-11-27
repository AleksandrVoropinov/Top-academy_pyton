# Задание 2
# Пользователь с клавиатуры вводит путь к файлу.
# После чего запускаются три потока. Первый поток за-
# полняет файл случайными числами. Два других потока
# ожидают заполнения. Когда файл заполнен оба потока
# стартуют. Первый поток находит все простые числа, вто-
# рой поток факториал каждого числа в файле. Результаты
# поиска каждый поток должен записать в новый файл. На
# экран необходимо отобразить статистику выполненных
# операций.

import random
import threading
import math


def generate_numbers(file_path):
    with open(file_path, 'w') as file:
        for _ in range(100):
            number = random.randint(1, 100)
            file.write(str(number) + '\n')


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


def find_primes(file_path, output_file_path):
    prime_numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            if is_prime(number):
                prime_numbers.append(number)
    with open(output_file_path, 'w') as output_file:
        output_file.write('Prime Numbers:\n')
        for number in prime_numbers:
            output_file.write(str(number) + '\n')


def calculate_factorials(file_path, output_file_path):
    factorials = []
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factorial = calculate_factorial(number)
            factorials.append(factorial)
    with open(output_file_path, 'w') as output_file:
        output_file.write('Factorials:\n')
        for factorial in factorials:
            output_file.write(str(factorial) + '\n')


def main():
    file_path = input('Enter file path: ')

    thread1 = threading.Thread(target=generate_numbers, args=(file_path,))
    thread2 = threading.Thread(target=find_primes, args=(file_path, 'prime_numbers.txt'))
    thread3 = threading.Thread(target=calculate_factorials, args=(file_path, 'factorials.txt'))

    thread1.start()
    thread1.join()

    thread2.start()
    thread3.start()
    thread2.join()
    thread3.join()

    print('Operations statistics:')
    print('Prime numbers found:', len(open('prime_numbers.txt').readlines()) - 1)
    print('Factorials calculated:', len(open('factorials.txt').readlines()) - 1)


if __name__ == '__main__':
    main()
