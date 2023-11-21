# Магические методы классов

# class MyZeroDivisionError(ZeroDivisionError):
#     def __init__(self, message=''):
#         self.message = message
#
#
# def divide(a, b):
#     # try:
#     #     return a / b
#     # except ZeroDivisionError:
#     #     raise MyZeroDivisionError
#     #     # return f'Делить на ноль нельзя!'
#     # except MyZeroDivisionError as error:
#     #     print(error.message)
#     #     return error.message
#     # raise MyZeroDivisionError('Деление на 0!')
#     try:
#         if b == 0:
#             raise MyZeroDivisionError('Деление на 0!')
#         else:
#             return a / b
#     except MyZeroDivisionError as error:
#         return error
#
#
# print(divide(10, 0))

###############################################################

# class Vehicle:
#     def __init__(self, weight):
#         self.weight = weight
#
#
# class Ship(Vehicle):
#     pass
#
#
# base_vehicle = Vehicle(1000)
# ship = Ship(1000)

# print(isinstance(base_vehicle, Vehicle))
# print(issubclass(Ship, Vehicle))

###############################################################

# class Multiple:
#     def __init__(self, num_1, num_2):
#         self.num_1 = num_1
#         self.num_2 = num_2
#
#     def __call__(self, *args, **kwargs):
#         print(f'Hi {kwargs["name"]}')
#         return self.num_1 * self.num_2
#
#
# multiple = Multiple(10, 15)
# result = multiple(name='Smith')
# print(result)

###############################################################

# Перегрузка арифметических операторов

# class Number:
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number + other.number)
#         else:
#             return f'Сложение невозможно!'
#
#     def __sub__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number - other.number)
#         else:
#             return f'Вычетание невозможно!'
#
#     def __mul__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number * other.number)
#         else:
#             return f'Умножение невозможно!'
#
#     def __truediv__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number / other.number)
#         else:
#             return f'Деление невозможно!'
#
#     def __eq__(self, other):
#         if isinstance(other, Number):
#             return self.number == other.number
#         else:
#             return f'Сравнение невозможно!'
#
#     def __gt__(self, other):
#         if isinstance(other, Number):
#             return self.number > other.number
#         else:
#             return f'Сравнение невозможно!'
#
#     def __ge__(self, other):
#         if isinstance(other, Number):
#             return self.number >= other.number
#         else:
#             return f'Сравнение невозможно!'
#
#     def __lt__(self, other):
#         if isinstance(other, Number):
#             return self.number < other.number
#         else:
#             return f'Сравнение невозможно!'
#
#     def __le__(self, other):
#         if isinstance(other, Number):
#             return self.number <= other.number
#         else:
#             return f'Сравнение невозможно!'
#
#     def __ne__(self, other):
#         if isinstance(other, Number):
#             return self.number != other.number
#         else:
#             return f'Сравнение невозможно!'
#
#
# number_1 = Number(10)
# number_2 = Number(11)
# print(number_2 == number_1)
# print(number_2 > number_1)
# print(number_2 >= number_1)
# print(number_2 < number_1)
# print(number_2 <= number_1)
# print(number_2 != number_1)
# number_3 = Number(12)
# result = number_1 + number_2 + number_3
# print(result.number)

###############################################################

# Корзина интернет магазина

class Product:
    def __init__(self, name, price, quantity, shop, discount=0.0):
        self.name = name
        self.price = price
        self. quantity = quantity
        self.shop = shop
        self.discount = discount

    def get_total_product_price(self):
        return self.price * self.quantity - (self.price * (1 - self.discount))


class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name


class Cart:
    def __init__(self):
        self.cart = []

    def __add__(self, other):
        if isinstance(other, Cart):
            # merge_cart = Cart()
            # merge_cart.cart = self.cart + other.cart
            # return merge_cart
            self.cart += other.cart
            return self
        return 'Невозможно произвести слияние корзины!'

    def add_product(self, *args):
        for i_product in args:
            self.cart.append(i_product)

    def get_all_products_in_cart(self):
        print('Товары в корзине: \n'
              f'{"":-^25}')
        for i_product in self.cart:
            print(f'Магазин: {i_product.shop.shop_name}\n'
                  f'\tНазвание: {i_product.name}\n'
                  f'\tЦена: {i_product.price}\n'
                  f'\tСкидка: {i_product.discount}\n'
                  f'\tКол-во: {i_product.quantity}\n'
                  f'\tОбщая стоимость: {i_product.get_total_product_price()}\n'
                  f'{"":-^25}')
        print(f'Общая стоимость товаров в корзине: {self.get_total_card_amount()}\n'
              f'{"":-^25}')

    def get_total_card_amount(self):
        total_price = sum([i_product.get_total_product_price() for i_product in self.cart])
        return total_price


shop_1 = Shop('Magnit')
shop_2 = Shop('Ozon')
shop_3 = Shop('Monetka')
shop_4 = Shop('Global')


cart_1 = Cart()
cart_1.add_product(Product('apple', 100, 5, shop_1, 0.5), Product('Oil', 125, 3, shop_2))
# cart_1.get_all_products_in_cart()

cart_2 = Cart()
cart_2.add_product(Product('banana', 120, 4, shop_3), Product('snake', 1250, 2, shop_4))
# cart_2.get_all_products_in_cart()

cart_1 += cart_2
cart_1.get_all_products_in_cart()
del cart_2

# cart_3 = cart_1 + cart_2
# cart_3.get_all_products_in_cart()



