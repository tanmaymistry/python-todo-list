tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Task selected")

    elif choice == "2":
        print("View Tasks selected")

    elif choice == "3":
        print("Mark Task as Complete selected")

    elif choice == "4":
        print("Delete Task selected")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
