# import necessary modules

from typing import List  # used for type hints
import uuid  # generates unique identifiers for recipes
import operator  # used for string containment checks


# class representing a recipe with a unique ID, name, ingredients, instructions, and tags
class Recipe:
    # initializing function
    def __init__(
        self,
        name: str,
        ingredients: List[str],
        instructions: List[str],
        tags: List[str],
    ):
        self.uuid = str(uuid.uuid1())  # generate a unique identifier for the recipe
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.tags = tags

    # returns representational string of the object
    def __repr__(self):
        # formats a list of items as either bullet points or a numbered list
        def format_list(items: List[str], numbered: bool) -> str:
            if not items:
                return "  None"
            lines = []
            for i, item in enumerate(items):
                if numbered:
                    lines.append(f"    {i + 1}. {item}")  # numbered formatting
                else:
                    lines.append(f"    - {item}")  # bullet point formatting
            return "\n".join(lines)

        return (
            f"{{\n"
            f"  ID: {self.uuid}\n"
            f"  Recipe: {self.name}\n"
            f"  Ingredients:\n{format_list(self.ingredients, False)}\n"
            f"  Instructions:\n{format_list(self.instructions, True)}\n"
            f"  Tags:\n{format_list(self.tags, False)}\n"
            f"}}"
        )


# class representing a collection of recipes
class Cookbook:
    # initializing function
    def __init__(self, recipe_list: List[Recipe]):
        self.recipe_list = recipe_list

    # function that adds a new recipe to the cookbook
    def add_recipe(self, recipe: Recipe) -> None:
        self.recipe_list.append(recipe)

    # function that retrieves all recipes in the cookbook
    def get_recipes(self) -> List[Recipe]:
        return self.recipe_list

    # function that deletes a recipe from the cookbook based on its unique ID
    def delete_recipe(self, recipe_id: str) -> bool:
        for recipe in self.recipe_list:
            if recipe.uuid == recipe_id:
                recipe_index = self.recipe_list.index(recipe)
                self.recipe_list.pop(recipe_index)
                return True
        return False

    # function that searches for recipes that contain a given name substring
    def find_recipes(self, partial_recipe_name: str) -> None:
        found_recipe_list = []
        for recipe in self.recipe_list:
            if operator.contains(recipe.name.lower(), partial_recipe_name.lower()):
                found_recipe_list.append(recipe)
        if len(found_recipe_list) > 0:
            print("\nResults Found!\n")
            print(found_recipe_list)
        else:
            print("\nNo Results Found!\n")

    # function that searches for recipes that contain a specific tag
    def search_recipe_by_tag(self, tag_name: str) -> None:
        found_recipe_list = []
        for recipe in self.recipe_list:
            if recipe.tags.count(tag_name) > 0:
                found_recipe_list.append(recipe)
        if len(found_recipe_list) > 0:
            print("\nResults Found!\n")
            print(found_recipe_list)
        else:
            print("\nNo Results Found!\n")

    #  function that edits an existing recipe by ID, updating only provided fields
    def edit_recipe_by_id(
        self,
        recipe_id: str,
        new_name: str,
        new_ingredients: List[str],
        new_instructions: List[str],
        new_tags: List[str],
    ) -> None:
        recipe_index = -1
        for index, recipe in enumerate(self.recipe_list):
            if recipe.uuid == recipe_id:
                recipe_index = index
                break
        if len(new_name) > 0:
            self.recipe_list[recipe_index].name = new_name
        if len(new_ingredients) > 0:
            self.recipe_list[recipe_index].ingredients = new_ingredients
        if len(new_instructions) > 0:
            self.recipe_list[recipe_index].instructions = new_instructions
        if len(new_tags) > 0:
            self.recipe_list[recipe_index].tags = new_tags
