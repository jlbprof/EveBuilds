
import csv
import json
import os
import sys

def increment_qty_in_dict(dict, key, qty):
    if key not in dict:
        dict[key] = qty
    else:
        dict[key] = dict[key] + qty

def parse_inventory_line(line):
    parts = line.split()
    if parts and parts[-1].startswith('x') and parts[-1][1:].isdigit():
        item = " ".join(parts[:-1])
        qty = int(parts[-1][1:])
    else:
        item = line
        qty = 1
    return (item, qty)

def parse_fit_ship_name_line(line):
    # '[Armageddon, ʘ 4th Rate Linked]'
    line = line[1:-1]  # Remove brackets
    parts = line.split(", ")
    ship_type = parts[0]
    ship_name = parts[1]
    return (ship_type, ship_name)

def parse_line_update_dict(dict, line):
    (item, qty) = parse_inventory_line(line)
    increment_qty_in_dict(dict, item, qty)

def parse_fit(fit_path):
    if not os.path.exists(fit_path):
        raise Exception(f"Fit Path does not exist :{fit_path}:")
        
    with open(fit_path, 'r') as f:
        lines = f.read().splitlines()

    # First line contains ship type and ship name

    line = lines.pop(0)
    (ship_type, ship_name) = parse_fit_ship_name_line(line)

    print(f"SHIP LINE :{ship_type}: :{ship_name}:")

    # Now we have the low slots, until a space
    low_slots = {}
    while True:
        line = lines.pop(0)
        if line == "":
            break

        parse_line_update_dict(low_slots, line)

    mid_slots = {}
    while True:
        line = lines.pop(0)
        if line == "":
            break

        parse_line_update_dict(mid_slots, line)

    high_slots = {}
    while True:
        line = lines.pop(0)
        if line == "":
            break

        parse_line_update_dict(high_slots, line)

    rig_slots = {}
    while True:
        line = lines.pop(0)
        if line == "":
            break

        parse_line_update_dict(rig_slots, line)

    # 2 more empty lines, and then drones
    line = lines.pop(0)
    line = lines.pop(0)

    drones = {}
    while True:
        line = lines.pop(0)
        if line == "":
            break

        parse_line_update_dict(drones, line)

    # Now cargo
    cargo = {}
    while True:
        line = lines.pop(0)
        if line == "":
            break

        parse_line_update_dict(cargo, line)

    return { "type": ship_type, "name": ship_name, "high": high_slots, "low": low_slots, "mid": mid_slots, "rigs": rig_slots, "drones": drones, "cargo": cargo }

# 1 - Is a fit
# 2 - Is a recipe
# 999 - Error

def determine_if_fit_or_recipe(file_path):
    if not os.path.exists(file_path):
        return (999, "Cannot find file")

    with open(file_path, 'r') as f:
        first_line = f.readline().strip()

    first_char = first_line[0]

    if first_char == '[':
        return (1, "FIT")

    if first_char == '{':
        recipe_name = file_path.split('/')[-1].split('.')[0]
        return (2, recipe_name)

    return (999, "Unknown Type")

def recipe_exists(recipe_name):
    recipe_file = f"{recipe_name}.json"
    recipe_path = os.path.join('recipes', recipe_file)
    if not os.path.exists(recipe_path):
        return (0, recipe_path)
    return (1, recipe_path)

def load_recipe(recipe_name):
    (exists, recipe_path) = recipe_exists(recipe_name)
    with open(recipe_path, 'r') as f:
        recipe = json.load(f)

    return recipe

def load_categories(path):
    categories = {}
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                categories[row[0].strip()] = row[1].strip()

    return categories

def pretty_print(data):
    print(json.dumps(data, indent=4))

