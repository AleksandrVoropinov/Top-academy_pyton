# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.

# Открываем файл для чтения
with open('input.txt', 'r+') as file:
    data = file.read()

# Подсчет количества символов
num_chars = len(data)

# Подсчет количества строк
num_lines = data.count('\n') + 1

# Подсчет количества гласных и согласных букв
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
num_vowels = 0
num_consonants = 0
for char in data:
    if char.isalpha():
        if char.lower() in vowels:
            num_vowels += 1
        else:
            num_consonants += 1

# Подсчет количества цифр
num_digits = sum(c.isdigit() for c in data)

# Открываем файл для записи статистики
with open('output.txt', 'w+') as file:
    file.write(f'Количество символов: {num_chars}\n')
    file.write(f'Количество строк: {num_lines}\n')
    file.write(f'Количество гласных букв: {num_vowels}\n')
    file.write(f'Количество согласных букв: {num_consonants}\n')
    file.write(f'Количество цифр: {num_digits}\n')
