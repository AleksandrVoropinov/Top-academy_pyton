# Задание 2
# Создайте класс Рецепт. Необходимо хранить следу-
# ющую информацию:
# ■ название рецепта;
# ■ автор рецепта;
# ■ тип рецепта (первое, второе блюдо и т.д.);
# ■ текстовое описание рецепта;
# ■ ссылка на видео с рецептом;
# ■ список ингредиентов;
# ■ название кухни (итальянская, французская, украин-
# ская и т.д.).
# Создайте необходимые методы для этого класса. Ре-
# ализуйте паттерн MVC для класса Рецепт и код для ис-
# пользования модели, контроллера и представления.

class Recipe:
    def __init__(self, name, author, type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.type = type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine


class RecipeController:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe
        return None


class RecipeView:
    def print_recipe(self, recipe):
        print(f"Name: {recipe.name}")
        print(f"Author: {recipe.author}")
        print(f"Type: {recipe.type}")
        print(f"Description: {recipe.description}")
        print(f"Video Link: {recipe.video_link}")
        print("Ingredients:")
        for ingredient in recipe.ingredients:
            print(f" - {ingredient}")
        print(f"Cuisine: {recipe.cuisine}")


recipe = Recipe("Carbonara Pasta", "John Doe", "Main Dish",
                "Creamy pasta with bacon and eggs", "https://www.youtube.com/watch?v=video_id",
                ["pasta", "bacon", "eggs", "parmesan cheese"], "Italian")

recipe_controller = RecipeController()
recipe_controller.add_recipe(recipe)

recipe_view = RecipeView()

recipe_name = "Carbonara Pasta"
found_recipe = recipe_controller.get_recipe(recipe_name)
if found_recipe:
    recipe_view.print_recipe(found_recipe)
else:
    print(f"No recipe found with name: {recipe_name}")
