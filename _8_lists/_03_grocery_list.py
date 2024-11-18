import sys


def welcome_message() -> None:
    """
    Prints the welcome message and a menu with the available options.
    """
    print("--- Welcome to the groceries ---")
    print("Enter : ")
    print("--------------------------------")
    print("1 - To add an item")
    print("2 - To remove an item")
    print("3 - To list all item")
    print("4 - To update existing item in list")
    print("0 - To exit the program")
    print("--------------------------------")


def add_item(item: str, groceries: list[str]) -> None:
    """
    Adds an item to the groceries list.
    
    Parameters:
        item (str): The item to be added.
        groceries (list[str]): The list of grocery items.
    """
    groceries.append(item)
    print(f"{item} - Added to the Groceries list")


def remove_item(item: str, groceries: list[str]) -> None:
    """
    Removes an item from the groceries list.
    
    Parameters:
        item (str): The item to be removed.
        groceries (list[str]): The list of grocery items.
    
    Raises:
        ValueError: If the item is not found in the list.
    """
    try:
        groceries.remove(item)
        print(f"{item} - Removed from the Groceries list")
    except ValueError:
        print("Item not founded!!")


def modify_list_item(item: str, groceries: list[str]) -> None:
    """
    Modifies an item in the groceries list.
    
    Parameters:
        item (str): The item to be modified.
        groceries (list[str]): The list of grocery items.
        
    Raises:
        ValueError: If the item is not found in the list.
    """
    try:
        groceries[groceries.index(item)] = input(f"Enter the item to replace with {item}: ").lower()
        print("Item replaced...")
    except ValueError:
        print("Item not founded!!")


def display(groceries: list[str]) -> None:
    """
    Displays the list of groceries.
    
    Parameters:
        groceries (list[str]): The list of grocery items.
    """
    print("--------------LIST--------------")
    for i, item in enumerate(groceries, 1):
        print(f"{i}. {item.capitalize()}")
    print("--------------------------------")


def is_an_option(text: str) -> bool:
    """
    Checks if the given text is a valid menu option.
    
    Parameters:
        text (str): The text to be checked.
        
    Returns:
        bool: True if the text is a valid option, False otherwise.
    """
    return text in ['1', '2', '3', '4', '0']


def main() -> None:
    """
    Main function to run the grocery list application.
    Presents a menu to the user and performs actions based on the user input.
    
    The available menu options are:
    1 - To add an item
    2 - To remove an item
    3 - To list all items
    4 - To update an existing item in the list
    0 - To exit the program
    """
    groceries: list[str] = []
    welcome_message()
    while True:
        user_input: str = input("Choose: ").lower()
        if not is_an_option(user_input):
            print("Please pick a valid option...")
            continue

        if user_input == '1':
            add_this = input("What you want to add ?: ").lower()
            if add_this == "":
                print("You have not added anything!! Try again.")
                continue
            add_item(add_this, groceries)
        elif user_input == '2':
            remove_this = input("What you want to remove ?: ").lower()
            remove_item(remove_this, groceries)
        elif user_input == '3':
            display(groceries)
        elif user_input == '4':
            update_item_with = input("What you want to be modified ?: ")
            modify_list_item(update_item_with, groceries)
        elif user_input == '0':
            print("Exiting program...")
            sys.exit()


if __name__ == '__main__':
    main()
