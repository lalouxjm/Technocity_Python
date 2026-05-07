from pathlib import Path

import my_func

grocery_file = Path('groceries.txt')

def load_grocery():
    groceries = []

    if not grocery_file.exists():
        print(my_func.red('Grocery file not found.'))
        return groceries
    with open(grocery_file,'r') as file:
        for line in file:
            item = line.strip()

            if item:
                groceries.append(item)
    return groceries
groceries = load_grocery()

def save_groceries(groceries):
    with open(grocery_file,'w') as file:
        for item in groceries:
            file.write(item+"\n")
    print(my_func.green("Grocery list saved!"))

def show_list(g):
    print(my_func.blue("===Grocery List==="))

    if not g:
        print(my_func.red("No groceries!"))
    else:
        for i, item in enumerate(g, start=1):
            print(f"{i}. {item}")

def add_item(g):
    print(my_func.blue("===Add item==="))
    new_item = input("What do you want to add?")
    if new_item in g:
        print(my_func.red(f'You already have {new_item} in your list!'))
    else:
        g.append(new_item.lower())
        print(my_func.blue(f"{new_item} is added to your list!"))

def remove_item(g):
    print(my_func.blue("===Remove item==="))
    removed_item = input("What do you want to remove?")
    if removed_item not in g:
        print(my_func.red(f"You don\'t have {removed_item} in your list!"))
    else:
        g.remove(removed_item.lower())

def clear_list(g):
    print(my_func.blue("===Clear list==="))
    while True:
        clear_choice = input("Would you like to clear the list? (y/n)")
        if clear_choice.lower() != 'y' and clear_choice.lower() != 'n':
            print(my_func.red("Please enter either 'y' or 'n'"))
        if clear_choice.lower() == 'y':
            g.clear()
            print(my_func.blue("Successfully cleared your list!"))
            break
        if clear_choice.lower() == 'n':
            print(my_func.red("Choice cancelled."))
            break

while True:
    print(my_func.green("===SHOPPING LIST MANAGER==="))
    try:
        menu_choice = int(input("1. Add Item - 2. Remove Item - 3. View List - 4. Check/Uncheck Item - 5. Clear List - 6. Save My List - 7. Exit: "))
    except ValueError:
        print(my_func.red('Please enter a correct number'))
        continue

    if menu_choice == 1:
        add_item(groceries)
    if menu_choice == 2:
        remove_item(groceries)
    if menu_choice == 3:
        show_list(groceries)
    if menu_choice == 4:
        print("ckeck/uncheck item")
    if menu_choice == 5:
        clear_list(groceries)
    if menu_choice == 6:
        save_groceries(groceries)
    if menu_choice == 7:
        print("Thank you for your time! Have a nice day!")
        break