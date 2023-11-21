# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
# ■ Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне са-
# молета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возмож-
# ному количеству пассажиров на борту (операции >
# < <= >=).

# class Airplane:
#     def __init__(self, passengers):
#         self.passengers = passengers
#
#     def __eq__(self, other):
#         if isinstance(other, Airplane):
#             return self.passengers == other.passengers
#         else:
#             return f'Сравнение невозможно!'
#
#     def __add__(self, num_passengers):
#         self.passengers += num_passengers
#         return self
#
#     def __sub__(self, num_passengers):
#         self.passengers -= num_passengers
#         return self
#
#     def __iadd__(self, num_passengers):
#         self.passengers += num_passengers
#         return self
#
#     def __isub__(self, num_passengers):
#         self.passengers -= num_passengers
#         return self
#
#     def __gt__(self, other):
#         if isinstance(other, Airplane):
#             return self.passengers > other.passengers
#         else:
#             return f'Сравнение невозможно!'
#
#     def __lt__(self, other):
#         if isinstance(other, Airplane):
#             return self.passengers < other.passengers
#         else:
#             return f'Сравнение невозможно!'
#
#     def __le__(self, other):
#         if isinstance(other, Airplane):
#             return self.passengers <= other.passengers
#         else:
#             return f'Сравнение невозможно!'
#
#     def __ge__(self, other):
#         if isinstance(other, Airplane):
#             return self.passengers >= other.passengers
#         else:
#             return f'Сравнение невозможно!'
#
#
# airplane_1 = Airplane(100)
# airplane_2 = Airplane(150)
#
# print(airplane_1 == airplane_2)
#
# airplane_1 += 50
# print(airplane_1.passengers)
#
# airplane_2 -= 50
# print(airplane_2.passengers)
#
# print(airplane_1 > airplane_2)
# print(airplane_1 < airplane_2)
# print(airplane_1 <= airplane_2)
# print(airplane_1 >= airplane_2)


# Задание 4
# Создать класс Flat (квартира). Реализовать перегру-
# женные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (опера-
# ция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).

class Flat:
    def __init__(self, apartment_area, apartment_price):
        self.apartment_area = apartment_area
        self.apartment_price = apartment_price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.apartment_area == other.apartment_area
        else:
            return f'Сравнение невозможно!'

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.apartment_area != other.apartment_area
        else:
            return f'Сравнение невозможно!'

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.apartment_price > other.apartment_price
        else:
            return f'Сравнение невозможно!'

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.apartment_price < other.apartment_price
        else:
            return f'Сравнение невозможно!'

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.apartment_price <= other.apartment_price
        else:
            return f'Сравнение невозможно!'

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.apartment_price >= other.apartment_price
        else:
            return f'Сравнение невозможно!'


apartment_1 = Flat(93, 7200000)
apartment_2 = Flat(54, 5500000)

print(apartment_1.apartment_area == apartment_2.apartment_area)
print(apartment_1.apartment_area != apartment_2.apartment_area)
print(apartment_1.apartment_price > apartment_2.apartment_price)
print(apartment_1.apartment_price < apartment_2.apartment_price)
print(apartment_1.apartment_price <= apartment_2.apartment_price)
print(apartment_1.apartment_price >= apartment_2.apartment_price)
