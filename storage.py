# imports
import json
from cookbook import Cookbook, Recipe

# define the JSON file used for storing cookbook data
JSON_FILE = "store.json"


# function that saves the user's cookbook to a JSON file
# converts the Cookbook object into a JSON-compatible format and writes it to a file for persistent storage
def save_cookbook(user_cookbook: Cookbook) -> None:
    cookbook_dict = json.dumps(user_cookbook, default=lambda obj: obj.__dict__)
    with open(JSON_FILE, "w") as outfile:
        outfile.write(cookbook_dict)
    print("\nSaved cookbook to JSON file!\n")


# loads the cookbook from a JSON file
# If the file exists, it reads the data and reconstructs the Cookbook and Recipe objects
# If the file is missing,it returns an empty Cookbook
def load_cookbook() -> Cookbook:
    new_cookbook = Cookbook([])
    try:
        with open(JSON_FILE, "r") as infile:
            cookbook_dict = json.load(infile)
    except FileNotFoundError:
        print("\nNo existing file found!")
        return new_cookbook

    for recipe_dict in cookbook_dict["recipe_list"]:
        new_recipe = Recipe(
            recipe_dict["name"],
            recipe_dict["ingredients"],
            recipe_dict["instructions"],
            recipe_dict["tags"],
        )
        new_recipe.uuid = recipe_dict["uuid"]
        new_cookbook.add_recipe(new_recipe)

    print("\nLoaded cookbook from JSON file!\n")

    return new_cookbook
