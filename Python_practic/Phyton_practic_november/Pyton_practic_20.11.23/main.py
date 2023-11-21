# Паттерны MVC

# class ArticleModel:
#     def __init__(self, title, author, num_characters, publication, description):
#         self.title = title
#         self.author = author
#         self.num_characters = num_characters
#         self.publication = publication
#         self.description = description
#
#
# class ArticleView:
#     @staticmethod
#     def display_article(article):
#         print(f"Title: {article.title}")
#         print(f"Author: {article.author}")
#         # More print statements for other attributes
#
#
# class ArticleController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#
#     def set_article_title(self, title):
#         self.model.title = title
#
#     # More methods to modify the model
#
#     def display_article(self):
#         self.view.display_article(self.model)


##################################################################################

# class FilmModel:
#     def __init__(self, title, genre, director, release_year, duration, studio, actors):
#         self.title = title
#         # More attributes...
#
#
# class FilmView:
#     @staticmethod
#     def display_film(film):
#         ...
#
#
# class FilmController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#         ...
#
#     def display_film(self):
#         self.view.display_film(self.model)

##################################################################################

# class Pizza:
#     def __init__(self, name):
#         self.name = name
#         self.toppings = []
#
#     def add_topping(self, topping):
#         self.toppings.append(topping)
#
#     def get_description(self):
#         toppings_description = ', '.join(self.toppings) if self.toppings else 'without toppings'
#         return f"Pizza '{self.name}' with toppings: {toppings_description}"
#
#
# class Order:
#     def __init__(self):
#         self.pizzas = []
#         self.status = "In Progress"
#
#     def add_pizza(self, pizza):
#         self.pizzas.append(pizza)
#
#     def calculate_total(self):
#         # More complex logic for calculating cost can be added here
#         return 100 * len(self.pizzas)
#
#     def complete_order(self):
#         self.status = "Completed"
#         return f"Order completed. Total cost: {self.calculate_total()} rub."
#
#
# class Payment:
#     @staticmethod
#     def process_payment(amount):
#         print(f"Payment of {amount} rub. successfully processed.")
#
#
# class Report:
#     @staticmethod
#     def generate_sales_report(orders):
#         total_sales = sum(order.calculate_total() for order in orders)
#         print(f"Total sales volume: {total_sales} rub.")
#
#
# # Creating pizzas
# margherita = Pizza("Margherita")
# margherita.add_topping("Mozzarella")
# margherita.add_topping("Tomatoes")
#
# pepperoni = Pizza("Pepperoni")
# pepperoni.add_topping("Pepperoni")
# pepperoni.add_topping("Mozzarella")
#
# # Creating an order
# order = Order()
# order.add_pizza(margherita)
# order.add_pizza(pepperoni)
#
# # Payment process
# Payment.process_payment(order.calculate_total())
#
# # Completing the order
# print(order.complete_order())
#
# # Generating a report
# Report.generate_sales_report([order])

##################################################################################

# Создать класс

# import unittest
# from fractions import Fraction
#
#
# class FractionCalculator:
#
#     def __init__(self, numerator, denominator):
#         self.fraction = Fraction(numerator, denominator)
#
#     def add(self, other):
#         return self.fraction + other.fraction
#
#     def sub(self, other):
#         return self.fraction - other.fraction
#
#     def multiplication(self, other):
#         return self.fraction * other.fraction
#
#     def division(self, other):
#         return self.fraction / other.fraction
#
#
# class TestFractionCalculator(unittest.TestCase):
#
#     def test_add(self):
#         frac1 = FractionCalculator(1, 2)
#         frac2 = FractionCalculator(1, 4)
#         self.assertEqual(frac1.add(frac2), Fraction(3, 4))
#
#     def test_sub(self):
#         frac1 = FractionCalculator(1, 2)
#         frac2 = FractionCalculator(1, 4)
#         self.assertEqual(frac1.dub(frac2), Fraction(3, 4))
#
#     def test_multiplication(self):
#         frac1 = FractionCalculator(1, 2)
#         frac2 = FractionCalculator(1, 4)
#         self.assertEqual(frac1.multiplication(frac2), Fraction(3, 4))
#
#     def test_division(self):
#         frac1 = FractionCalculator(1, 2)
#         frac2 = FractionCalculator(1, 4)
#         self.assertEqual(frac1.division(frac2), Fraction(3, 4))
#
#
# if __name__ == "main":
#     unittest.main()

##################################################################################

import unittest


class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")

    def maximum(self, num1, num2):
        return max(num1, num2)

    def minimum(self, num1, num2):
        return min(num1, num2)

    def percentage(self, num, percent):
        return (num * percent) / 100

    def exponent(self, num, pow):
        return num ** pow


class CalculatorTest(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        result = calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_sub(self):
        calculator = Calculator()
        result = calculator.sub(5, 1)
        self.assertEqual(result, 4)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        calculator = Calculator()
        result = calculator.multiply(9, 3)
        self.assertEqual(result, 3)

    def test_division_by_zero(self):
        calculator = Calculator()
        with self.assertRaises(ValueError):
            calculator.division(8, 0)

    def test_max(self):
        calculator = Calculator()
        result = calculator.maximum(9, 3)
        self.assertEqual(result, 9)

    def test_min(self):
        calculator = Calculator()
        result = calculator.minimum(9, 3)
        self.assertEqual(result, 3)

    def test_percentage(self):
        calculator = Calculator()
        result = calculator.percentage(50, 20)
        self.assertEqual(result, 10)

    def test_exponent(self):
        calculator = Calculator()
        result = calculator.exponent(2, 4)
        self.assertEqual(result, 16)


if __name__ == "main":
    unittest.main()






