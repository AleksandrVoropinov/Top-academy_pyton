# Создайте реализацию паттерна Prototype. Протести-
# руйте работу созданного класса.

import copy


class Car:
    def _init_(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def _str_(self):
        return f"{self.make} {self.model} {self.color}"

    def clone(self):
        return copy.deepcopy(self)


# Создаем первый автомобиль
car1 = Car("Toyota", "Corolla", 2021, "blue")
print("Original Car: ", car1)

# Клонируем автомобиль
car2 = car1.clone()

# Изменяем цвет второго автомобиля
car2.color = "red"
print("Cloned Car: ",car2)
