# Патерны - шаблон

# class Singleton:
#     _instance = None
#
#    def __new__(cls):
#        if cls._instance is None:
#            cls._instance = super(Singleton, cls).__new__(cls)
#
#        return cls._instance
#
#
# def test_singleton_identify():
#     singleton_1 = Singleton()
#     singleton_2 = Singleton()
#
#     assert singleton_1 is singleton_2, 'Singleton instances are not same'
#
#
# def test_singleton_state():
#     singleton_1 = Singleton()
#     singleton_1.data = 'Singleton data'
#     singleton_2 = Singleton()
#
#     assert singleton_2.data == 'Singleton data', 'Singleton state is not share'
#
#
# test_singleton_state()
# test_singleton_identify()

##################################################################################

# class AbstractFactory:
#     def create_product_a(self):
#         raise NotImplemented
#
#
# class ConcreteFactory(AbstractFactory):
#     def create_product_a(self):
#         return ProductA1()
#
#     def create_product_b(self):
#         return ProductB1()
#
#
# class ProductA1:
#     ...
#
#
# class ProductB1:
#     ...
#
#
# def test_concrete_factory_creation():
#     factory = ConcreteFactory()
#
#     assert isinstance(factory, AbstractFactory), "ConcreteFactory is not an instance of AbstractFactory"
#
#
# def test_product_creation_by_factory():
#     factory = ConcreteFactory()
#
#     product_a = factory.create_product_a()
#     product_b = factory.create_product_b()
#
#     assert isinstance(product_a, ProductA1), "ProductA is not created by ConcreteFactory"
#     assert isinstance(product_b, ProductB1), "ProductB is not created by ConcreteFactory"
#
#
# test_concrete_factory_creation()
# test_product_creation_by_factory()

##################################################################################

# Задание 3
# Пользователь вводит с клавиатуры набор чисел и путь
# к файлу для сохранения полученных данных. Необходимо:
# ■ Сохранить все полученные числа.
# ■ Найти максимум, минимум. Эти значения сохранить
# в том же файле.
# ■ Отобразить числа.
# ■ Отобразить максимум и минимум.
# ■ Создать класс для логгирования операций. При созда-
# нии объекта класса нужно уточнить куда производится
# логгирование: экран или файл. В программе можно
# создать только один объект класса. Все действия в программе необходимо логгировать с помощью объекта этого класса


# import logging
#
# # Создание класса для логгирования операций
#
#
# class Logger:
#     def _init_(self, log_type):
#         self.log_type = log_type
#         if self.log_type == "screen":
#             logging.basicConfig(format="%(message)s", level=logging.INFO)
#         elif self.log_type == "file":
#             logging.basicConfig(
#                 filename="log.txt",
#                 format="%(asctime)s - %(message)s",
#                 level=logging.INFO,
#             )
#
#     def log(self, message):
#         logging.info(message)
#
#
# # Функция для сохранения чисел в файл и поиска максимума и минимума
# def save_numbers(filepath):
#     numbers = []
#     maximum = float("-inf")
#     minimum = float("inf")
#
#     # Ввод набора чисел
#     input_str = input("Введите набор чисел через пробел: ")
#     input_numbers = input_str.split()
#
#     # Преобразование строк в числа и поиск максимума и минимума
#     for num in input_numbers:
#         number = float(num)
#         numbers.append(number)
#         if number > maximum:
#             maximum = number
#         if number < minimum:
#             minimum = number
#
#     # Сохранение чисел, максимума и минимума в файл
#     with open(filepath, "w") as file:
#         file.write("Числа:\n")
#         for number in numbers:
#             file.write(str(number) + "\n")
#         file.write("\n")
#         file.write("Максимум: " + str(maximum) + "\n")
#         file.write("Минимум: " + str(minimum) + "\n")
#
#     return numbers, maximum, minimum
#
#
# # Отображение чисел, максимума и минимума
# def display_data(numbers, maximum, minimum):
#     print("Числа:")
#     for number in numbers:
#         print(number)
#     print("Максимум:", maximum)
#     print("Минимум:", minimum)
#
#
# # Главная функция
# def main():
#     # Ввод пути к файлу
#     file_path = input("Введите путь к файлу: ")
#
#     # Создание объекта класса для логгирования
#     logger = Logger("file")
#
#     # Сохранение чисел и поиск максимума и минимума
#     numbers, maximum, minimum = save_numbers(file_path)
#
#     # Логгирование результатов
#     logger.log("Сохранены числа: " + str(numbers))
#     logger.log("Максимум: " + str(maximum))
#     logger.log("Минимум: " + str(minimum))
#
#     # Отображение чисел, максимума и минимума
#     display_data(numbers, maximum, minimum)
#
#
# # Вызов главной функции
# main()


