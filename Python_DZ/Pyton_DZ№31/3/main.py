# Задание 3
# Пользователь с клавиатуры вводит путь к существу-
# ющей директории и к новой директории. После чего
# запускается поток, который должен скопировать содер-
# жимое директории в новое место. Необходимо сохранить
# структуру директории. На экран необходимо отобразить
# статистику выполненных операций.

import os
import shutil


def copy_directory_contents(source, destination):
    if not os.path.exists(source):
        print("Директория-источник не существует")
        return
    if not os.path.isdir(source):
        print("Путь не указывает на директорию")
        return
    if not os.path.exists(destination):
        os.makedirs(destination)

    files_copied = 0
    directories_created = 0

    for root, dirs, files in os.walk(source):
        dest_dir = os.path.join(destination, os.path.relpath(root, source))
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            directories_created += 1
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)
            files_copied += 1
    print("Скопировано файлов:", files_copied)
    print("Создано директорий:", directories_created)


source_directory = input("Введите путь к существующей директории: ")
destination_directory = input("Введите путь к новой директории: ")

copy_directory_contents(source_directory, destination_directory)
