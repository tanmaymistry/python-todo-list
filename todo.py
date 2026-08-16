import os

FILE_NAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\n===== TO-DO LIST =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!\n")

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter task number to remove: "))
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}\n")
                except (ValueError, IndexError):
                    print("Invalid task number.\n")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
