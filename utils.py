
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

