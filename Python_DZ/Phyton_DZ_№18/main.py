# Создайте программу «Фирма». Нужно хранить ин-
# формацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поис-
# ка, замены данных. Используйте словарь для хранения
# информации.

person = {'name': 'John Smith', 'tel': 33333, 'email': 'job@mail.ru', 'job_title': 'Manager', 'number_office': 10,
          'skype': 'jodwork'}


def main():
    while True:
        action = input("1-add \n"
                       "2-remove \n"
                       "3-search \n"
                       "4-replace: ")
        if action == 'add':
            key = input("Введите ключ для добавления: ")
            value = input("Введите значение для добавления: ")
            person[key] = value

        elif action == 'remove':
            key = input("Введите ключ для удаления: ")
            del person[key]

        elif action == 'search':
            key: str = input("Введите ключ для поиска: ")
            if key in person:
                print(f"{key}: {person[key]}")

            else:
                print(f"{key} данного ключа нет в словаре.")

        elif action == 'replace':
            key = input("Введите ключ для замены: ")
            value = input("Введите новое значение: ")
            person[key] = value

        else:
            print('Такой команды нет!')


main()
