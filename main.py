items = []


# add item to shopping list
def add_item(item):
    items.append(item)
    print(f"Item '{item} added")


# delete item from shopping list
def delete_item(item):
    if item in items:
        items.remove(item)
        print(f"Item '{item} deleted")
    else:
        print(f"Item '{item} doesn't exist in list")


# update item in shopping list
def update_item(item, new_item):
    if item in items:
        index = items.index(item)
        items[index] = new_item
        print(f"Item '{item}' is updated to '{new_item}")
    else:
        print(f"Item '{item}' doesn't exist in list")


# display all items to the console
def display_items():
    if items:
        print("------------------------")
        print("Shopping List")
        print("------------------------")

        for item in items:
            print(item)
    else:
        print("No items in list")


def shopping_list():
    while True:
        print("==========================")
        print("1. Add Item")
        print("2. Delete Item")
        print("3. Update Item")
        print("4. Display Shopping List")
        print("5. Exit")
        print("==========================")

        choice = input("Select a option from the above list: ")
        if choice == '1':
            item = input("Type new item: ")
            add_item(item)

        elif choice == '2':
            item = input("Type item to delete: ")
            delete_item(item)

        elif choice == '3':
            item = input("Type item to update: ")
            new_item = input("Type new item to replace old item: ")
            update_item(item, new_item)

        elif choice == '4':
            display_items()

        elif choice == '5':
            print("Exit program")
            break

        else:
            print("Invalid input. Please type valid numbers between 1-5")


if __name__ == "__main__":
    shopping_list()
