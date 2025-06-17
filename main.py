# import necessary functions from other modules

from cli import start_menu  # handles user interaction via the command line interface
from storage import (
    save_cookbook,
    load_cookbook,
)  # functions to load and save cookbook data


# entry point of the program
# main function to load the cookbook, interact with the user, and save changes
def main() -> None:
    # inform the user that the program has started
    print("This is the entry point of the program.\n")
    # load existing cookbook data from storage
    loaded_cookbook = load_cookbook()
    # start the command-line interface and allow the user to modify the cookbook
    final_cookbook = start_menu(loaded_cookbook)
    # save the modified cookbook back to storage
    save_cookbook(final_cookbook)
    # display a closing message to the user
    print("Thanks for using this program!\n")


# run main function if main.py is executed directly
if __name__ == "__main__":
    main()
