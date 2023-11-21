# ООП 2 урок - классы

# class Point:
#
#     MIN_COORD = 0  # Константа - практически не изменяются поэтому пишем капсом
#     MAX_COORD = 100  # Константа
#
#     def __init__(self, x, y):
#         self.set_coordinates(x, y)
#         # self.x = x
#         # self.y = y
#
#     @classmethod
#     def set_square(cls, left, right):
#         cls.MIN_COORD = left
#         cls.MAX_COORD = right
#
#     def set_coordinates(self, x, y):
#         if Point.MIN_COORD <= x <= Point.MAX_COORD and Point.MIN_COORD <= y <= Point.MAX_COORD:
#             self.x = x
#             self.y = y
#         else:
#             print('Точка лежит вне области!')
#
#     def __setattr__(self, key, value):
#         print('Сработал __setattr__')
#         if key == 'w':
#             raise ValueError('Недопустимое значение атрибута')
#         object.__setattr__(self, key, value)
#
#     def __getattribute__(self, item):
#         print('Сработал метод __getattribute__')
#         if item == 'x':
#             raise ValueError('У вас нет доступа к значению этого атрибута')
#         return object.__getattribute__(self, item)
#
#     def __str__(self):
#         return f'Координаты точки: x={self.x}, y={self.y}'
#
#
# point = Point(1, 2)
# print(point.x)
# print(point.y)
# point.x = 5
# point_1 = Point(3, 4)
# print(point_1.MIN_COORD, point_1.MAX_COORD)
# point.set_square(40, 80)
# print(Point.__dict__)
# print(point.MIN_COORD, point.MAX_COORD)
# point_1 = Point(1, 1)
# point_1.set_coordinates(1, 50)
# print(point_1)
# point_1.MIN_COORD = 50
# point_1.MAX_COORD = 150
# print(point_1.MIN_COORD)
# print(point_1.MAX_COORD)
#
# point_2 = Point(2, 2)
# print(point_2.MIN_COORD)
# print(point_2.MAX_COORD)

####################################################################

# Наследование в классах

class Employee:

    ID = 0
    TAX = 0.13

    def __init__(self, email, salary):
        Employee.ID += 1
        self.id = Employee.ID
        self.email = email
        self.salary = salary

    def get_salary_for_month(self, bonus=0):
        return self.salary - self.salary * self.TAX + bonus

    def __str__(self):
        return f'id: {self.id}, email: {self.email}, salary: {self.salary}'


class Manager(Employee):
    TAX = 0.1

    def __init__(self, email, salary, employees):
        super(Manager, self).__init__(email, salary)
        self.employees = employees

    def get_employees(self):
        if self.employees:
            for i_employees in self.employees:
                print(f'id: {i_employees.id}\nemail: {i_employees.email}\nsalary: {i_employees.salary}')

    def __str__(self):
        return f'id: {self.id}, email: {self.email}, ' \
         f'salary: {self.salary} \nEmployees: {self.employees[0].email}'


class Engineer(Employee):
    TAX = 0.13
    ONE_HOURS = 1500

    def __init__(self, email, rank, salary):
        super(Engineer, self).__init__(email, salary)
        self.rank = rank

    def get_salary(self, bonus=0):
        return self.salary - self.salary * self.TAX * self.ONE_HOURS + bonus

    @classmethod
    def rub_get_hour(cls):
        cls.ONE_HOURS = 8

    def __str__(self):
        return f'id: {self.id}, email: {self.email}, rank: {self.rank}, salary: {self.salary}'


employee_1 = Employee('test_1@mail.com', 10000)
print(employee_1)
print(employee_1.get_salary_for_month(1000))
employee_2 = Employee('test_2@mail.com', 20000)
print(employee_2)
print(employee_2.get_salary_for_month(2500))
manager_1 = Manager('boss@mail.com', 100000, [employee_1])
print(manager_1)
manager_1.get_employees()
engineer_1 = Engineer('enginer@mail.com',  '1st category specialist', 75000)
print(engineer_1)
engineer_1.get_salary()


