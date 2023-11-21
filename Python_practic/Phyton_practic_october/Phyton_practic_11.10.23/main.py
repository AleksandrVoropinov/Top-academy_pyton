# Объектно ориентированное программирование - ООП

# import random
# import time


# class Vehicle:  # Наименование класса всегда с большой буквы
#
#     def __init__(self, name: str, weight: float, hp: int, max_speed: int):
#         self.name = name
#         self.weight = weight
#         self.hp = hp
#         self.__wheel_count = 4
#         self.fuel = 5
#         self.max_speed = max_speed
#         self.__possible_failures = ['Дерево', 'Столб', 'Обрыв']

#     def output_info(self):
#         print(f'Информация о машине: {self.name}\n'
#               f'Масса: {self.weight}\n'
#               f'Л.с.: {self.hp}')
#     @staticmethod
#     def refuel(litters: float):
#         print(f'Машина заправлена на {litters} литров')
#
#     def refuel(self, liters: float):
#         self.fuel += liters
#         print(f'Машина заправлена на {liters} литров')
#         print(f'Сейчас уровень топлива равен: {self.fuel}')
#
#     def drive(self, km):
#         self.fuel -= km * 0.1
#         if self.fuel <= 0:
#             print('Нужно заправиться!')
#             choice = int(input('На сколько заправиться?'))
#             self.refuel(choice)
#         print(f'В баке осталось {self.fuel} литров')
#
#     def boost(self):
#         start = time.time()
#         if self.max_speed >= 100:
#             time.sleep(3.5)
#             print(f'Разгон до 100 км/ч {start}')
#             if self.max_speed >= 200:
#                 time.sleep(6.5)
#                 print(f'Разгон до 200 км/ч {start}')
#         print(f'Разгон до максимальной скорости {self.max_speed} равен {start} сек.')

#     def boost(self):
#         cur_time = 0
#         for i in range(0, self.max_speed, 20):
#             if random.randint(1, 10) == 5:
#                 print(f'Вы встретили припятствие {random.choice(self.__possible_failures)} при разгоне')
#                 return
#             cur_time += 0.5
#             time.sleep(0.5)
#             print(f'Текущая скорость {i} км/ч')
#         print(f'Машина {self.name} достигла максимальной скорости {self.max_speed} км/ч')
#
#     def __str__(self):
#         return f'Информация о машине: {self.name}\n'\
#                f'Масса: {self.weight}\n'\
#                f'Л.с.: {self.hp}\n' \
#                f'Расход топлива: {self.fuel} л.\n'\
#                f'Кол-во колес: {self.__wheel_count} шт.'
#
#
# vehicle_1 = Vehicle(name='Audi', weight=2000, hp=500, max_speed=200)
# vehicle_2 = Vehicle(name='BMW', weight=2150, hp=480, max_speed=230)

# print(vehicle_1, vehicle_2)
# print(vehicle_1.name)

# vehicle_1.output_info()
# vehicle_2.output_info()

# print(id(vehicle_2), id(vehicle_1))
# print(f'{vehicle_1}\n{vehicle_2}')
# __wheel_count - __ Категорически нельзя его изменять и обращатся вне класса

# vehicle_1.max_speed = 100
# print(f'Макс. скорость: {vehicle_1.max_speed}')

# vehicle_1.refuel(10)
# vehicle_2.refuel(12)
# vehicle_1.drive(100)
# vehicle_2.drive(90)
# vehicle_1.boost()
# vehicle_2.boost()

#################################################################################

# Задание 1

# class Human:
#
#     def __init__(self, fullname: str, birth_day: str, tel: str, city: str, country: str):
#         self.fullname = fullname
#         self.birth_day = birth_day
#         self.tel = tel
#         self.city = city
#         self.country = country
#
#     def set_fullname(self, value):
#         self.fullname = value
#
#     def set_birth_day(self):
#         return self.birth_day
#
#     def set_tel(self):
#         return self.tel
#
#     def set_city(self):
#         return self.city
#
#     def set_country(self):
#         return self.country
#
# human = Human(fullname='Ivan', birth_day='11.06.2001', tel=+79993214823, city='Moscow', country='Russian')
# print(human.set_fullname)

#################################################################################

# import random
# 
#
# class Student:
#
#     def __init__(self, fullname: str, group_num: str, mark_list: list[int]):
#         self.fullname = fullname
#         self.group_num = group_num
#         self.mark_list = mark_list
#
#     def get_avg_mark(self) -> float:
#         return sum(self.mark_list) / len(self.mark_list)
#
#     def __str__(self):
#         return f'{self.fullname} {self.group_num} {self.get_avg_mark()}'
#
#
# students = [
#     Student('Ivan', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#     Student('Alex', 'P-2', [random.randint(1, 5) for _ in range(5)]),
#     Student('Irina', 'P-3', [random.randint(1, 5) for _ in range(5)]),
#     Student('Semen', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#     Student('Damir', 'P-2', [random.randint(1, 5) for _ in range(5)]),
#     Student('Ylia', 'P-3', [random.randint(1, 5) for _ in range(5)]),
#     Student('Anna', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#     Student('Petr', 'P-3', [random.randint(1, 5) for _ in range(5)]),
# ]

# sorted_students = sorted(students, key=lambda x: x.get_avg_mark())
# sorted_students = sorted(students, key=lambda x: x.group_num[2])
# sorted_students = sorted(students, key=lambda x: x.fullname[0])
#
# for i_student in sorted_students:
#     print(i_student)
