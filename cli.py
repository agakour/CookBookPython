# imports
from cookbook import Recipe, Cookbook
from typing import List


# function that displays the main menu and processes user choices
def start_menu(my_cookbook: Cookbook) -> Cookbook:
    print("\n--Welcome to the COOKBOOK!--\n")
    # main loop that handles user actions
    while True:
        print("\nPress the required button and ENTER\n")
        print("a: ADD RECIPE\n")
        print("v: VIEW RECIPE LIST\n")
        print("f: FIND RECIPE\n")
        print("t: SEARCH BY TAGS\n")
        print("d: DELETE RECIPE BY ID\n")
        print("e: EDIT RECIPE BY ID\n")
        print("q: QUIT APP\n")
        menu_input = input()
        match menu_input:
            case "a":
                print("\nYou selected ADD RECIPE\n")
                user_recipe = get_recipe_input()
                my_cookbook.add_recipe(user_recipe)
            case "v":
                print("\nYou selected VIEW RECIPES\n")
                all_recipes = my_cookbook.get_recipes()
                if len(all_recipes) > 0:
                    print(all_recipes)
                else:
                    print("\nNo recipes found!\n")
            case "f":
                print("\nYou selected FIND RECIPE\n")
                input_recipe_name = get_partial_recipe_input()
                my_cookbook.find_recipes(input_recipe_name)
            case "t":
                print("\nYou selected SEARCH BY TAGS\n")
                input_tag_name = get_tag_input()
                my_cookbook.search_recipe_by_tag(input_tag_name)
            case "d":
                print("\nYou selected DELETE RECIPE BY ID\n")
                uuid = get_uuid_input()
                del_result = my_cookbook.delete_recipe(uuid)
                if del_result:
                    print(f"\nRecipe with ID: {uuid} Succefully Deleted!\n")
                else:
                    print(f"\nID: {uuid} NOT FOUND!\n")
            case "e":
                print("\nYou selected EDIT RECIPE BY ID\n")
                uuid = get_uuid_input()
                name, ingredients, instructions, tags = get_recipe_fields()
                my_cookbook.edit_recipe_by_id(
                    uuid, name, ingredients, instructions, tags
                )
            case "q":
                print("\nYou selected QUIT APP\n")
                return my_cookbook
            case _:
                print("\nEnter a VALID OPTION\n")


# function to collect user input and create a new Recipe object
def get_recipe_input() -> Recipe:
    name = ""
    ingredients = []
    instructions = []
    tags = []

    while True:
        name = input("\nGive me recipe name\n")
        if len(name) > 0:
            break
        else:
            print("\nRecipe name must not be empty\n")

    while True:
        ingredient = input("\nGive me an ingredient or type q to QUIT\n")
        if ingredient == "q":
            if len(ingredients) > 0:
                print("\nYou finished entering the ingredient list!\n")
                break
            else:
                print("\nIngredient list must not be empty!\n")
        else:
            ingredients.append(ingredient)

    while True:
        instruction = input("\nGive me an instruction or type q to QUIT\n")
        if instruction == "q":
            if len(instructions) > 0:
                print("\nYou finished entering the instruction list!\n")
                break
            else:
                print("\nInstruction list must not be empty!\n")
        else:
            instructions.append(instruction)

    while True:
        tag = input("\nGive me a tag or type q to QUIT\n")
        if tag == "q":
            print("\nYou finished entering the tag list!\n")
            break
        else:
            tags.append(tag.lower())

    input_recipe = Recipe(name, ingredients, instructions, tags)
    return input_recipe


# function to get a recipe's UUID from the user
def get_uuid_input() -> str:
    recipe_uuid = input("\nGive the UUID\n")
    return recipe_uuid


# function to get part of a recipe name for searching
def get_partial_recipe_input() -> str:
    partial_input = input("\nGive me Recipe Name\n")
    return partial_input


# function to get a tag name for searching recipes by tag
def get_tag_input() -> str:
    tag_input = input("\nGive me a Tag\n")
    return tag_input.lower()


# function to get user input for editing a recipe
def get_recipe_fields() -> tuple[str, List[str], List[str], List[str]]:
    name = ""
    ingredients = []
    instructions = []
    tags = []
    while True:
        print("\nPress the required button and ENTER\n")
        print("n: EDIT NAME\n")
        print("w: EDIT INGREDIENTS\n")
        print("i: EDIT INSTRUCTIONS\n")
        print("t: EDIT TAGS\n")
        print("q: QUIT EDITING\n")
        edit_input = input()
        match edit_input:
            case "n":
                print("You selected EDIT NAME\n")
                while True:
                    name = input("\nGive me recipe name\n")
                    if len(name) > 0:
                        break
                    else:
                        print("\nName must not be empty\n")
            case "w":
                print("You selected EDIT INGREDIENTS\n")
                while True:
                    ingredient = input("\nGive me an ingredient or type q to QUIT\n")
                    if ingredient == "q":
                        if len(ingredients) > 0:
                            print("\nYou finished entering the ingredient list!\n")
                            break
                        else:
                            print("\nIngredient list must not be empty!\n")
                    else:
                        ingredients.append(ingredient)
            case "i":
                print("You selected EDIT INSTRUCTIONS\n")
                while True:
                    instruction = input("\nGive me an instruction or type q to QUIT\n")
                    if instruction == "q":
                        if len(instructions) > 0:
                            print("\nYou finished entering the instruction list!\n")
                            break
                        else:
                            print("\nInstruction list must not be empty!\n")
                    else:
                        instructions.append(instruction)
            case "t":
                print("You selected EDIT TAGS\n")
                while True:
                    tag = input("\nGive me a tag or type q to QUIT\n")
                    if tag == "q":
                        print("\nYou finished entering the tag list!\n")
                        break
                    else:
                        tags.append(tag.lower())
            case "q":
                print("You selected QUIT EDITING\n")
                break
            case _:
                print("Enter a VALID OPTION\n")

    input_tuple = (name, ingredients, instructions, tags)
    return input_tuple
