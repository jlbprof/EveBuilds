#!/usr/bin/python3

import math
import os
import sys

from utils import parse_fit, increment_qty_in_dict, load_recipe, recipe_exists, load_categories, pretty_print

full_list = {}
recipes   = {}

def add_fit_ingredients(ingredients, quantity):
    required = {}
    for ing, qty in ingredients.items():
        num = qty * quantity
        required[ing] = {
            'ingredient': ing,
            'qty': num,
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

def add_recipe(recipe_name, quantity):
    (exists, recipe_path) = recipe_exists(recipe_name)
    if exists == 0:
        return 0

    print(f"Recipe {recipe_name}:{quantity:,}")
    try:
        recipe = load_recipe(recipe_name)
        ingredients = recipe["ingredients"]
        output_quantity = recipe["output"]
       
        num_runs = int(math.ceil(quantity / output_quantity));
        increment_qty_in_dict(recipes, recipe_name, num_runs)
        print(f"ADDING TO RECIPES :{recipe_name}: :{num_runs}: :{recipes[recipe_name]}")
        print(f"Quantity :{quantity}: :{output_quantity}: :{num_runs}:")

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

def build_list(fit_path, quantity):
    myfit = parse_fit(fit_path) 

    recipe_name = myfit["type"]
    try:
        add_recipe(recipe_name, quantity)
        add_fit_ingredients(myfit["high"], quantity)
        add_fit_ingredients(myfit["mid"], quantity)
        add_fit_ingredients(myfit["low"], quantity)
        add_fit_ingredients(myfit["rigs"], quantity)
        add_fit_ingredients(myfit["drones"], quantity)
        add_fit_ingredients(myfit["cargo"], quantity)

    except Exception as e:
        print(f"Error: {e}")

def is_done(master_list, item):
    return master_list[item]["done"]

category_is_a_mat = { "Mineral": True, "Moon": True, "P1": True, "P2": True, "P3": True }

def is_item_a_mat(categories, item):
    if item in category_is_a_mat:
        return True

    # Also considered a mat, if no recipe exists for it.
    (exists, path) = recipe_exists(item)
    if not exists:
        return True

    return False

def material_blueprint_reaction(master_list, recipe):
    if is_item_a_mat(categories, recipe):
        return "Material"

    return master_list[recipe]["type"]

# This is complex, we want to know if all the materials or sub recipes are completed
# If so then we can print this recipe, otherwise we need to wait on this item

def are_all_ingredients_mats_or_done(master_list, item):
    recipe = master_list[item]["recipe"]
    ingredients = recipe["ingredients"]
    for ing in ingredients.keys():
        if not is_item_a_mat(categories, ing):
            if ing in master_list and not master_list[ing]["done"]:
                return False

    return True

def print_recipe_and_mark_done(recipe, master_list):
    ingredients = master_list[recipe]["recipe"]["ingredients"]
    xtype = master_list[recipe]["type"]
    qty = recipes[recipe]

    print(f"{xtype} {recipe} Number of runs: {qty}")
    for ing in ingredients.keys():
        num = ingredients[ing] * qty
        mat = material_blueprint_reaction(blueprint_report, ing)
        print(f"    {mat} {ing} {num}")

    print("")
    master_list[recipe]["done"] = True

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

    build_list(item_name, quantity)

    categories = load_categories("categories.csv")

    lines = []
    for ingredient, value in full_list.items():
        ing = value["ingredient"]
        qty = value["qty"]
        category = categories.get(ing, "Buy")

        line = f"{category},{ingredient},{qty:,}"
        lines.append(line)

    lines.sort()

    print("")
    print("==============================================================================")
    print("==============================================================================")
    print("==============================================================================")
    print("")
    print(f"Ingredients List to build {quantity} {item_name}")
    print("")

    for line in lines:
        print(line)

    # separate reactions and blueprints
    blueprint_report = {}

    for recipe in sorted(recipes.keys()):
        recipe_data = load_recipe(recipe)
        blueprint_report[recipe] = { "recipe": recipe_data, "done": False, "type": "Reaction" if recipe_data["type"] == "reaction" else "Blueprint" }

    print ("")
    print ("")
    print ("Perform the Blueprint/Reaction Runs in this order:")
    print ("")

    # The build report is very complex.
    #
    # We want to print out the items in order of buildability
    # Whereas item1 needs item2 built then we print item2 first then item1

    did_something = True
    while did_something:
        did_something = False

        for recipe in blueprint_report.keys():
            # We have already listed this recipe
            if is_done(blueprint_report, recipe):
                continue

            if are_all_ingredients_mats_or_done(blueprint_report, recipe):
                # We can do this one
                print_recipe_and_mark_done(recipe, blueprint_report)
                did_something = True

