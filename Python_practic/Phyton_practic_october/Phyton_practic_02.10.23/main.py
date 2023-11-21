#  Работа с файлами

# file = open('filename.txt', 'r+')  # 'r' - флаг открытия файла и чтения файла 'r+'
                                   # 'w' - флаг открытия файла и записи 'w+'
                                   # 'a' - флаг открытия файла и дозапись
# text = file.read()  # чтение файла
# file.write('Ok')
# text = file.read()
# print(text)
# file.write(f'Привет, я файл!\n')  # дозапись в файле
# file.write(f'Привет, я файл!\n')

# file.close()  # метод закрытия файла

######################################################################################

# file = open('filename.txt', 'r+')

# for _ in range(5):
#     file.write('Привет, я файл!\n')
# text = file.readlines()  #  Выводит текст файла по строкам в консоль и добовляет ее в список
                         #  readline берет только первую строчку
# print(text)
#
# file.close()

# Принудительное закрытие файла несмотря на ошибку

# file = open('filename.txt', 'r+')
#
# try:
#     text = file.readlines()
#     raise ValueError
#     print(text)
# except ValueError:
#     print('Поймали ошибку!')
# finally:
#     print('Файл закрыт!')
#     file.close()

######################################################################################

# filename_bin = open('file.bin', 'rb')  # 'b' - это байт строка

# filename_bin.write(bytes('Какой-то текст'.encode()))  #  encode кодирование текста bytes переводит текст в байты
# print(filename_bin.read().decode())  # decode декодирование текста в консоли
# filename_bin.close()

#  Контекстный менеджер самостоятельно закрывает файл

# with open('filename.txt', 'r') as file:
#     print(file.read())


# class CustomFile:
#     def __init__(self, file_name, mode):
#         self.file_name = file_name
#         self.mode = mode
#
#
#     def __enter__(self):
#         self.file = open(self.file_name, self.mode)
#         return self.file
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('работал метод exit')
#         print(exc_type)
#         self.file.write(str(exc_tb))
#         self.file.close()
#         print('Файл закрыт')
#
#
# with CustomFile('filename.txt', 'r') as file:
#     raise ValueError

######################################################################################
# with open('filename.txt', 'w') as file:
#     file.write('Привет')

######################################################################################

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
#
# def caesar_code(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in text.lower()]
#     return ''.join(decrypted_list)
#
#
# with open('text.txt', 'w', encoding='utf-8') as file_1:
#     for _ in range(5):
#         file_1.write('Привет\n')
#
#
# with open('cipher_text.txt', 'a', encoding='utf-8') as file_2:
#     with open('text.txt', 'r', encoding='utf-8') as file_1:
#         lines = file_1.readlines()
#         shift = 1
#         for i_line in lines:
#             ciphered = caesar_code(i_line.strip(), shift)
#             file_2.write(ciphered + '\n')
#             file_2.write(ciphered[:len(ciphered) // 2] + f'{shift}' + ciphered[len(ciphered) // 2:] + '\n')
#             shift += 1

######################################################################################

# frequency = {}
#
# with open('zen.txt', 'r') as file:
#     text = file.read().lower()
#     for sym in text:
#         if sym.isalpha():
#             frequency.setdefault(sym, text.count(sym))
#
#     frequency = {sym: text.count(sym) for sym in text if sym.isalpha()}
#     print(frequency)
#
#     frequency = {sym: text.count(sym) for sym in text if sym.isalpha()}
#     alpha_num = len(frequency.keys())
#     total_num = sum(frequency.values())
#     min_alpha = min(frequency.values())
#     file.seek(0)  # перемещает курсор на определенную позицию
#     lines_num = len(file.readlines())
#     word_num = len(text.split())
#
#     print(alpha_num)
#     print(total_num)
#     print(min_alpha)
#     print(lines_num)
#     print(word_num)

######################################################################################

# frequency = {}
#
# with open('zen.txt', 'r') as file:
#     text = file.read().lower()
#
# file.seek(0)
# revers_text = file.readlines()[::-1]
#
# for i in revers_text:
#     file.write(i.strip() + '\n')

######################################################################################

with open('redact.txt', 'r') as file_1:
    with open('badword.txt', 'r+') as file_2:
        file_1.seek(0)
        text = file_2.read()
        for bad in file_1.readlines():
            if bad.strip() in text:
                text = text.replace(bad, '')
        file_2.write(text)
    with open('badword.txt', 'w') as file_2:
        file_2.write(text)
