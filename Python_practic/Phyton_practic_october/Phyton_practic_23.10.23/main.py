# Классы - структуры данных

# 1.Очередь

# class Queue:
#     """
#     FIFO First in First out
#     """
#     def __init__(self):
#         self.queue = []
#
#     def add_i(self, item):
#         self.queue.append(item)
#
#     def pop_item(self):
#         if self.queue:
#             self.queue.pop(0)
#
#     def show_queue(self):
#         print('Очередь:', self.queue)
#         return self.queue
#
#
# queue = Queue()
# queue.show_queue()
# queue.add_i(5)
# queue.add_i(4)
# queue.show_queue()
# queue.pop_item()
# queue.show_queue()

# 2.Стек

# class Steck:
#     """
#     LIFO
#     """
#     def __init__(self):
#         self.steck = []
#
#     def add_i(self, item):
#         self.steck.append(item)
#
#     def pop_item(self):
#         if self.steck:
#             self.steck.pop(-1)
#
#     def show_steck(self):
#         print(f'Очередь: {self.steck}')
#         return self.steck
#
#
# steck = Steck()
# steck.show_steck()
# steck.add_i(5)
# steck.add_i(4)
# steck.show_steck()
# steck.pop_item()
# steck.show_steck()

# 3.Связанные списки

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head):
        self.head = head

    def get_all_nodes(self):
        current = self.head
        while current:
            yield current.value
            # print(current.value)
            current = current.next

    def remove_node(self, value):
        current = self.head
        prev = current
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def find_middle_node(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

    def change_head_nodes(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def reversed(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


head = Node(1)  # Головной узел

node_1 = Node(2)
head.next = node_1

node_2 = Node(3)
node_1.next = node_2

node_3 = Node(4)
node_2.next = node_3

node_4 = Node(5)
node_3.next = node_4

# print(head.value, head.next.value, head.next.next.value, head.next.next.next)

linked_list = LinkedList(head)
#
# linked_list.remove_node(3)
# linked_list.change_head_nodes(4)
# linked_list.get_all_nodes()
# linked_list.count_nodes()
# linked_list.find_middle_node()
# linked_list.get_all_nodes()
# print(linked_list.count_nodes())
# print(linked_list.find_middle_node())
# linked_list.reversed()
# linked_list.get_all_nodes()
# for i in linked_list.remove_node(3):
#     print(i)

# 1.Посчитать сколько всего узлов в связанном списке включая головной
# 2.Найти центральный узел
# 3.Получить значение по порядковому номеру узла


