def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added successfully.")


def remove_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed successfully.")
    else:
        print("Invalid task number.")


def main():
    tasks = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(tasks, task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
