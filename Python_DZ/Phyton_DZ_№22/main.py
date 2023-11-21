# Генераторы
#
# 1. Генераторное выражение выдающее квадраты чисел из заданного
# диапазона чисел.
# 2. Генераторная функция принимающая начало и конец диапазона,
# и выдающая только простые числа.
# 3*. Класс-итератор выдающий только чётные числа из заданного диапазона

# Генераторное выражение выдающее квадраты чисел из заданного диапазона чисел

# numbers = [1, 2, 3, 4, 5]
# squares = (x**2 for x in numbers)
# for square in squares:
#     print(square)

# Генераторная функция принимающая начало и конец диапазона и выдающая только простые числа


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def primes(start, end):
#     for num in range(start, end+1):
#         if is_prime(num):
#             yield num
#
#
# for prime in primes(1, 10):
#     print(prime)

# Класс-итератор выдающий только чётные числа из заданного диапазона


# class EvenNumbers:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start % 2 == 1:
#             self.start += 1
#         if self.start > self.end:
#             raise StopIteration
#         result = self.start
#         self.start += 2
#         return result
#
#
# even_nums = EvenNumbers(1, 30)
# for even_num in even_nums:
#     print(even_num)
