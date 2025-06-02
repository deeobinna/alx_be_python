shopping_list = []
def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    display_menu()
    while True:
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_item = input("Enter item to add: ")
            shopping_list.append(add_item)
            print(f"Added '{add_item}' to the shopping list.")
        elif choice == '2':
            remove_item = input("Enter item to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"Removed '{remove_item}' from the shopping list.")
            else:
                print(f"'{remove_item}' not found in the shopping list.")
        elif choice == '3':
            print("Current Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    add_item = input("Enter item to add: ")
   