# Задание 1
# Пользователь вводит с клавиатуры набор чисел. По-
# лученные числа необходимо сохранить в односвязный
# список. После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить элемент в список.
# 2. Удалить элемент из списка.
# 3. Показать содержимое списка.
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке.
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def add_element(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node
#
#     def remove_element(self, data):
#         if self.head is None:
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#         else:
#             current = self.head
#             while current.next is not None:
#                 if current.next.data == data:
#                     current.next = current.next.next
#                     return
#                 current = current.next
#
#     def display(self):
#         if self.head is None:
#             print("Список пуст!")
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.data, end=' ')
#                 current = current.next
#             print()
#
#     def contains(self, data):
#         current = self.head
#         while current is not None:
#             if current.data == data:
#                 return True
#             current = current.next
#         return False
#
#     def replace(self, old_value, new_value):
#         current = self.head
#         while current is not None:
#             if current.data == old_value:
#                 current.data = new_value
#                 return
#             current = current.next
#
#
# linked_list = LinkedList()
#
# while True:
#     print("Меню: ")
#     print("1. Добавить элемент в список")
#     print("2. Удалить элемент из списка")
#     print("3. Показать содержимое списка")
#     print("4. Проверить есть ли значение в списке")
#     print("5. Заменить значение в списке")
#     choice = input("Выберите действие (1-5): ")
#
#     if choice == "1":
#         element = input("Введите элемент для добавления в список: ")
#         linked_list.add_element(element)
#         print("Элемент добавлен в список!")
#     elif choice == "2":
#         element = input("Введите элемент для удаления из списка: ")
#         linked_list.remove_element(element)
#         print("Элемент удален из списка!")
#     elif choice == "3":
#         linked_list.display()
#     elif choice == "4":
#         element = input("Введите элемент для проверки наличия в списке: ")
#         if linked_list.contains(element):
#             print("Значение присутствует в списке!")
#         else:
#             print("Значение отсутствует в списке!")
#     elif choice == "5":
#         old_value = input("Введите значение, которое нужно заменить: ")
#         new_value = input("Введите новое значение: ")
#         linked_list.replace(old_value, new_value)
#         print("Значение успешно заменено!")
#     else:
#         print("Некорекктный выбор команды! Попробуйте снова!")


# Задание 2
# Пользователь вводит с клавиатуры набор строк. По-
# лученные строки необходимо сохранить в двусвязный
# список. После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить элемент в список
# 2. Удалить элемент из списка
# 1
# 3. Показать содержимое списка
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def add_element(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current
#
#     def remove_element(self, data):
#         if self.head is None:
#             return
#         current = self.head
#         while current:
#             if current.data == data:
#                 if current.prev:
#                     current.prev.next = current
#                 else:
#                     self.head = current.next
#                 if current.next:
#                     current.next.prev = current.prev
#                 return
#             current = current.next
#
#     def print_list(self):
#         if self.head is None:
#             print('Список пуст!')
#         else:
#             current = self.head
#             while current:
#                 print(current.data)
#                 current = current.next
#
#     def contains(self, data):
#         if self.head is None:
#             return False
#         current = self.head
#         while current:
#             if current.data == data:
#                 return True
#             current = current.next
#         return False
#
#     def replace(self, old_value, new_value):
#         if self.head is None:
#             return False
#         current = self.head
#         while current:
#             if current.data == old_value:
#                 current.data = new_value
#                 return True
#             current = current.next
#         return False
#
#
# linked_list = DoublyLinkedList()
#
# while True:
#     print("Меню: ")
#     print("1. Добавить элемент в список")
#     print("3. Показать содержимое списка")
#     print("4. Проверить есть ли значение в списке")
#     print("5. Заменить значение в списке")
#     choice = input("Выберите действие (1-5): ")
#
#     if choice == "1":
#         element = input("Введите элемент для добавления в список: ")
#         linked_list.add_element(element)
#         print("Элемент добавлен в список!")
#     elif choice == "2":
#         element = input("Введите элемент для удаления из списка: ")
#         linked_list.remove_element(element)
#         print("Элемент удален из списка!")
#     elif choice == "3":
#         linked_list.print_list()
#     elif choice == "4":
#         element = input("Введите элемент для проверки наличия в списке: ")
#         if linked_list.contains(element):
#             print("Значение присутствует в списке!")
#         else:
#             print("Значение отсутствует в списке!")
#     elif choice == "5":
#         old_value = input("Введите значение, которое нужно заменить: ")
#         new_value = input("Введите новое значение: ")
#         linked_list.replace(old_value, new_value)
#         print("Значение успешно заменено!")
#     else:
#         print("Некорекктный выбор команды! Попробуйте снова!")

# Задание 3
# Реализуйте класс стека для работы с целыми значе-
# ниями (стек целых).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение целого значения в стек;
# ■ выталкивание целого значения из стека;
# ■ подсчет количества целых в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхнего це-
# лого в стеке.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необ-
# ходимую операцию
# Задание 4
# Измените стек из третьего задания, таким образом,
# чтобы его размер был нефиксированным.

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, value):
#         self.stack.append(value)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             print("Стек пуст!")
#
#     def count(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def is_full(self):
#         return False
#
#     def clear(self):
#         self.stack = []
#
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             print("Стек пуст!")
#
#
# def display_menu():
#     print("1. Отправить значение в стек")
#     print("2. Извлечь значение из стека")
#     print("3. Подсчет значений в стеке")
#     print("4. Проверьте, пуст ли стек")
#     print("5. Очистить стек")
#     print("6. Получите значение с вершины стека, не выскакивая")
#     print("0. Выход")
#
#
# def main():
#     stack = Stack()
#     while True:
#         display_menu()
#         choice = int(input("Введите свой выбор: "))
#         if choice == 0:
#             break
#         elif choice == 1:
#             value = int(input("Введите значение для нажатия: "))
#             stack.push(value)
#         elif choice == 2:
#             popped_value = stack.pop()
#             if popped_value:
#                 print("Всплывшее значение: ", popped_value)
#         elif choice == 3:
#             count = stack.count()
#             print("Общее количество значений в стеке: ", count)
#         elif choice == 4:
#             if stack.is_empty():
#                 print("Стек пуст!")
#             else:
#                 print("Стек не пуст!")
#         elif choice == 5:
#             stack.clear()
#             print("Стек очищен!")
#         elif choice == 6:
#             top_value = stack.peek()
#             if top_value:
#                 print("Максимальное значение в стеке: ", top_value)
#         else:
#             print("Неверный выбор!")
#
#
# if __name__ == "__main__":
#     main()
