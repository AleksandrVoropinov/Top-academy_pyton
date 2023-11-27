# Задание 4
# Пользователь с клавиатуры вводит путь к существующей
# директории и слово для поиска. После чего запускаются
# два потока. Первый должен найти файлы, содержащие
# искомое слово и слить их содержимое в один файл. Вто-
# рой поток ожидает завершения работы первого потока.
# После чего проводит вырезание всех запрещенных слов
# (список этих слов нужно считать из файла с запрещенны-
# ми словами) из полученного файла. На экран необходимо
# отобразить статистику выполненных операций.

import os
import threading


def search_files(dir_path, keyword, result_file):
    files_with_keyword = []
    for current_dir, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(current_dir, file)
            with open(file_path, 'r') as f:
                if keyword in f.read():
                    files_with_keyword.append(file_path)

    with open(result_file, 'w') as f:
        for file_path in files_with_keyword:
            with open(file_path, 'r') as file:
                f.write(file.read())

    print(f"Первая тема: {len(files_with_keyword)} найдено файлов.")


def remove_banned_words(result_file, banned_words_file):
    banned_words = []
    with open(banned_words_file, 'r') as f:
        banned_words = f.read().splitlines()

    with open(result_file, 'r+') as f:
        content = f.read()
        for banned_word in banned_words:
            content = content.replace(banned_word, '')
        f.seek(0)
        f.write(content)
        f.truncate()

    print(f"Вторая тема: Запрещенные слова удалены.")


if __name__ == "__main__":
    dir_path = input("Введите путь к каталогу: ")
    keyword = input("Введите ключевое слово: ")
    result_file = "result.txt"
    banned_words_file = "banned_words.txt"

    thread1 = threading.Thread(target=search_files, args=(dir_path, keyword, result_file))
    thread2 = threading.Thread(target=remove_banned_words, args=(result_file, banned_words_file))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    print("Операции завершились успешно.")
