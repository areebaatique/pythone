shopping_list = []

while True:
    action = input("Add, remove, show, or quit? ").lower()

    if action == "add":
        item = input("Enter item: ")
        shopping_list.append(item)

    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not in list.")

    elif action == "show":
        print("Current list:", shopping_list)

    elif action == "quit":
        break

    else:
        print("Unknown action.")

