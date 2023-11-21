# Задание 1
# Создайте класс Обувь. Необходимо хранить следую-
# щую информацию:
# ■ тип обуви;
# ✓ мужская,
# ✓ женская;
# ■ вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.);
# ■ цвет;
# ■ цена;
# ■ производитель;
# ■ размер.
# Создайте необходимые методы для этого класса. Реа-
# лизуйте паттернMVC для класса Обувь и код для исполь-
# зования модели, контроллера и представления.

class Shoe:
    def __init__(self, shoe_type, gender, shoe_style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.gender = gender
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size


class ShoeController:
    def __init__(self):
        self.shoe_models = []

    def add_shoe(self, shoe):
        self.shoe_models.append(shoe)

    def remove_shoe(self, shoe):
        self.shoe_models.remove(shoe)

    def get_shoe_by_gender(self, gender):
        return [shoe for shoe in self.shoe_models if shoe.gender == gender]

    def get_shoe_by_price(self, price):
        return [shoe for shoe in self.shoe_models if shoe.price == price]

    def get_shoe_by_manufacturer(self, manufacturer):
        return [shoe for shoe in self.shoe_models if shoe.manufacturer == manufacturer]


class ShoeView:
    @staticmethod
    def display_shoes(shoes):
        print("Shoes:")
        for shoe in shoes:
            print(f"- Type: {shoe.shoe_type}\n Gender: {shoe.gender}\n Style: {shoe.shoe_style}\n Color: {shoe.color}\n"
                  f" Price: {shoe.price}\n Manufacturer: {shoe.manufacturer}\n Size: {shoe.size}")
        print()


controller = ShoeController()

shoe1 = Shoe("Sports", "Men", "Sneakers", "Black", 99.99, "Nike", 10)
shoe2 = Shoe("Casual", "Women", "Sandals", "White", 49.99, "Adidas", 8)
shoe3 = Shoe("Formal", "Men", "Oxfords", "Brown", 149.99, "Gucci", 9)

controller.add_shoe(shoe1)
controller.add_shoe(shoe2)
controller.add_shoe(shoe3)

male_shoes = controller.get_shoe_by_gender("Men")
ShoeView.display_shoes(male_shoes)

adidas_shoes = controller.get_shoe_by_manufacturer("Adidas")
ShoeView.display_shoes(adidas_shoes)

controller.remove_shoe(shoe1)

female_shoes = controller.get_shoe_by_gender("Women")
ShoeView.display_shoes(female_shoes)
