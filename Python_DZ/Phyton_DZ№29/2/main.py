# Создайте приложение для приготовления пасты. При-
# ложение должно уметь создавать минимум три вида па-
# сты. Классы различной пасты должны иметь следующие
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

class Pasta:
    def _init_(self, pasta_type, sauce, filling, toppings):
        self.pasta_type = pasta_type
        self.sauce = sauce
        self.filling = filling
        self.toppings = toppings

    def _str_(self):
        return f"Type: {self.pasta_type}\n" \
               f"Sauce: {self.sauce}\n" \
               f"Filling: {self.filling}\n" \
               f"Toppings: {', '.join(self.toppings)}\n"


class PastaFactory:
    def create_pasta(self, pasta_type):
        if pasta_type == "carbonara":
            return Pasta("Carbonara", "Cream sauce", "Bacon and eggs", "Parmesan cheese")
        elif pasta_type == "bolognese":
            return Pasta("Bolognese", "Tomato sauce", "Ground beef", "Parmesan cheese", "Basil")
        elif pasta_type == "alfredo":
            return Pasta("Alfredo", "Butter and cream sauce", "Chicken", "Mushrooms", "Peas")
        else:
            raise ValueError("Invalid pasta type")


pasta_factory = PastaFactory()

carbonara_pasta = pasta_factory.create_pasta("carbonara")
print(carbonara_pasta)

bolognese_pasta = pasta_factory.create_pasta("bolognese")
print(bolognese_pasta)

alfredo_pasta = pasta_factory.create_pasta("alfredo")
print(alfredo_pasta)
