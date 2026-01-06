#!/usr/bin/python3

import json
import os

def validate_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)

                if "type" not in data:
                    raise Exception(f"{filepath} does not have a 'type' key")

                xtype = data["type"]
                if xtype != "manufacture" and xtype != "reaction":
                    raise Exception(f"{filepath} invalid type :{xtype}:")

                if "output" not in data:
                    raise Exception(f"{filepath} does not have a 'output' key")

                output = data["output"]
                if not isinstance(output, int):
                    raise Exception(f"{filepath} output :{output}: is not an integer")

                if "ingredients" not in data:
                    raise Exception(f"{filepath} does not have a 'ingredients' key")

                ingredients = data["ingredients"]
                if len(ingredients) <= 0:
                    raise Exception(f"{filepath} has an empty 'ingredients' list")

                for key, value in ingredients.items():
                    if not isinstance(value, int):
                        raise Exception(f"{filepath} ingredient {key} is not an integer")
                        
                print(f"{filename}: Valid")
            except json.JSONDecodeError as e:
                print(f"{filename}: Invalid - {e}")
            except Exception as e:
                print(f"{filename}: Error - {e}")

if __name__ == "__main__":
    recipes_dir = 'recipes'
    validate_json_files(recipes_dir)
