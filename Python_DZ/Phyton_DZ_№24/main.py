# Задание 1
# Создать базовый класс Фигура с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади.

class Figure:
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Trapezoid(Figure):
    def __init__(self, base_1, base_2, height_1):
        self.base_1 = base_1
        self.base_2 = base_2
        self.height_1 = height_1

    def area(self):
        return 0.5 * (self.base_1 + self.base_2) * self.height_1


rectangle = Rectangle(5, 10)
rectangle_1 = rectangle.area()
print(f'Площадь прямоугольника: {rectangle_1}')

circle = Circle(7)
circle_1 = circle.area()
print(f'Площадь круга: {circle_1}')

triangle = RightTriangle(4, 6)
triangle_1 = triangle.area()
print(f'Площадь прямоугольного треугольника: {triangle_1}')

trapezoid = Trapezoid(3, 5, 8)
trapezoid_1 = trapezoid.area()
print(f'Площадь трапеции: {trapezoid_1}')