# class Logger:
#     _instance = None
#
#     def __new__(cls, output_type="screen"):
#         if cls._instance is None:
#             cls._instance = super(Logger, cls).__new__(cls)
#             cls._output_type = output_type
#         return cls._instance
#
#     def log(self, message):
#         if self._output_type == "file":
#             with open("log.txt", "a") as file:
#                 file.write(message + "\n")
#         else:
#             print(message)
#
#
# def read_numbers():
#     numbers = input("Enter numbers separated by space: ")
#     return list(map(int, numbers.split()))
#
#
# def save_numbers(numbers, file_path):
#     with open(file_path, "w") as file:
#         for number in numbers:
#             file.write(f"{number}\n")
#
#
# def find_min_max(numbers):
#     return min(numbers), max(numbers)
#
#
# def main():
#     logger = Logger(output_type="screen")  # or "file" for logging to a file
#     numbers = read_numbers()
#     file_path = input("Enter file path to save: ")
#
#     logger.log(f"Numbers: {numbers}")
#     save_numbers(numbers, file_path)
#     logger.log(f"Numbers saved to file {file_path}")
#
#     min_num, max_num = find_min_max(numbers)
#     logger.log(f"Minimum number: {min_num}, Maximum number: {max_num}")
#
#     # Additionally, save the min and max number to the file
#     with open(file_path, "a") as file:
#         file.write(f"Minimum number: {min_num}, Maximum number: {max_num}")
#
#
# main()

##################################################################################

# Патерн стратегия

# import unittest
#
#
# class ArrayOperations:
#     def __init__(self, strategy):
#         self.strategy = strategy
#         self.data = []
#
#     def execute(self):
#         return self.strategy.execute(self.data)
#
#
# class DisplayStrategy:
#     def execute(self, data):
#         return "Displaying: " + str(data)
#
#
# class ReverseStrategy:
#     def execute(self, data):
#         return "Reversed: " + str(data[::-1])
#
#
# class FindMaxStrategy:
#     def execute(self, data):
#         return "Max: " + str(max(data))
#
#
# class FindMinStrategy:
#     def execute(self, data):
#         return "Min: " + str(min(data))
#
#
# class TestStrategyPattern(unittest.TestCase):
#     def setUp(self):
#         self.data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
#
#     def test_display_strategy(self):
#         operations = ArrayOperations(DisplayStrategy())
#         operations.data = self.data
#         self.assertEqual(operations.execute(), "Displaying: [3, 1, 4, 1, 5, 9, 2, 6, 5]")
#
#     def test_reverse_strategy(self):
#         operations = ArrayOperations(ReverseStrategy())
#         operations.data = self.data
#         self.assertEqual(operations.execute(), "Reversed: [5, 6, 2, 9, 5, 1, 4, 1, 3]")
#
#     def test_find_max_strategy(self):
#         operations = ArrayOperations(FindMaxStrategy())
#         operations.data = self.data
#         self.assertEqual(operations.execute(), "Max: 9")
#
#     def test_find_min_strategy(self):
#         operations = ArrayOperations(FindMinStrategy())
#         operations.data = self.data
#         self.assertEqual(operations.execute(), "Min: 1")
#
#
# if __name__ == "__main__":
#     unittest.main()

##################################################################################

# Паттерн адаптер

# import unittest
#
#
# class OldSystem:
#     def specific_request(self):
#         return "Old system functionality"
#
#
# class Adapter:
#     def __init__(self, old_system):
#         self.old_system = old_system
#
#     def request(self):
#         return self.old_system.specific_request()
#
#
# class TestAdapterPattern(unittest.TestCase):
#     def test_adapter(self):
#         old_system = OldSystem()
#         adapter = Adapter(old_system)
#         self.assertEqual(adapter.request(), "Old system functionality")
#
#
# if __name__ == "__main__":
#     unittest.main()

##################################################################################

# Патерн фасад

# import unittest
#
#
# class SubsystemOne:
#     def operation_one(self):
#         return "Operation 1 from Subsystem One"
#
#
# class SubsystemTwo:
#     def operation_two(self):
#         return "Operation 2 from Subsystem Two"
#
#
# class Facade:
#     def __init__(self):
#         self.subsystem_one = SubsystemOne()
#         self.subsystem_two = SubsystemTwo()
#
#     def operation(self):
#         return (
#             self.subsystem_one.operation_one()
#             + ", "
#             + self.subsystem_two.operation_two()
#         )
#
#
# class TestFacadePattern(unittest.TestCase):
#     def test_facade(self):
#         facade = Facade()
#         self.assertEqual(
#             facade.operation(),
#             "Operation 1 from Subsystem One, Operation 2 from Subsystem Two",
#         )
#
#
# if __name__ == "__main__":
#     unittest.main()

#################################################################################
# pip3 install black

# Патерн итератор

# import unittest
#
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#
# class Group:
#     def __init__(self, students):
#         self.students = students
#
#     def __iter__(self):
#         self._index = 0
#         return self
#
#     def __next__(self):
#         if self._index < len(self.students):
#             result = self.students[self._index]
#             self._index += 1
#             return result
#         raise StopIteration
#
#
# class TestIteratorPattern(unittest.TestCase):
#     def test_iterator(self):
#         group = Group([Student("Alice"), Student("Bob"), Student("Charlie")])
#         students = [student.name for student in group]
#         self.assertEqual(students, ["Alice", "Bob", "Charlie"])
#
#
# if __name__ == "__main__":
#     unittest.main()

#################################################################################


