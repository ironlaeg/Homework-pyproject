import os

def read_recipes(file_name):

    recipes = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            dish_name = line
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            recipes[dish_name] = ingredients
    return recipes


def print_recipes(recipes):

    for dish, ingredients in recipes.items():
        print(f"Блюдо: {dish}")
        print("Ингредиенты:")
        for ingredient in ingredients:
            print(f"  - {ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}")
        print()

file_name = 'Recipes.txt'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)
except FileNotFoundError:
    print(f"Файл {file_name} не найден.")
except Exception as e:
    print(f"Ошибка: {e}")

# Последний код написала нейронка, так как я не понимаю почему не открывается файл без этого кода