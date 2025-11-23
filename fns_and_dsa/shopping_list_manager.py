shopping_list = []

#add item to list
def add_item(item):
    shopping_list.append(item)

#remove item from list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)

def display_menu():
    print(shopping_list)


#user interface

while True:
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Shopping List")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        item = input("Enter the item to add: ")
        add_item(item)
        print(f"{item} has been added to the shopping list.")
        
    elif choice == '2':
        item = input("Enter the item to remove: ")
        remove_item(item)
        print(f"{item} has been removed from the shopping list.")
        
    elif choice == '3':
        print("Current Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
            
    elif choice == '4':
        print("Exiting Shopping List Manager. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")  