# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеариф-
# метическое каждой группы.

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

sum_of_even = 0
sum_of_odd = 0
sum_of_multiples = 0
avg_1 = 0
avg_2 = 0
avg_3 = 0

for i in range(num_1, num_2 + 1):
    if i % 2 == 0:
        sum_of_even += i
    avg_1 = sum_of_even/num_2
    if i % 2 != 0:
        sum_of_odd += i
    avg_2 = sum_of_odd/num_2
    if i % 9 == 0:
        sum_of_multiples += i
    avg_3 = sum_of_multiples/num_2
print(f"Сумма четных чисел в диапазоне от {num_1} до {num_2} равна {sum_of_even}")
print(f"Среднее арифметическое четных чисел равно: {avg_1}")

print(f"Сумма нечетных чисел в диапазоне от {num_1} до {num_2} равна {sum_of_odd}")
print(f"Среднее арифметическое нечетных чисел равно: {avg_2}")

print(f"Сумма чисел, кратных 9, в диапазоне от {num_1} до {num_2} равна {sum_of_multiples}")
print(f"Среднее арифметическое кратных 9 равно: {avg_3}")

# Задание 2
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины.

line = int(input('Введите длину линии: '))
Simbol = input('Введите символ: ')

for i in range(line):
    print(Simbol)

# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»

num = int(input('Введите любое число: '))
start = 0
end = 0

for i in range(start, end + 1):

    if num > 0:
        print("Number is positive")

    elif num < 0:
        print("Number is negative")

    else:
        print("Number is equal to zero")

    if num == 7:
        print("Good bye!")
        break
