#!/usr/bin/python3

import csv
import json
import math
import os
import sys

full_list = {}

def recipe_exists(recipe_name):
    recipe_file = f"{recipe_name}.json"
    recipe_path = os.path.join('recipes', recipe_file)
    if not os.path.exists(recipe_path):
        return (0, recipe_path)
    return (1, recipe_path)

def add_recipe(recipe_name, quantity):
    (exists, recipe_path) = recipe_exists(recipe_name)
    if exists == 0:
        return 0

    print(f"Recipe {recipe_name}:{quantity:,}")
    try:
        with open(recipe_path, 'r') as f:
            data = json.load(f)
        
        ingredients = data["ingredients"]
        output_quantity = data["output"]
       
        num_runs = int(math.ceil(quantity / output_quantity));

        required = {}
        for ing, qty in ingredients.items():
            print(f"CHECK {ing}:{qty:,}:{num_runs:,}")
            required[ing] = {
                'ingredient': ing,
                'qty': (qty * num_runs),
            }
        
        for value in required.values():
            ingredient = value["ingredient"]
            qty = value["qty"]

            has_recipe = add_recipe(ingredient, qty)
            if not has_recipe:
                print(f"Not recipe ({ingredient}) ({qty:,})")
                if not ingredient in full_list:
                    full_list[ingredient] = { "ingredient": ingredient, "qty": qty }
                else:
                    full_list[ingredient]["qty"] = full_list[ingredient]["qty"] + qty;
    except Exception as e:
        print(f"Exception {e}")
        sys.exit(1)

    return 1

def build_list(recipe_name, quantity):
    try:
        add_recipe(recipe_name, quantity)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 build_list.py <item_name> <quantity>")
        sys.exit(1)
    
    item_name = sys.argv[1]
    try:
        quantity = int(sys.argv[2])
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Quantity must be a positive integer.")
        sys.exit(1)

    categories = {}
    with open('categories.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                categories[row[0].strip()] = row[1].strip()

    build_list(item_name, quantity)

    lines = []
    for ingredient, value in full_list.items():
        ing = value["ingredient"]
        qty = value["qty"]
        category = categories.get(ing, "NotSet")

        line = f"{category},{ingredient},{qty:,}"
        lines.append(line)

    lines.sort()

    print("")
    print("")
    print(f"Ingredients List to build {quantity} {item_name}s")
    for line in lines:
        print(line)

