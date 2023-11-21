# Задание 1
# Пользователь вводит с клавиатуры набор чисел. По-
# лученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число су-
# ществует в списке, нужно вывести сообщение поль-
# зователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от вы-
# бора пользователя список нужно показать с начала
# или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь опреде-
# ляет заменить ли только первое вхождение или все
# вхождения)
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.

# numbers = []  # создаем пустой список для хранения чисел
#
# while True:  # выполняем ввод чисел до тех пор, пока пользователь не введет пустую строку
#     user_input = input("Введите число (для завершения введите пустую строку): ")
#     if user_input == " ":
#         break
#     else:
#         numbers.append(int(user_input))
#
# while True:  # показываем меню и выполняем действие в зависимости от выбора пользователя
#     print("Меню:")
#     print("1. Добавить новое число в список")
#     print("2. Удалить все вхождения числа из списка")
#     print("3. Показать содержимое списка")
#     print("4. Проверить есть ли значение в списке")
#     print("5. Заменить значение в списке")
#     choice = int(input("Выберите пункт меню (1-5): "))
#
#     if choice == 1:  # добавление нового числа в список
#         number = int(input("Введите новое число: "))
#         if number in numbers:
#             print("Такое число уже есть в списке")
#         else:
#             numbers.append(number)
#     elif choice == 2:  # удаление всех вхождений числа из списка
#         number = int(input("Введите число для удаления: "))
#         if number in numbers:
#             numbers = [x for x in numbers if x != number]
#             print("Все вхождения числа", number, "были удалены")
#         else:
#             print("Число", number, "не найдено в списке")
#     elif choice == 3:  # показ содержимого списка
#         order_choice = input("Выберите порядок показа (начало или конец): ")
#         if order_choice.lower() == "начало":
#             print("Содержимое списка:", numbers)
#         elif order_choice.lower() == "конец":
#             print("Содержимое списка:", numbers[::-1])
#         else:
#             print("Некорректный выбор порядка показа")
#     elif choice == 4:  # проверка наличия значения в списке
#         number = int(input("Введите значение для проверки: "))
#         if number in numbers:
#             print("Значение", number, "найдено в списке")
#         else:
#             print("Значение", number, "не найдено в списке")
#     elif choice == 5:  # замена значения в списке
#         number = int(input("Введите значение для замены: "))
#         replace_choice = input("Заменить только первое вхождение или все вхождения? (первое/все): ")
#
#         if replace_choice.lower() == "первое":
#             if number in numbers:
#                 index = numbers.index(number)
#                 numbers[index] = int(input("Введите новое значение: "))
#             else:
#                 print("Значение", number, "не найдено в списке")
#         elif replace_choice.lower() == "все":
#             if number in numbers:
#                 new_number = int(input("Введите новое значение: "))
#                 numbers = [new_number if x == number else x for x in numbers]
#             else:
#                 print("Значение", number, "не найдено в списке")
#         else:
#             print("Некорректный выбор действия")
#     else:
#         print("Некорректный выбор пункта меню")

# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необ-
# ходимую операцию.


# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = []
#
#     def push(self, item):
#         if len(self.stack) == self.size:
#             print("Стек полный")
#         else:
#             self.stack.append(item)
#             print("Строка добавлена в стек")
#
#     def pop(self):
#         if len(self.stack) == 0:
#             print("Стек пустой")
#         else:
#             self.stack.pop()
#             print("Строка удалена из стека")
#
#     def count(self):
#         count = len(self.stack)
#         print("Количество строк в стеке:", count)
#
#     def is_empty(self):
#         if len(self.stack) == 0:
#             print("Стек пустой")
#         else:
#             print("Стек не пустой")
#
#     def is_full(self):
#         if len(self.stack) == self.size:
#             print("Стек полный")
#         else:
#             print("Стек не полный")
#
#     def clear(self):
#         self.stack = []
#         print("Стек очищен")
#
#     def get_top(self):
#         if len(self.stack) == 0:
#             print("Стек пустой")
#         else:
#             top = self.stack[-1]
#             print("Значение верхней строки:", top)
#
#
# def show_menu():
#     print("Выберите операцию:")
#     print("1. Поместить строку в стек")
#     print("2. Вытолкнуть строку из стека")
#     print("3. Подсчитать количество строк в стеке")
#     print("4. Проверить, пустой ли стек")
#     print("5. Проверить, полный ли стек")
#     print("6. Очистить стек")
#     print("7. Получить значение верхней строки стека")
#     print("0. Выход")
#
#
# stack_size = 5
# stack = Stack(stack_size)
#
# while True:
#     show_menu()
#     choice = input("Ваш выбор: ")
#
#     if choice == "1":
#         item = input("Введите строку: ")
#         stack.push(item)
#     elif choice == "2":
#         stack.pop()
#     elif choice == "3":
#         stack.count()
#     elif choice == "4":
#         stack.is_empty()
#     elif choice == "5":
#         stack.is_full()
#     elif choice == "6":
#         stack.clear()
#     elif choice == "7":
#         stack.get_top()
#     elif choice == "0":
#         print("Выход из программы")
#         break
#     else:
#         print("Неправильный выбор. Повторите попытку.")

# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print("Строка успешно помещена в стек")

    def pop(self):
        if self.is_empty():
            print("Стек пустой")
        else:
            item = self.stack.pop()
            print("Извлеченная строка:", item)

    def count(self):
        count = len(self.stack)
        print("Количество строк в стеке:", count)

    def is_empty(self):
        if len(self.stack) == 0:
            print("Стек пустой")
        else:
            print("Стек не пустой")

    def is_full(self):
        print("Стек не может быть полным, так как его размер не ограничен")

    def clear(self):
        self.stack = []
        print("Стек очищен")

    def get_top(self):
        if self.is_empty():
            print("Стек пустой")
        else:
            top = self.stack[-1]
            print("Значение верхней строки:", top)


def show_menu():
    print("Выберите операцию:")
    print("1. Поместить строку в стек")
    print("2. Вытолкнуть строку из стека")
    print("3. Подсчитать количество строк в стеке")
    print("4. Проверить, пустой ли стек")
    print("5. Проверить, полный ли стек")
    print("6. Очистить стек")
    print("7. Получить значение верхней строки стека")
    print("0. Выход")


stack = Stack()

while True:
    show_menu()
    choice = input("Ваш выбор: ")

    if choice == "1":
        item = input("Введите строку: ")
        stack.push(item)
    elif choice == "2":
        stack.pop()
    elif choice == "3":
        stack.count()
    elif choice == "4":
        stack.is_empty()
    elif choice == "5":
        print("Стек не может быть полным, так как его размер не ограничен")
    elif choice == "6":
        stack.clear()
    elif choice == "7":
        stack.get_top()
    elif choice == "0":
        print("Выход из программы")
        break
    else:
        print("Неправильный выбор. Повторите попытку.")
