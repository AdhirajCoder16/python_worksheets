def todo_list():
    tasks = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter new task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks available.")
        elif choice == '3':
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                to_del = input("Enter task number to delete: ")
                if to_del.isdigit() and 1 <= int(to_del) <= len(tasks):
                    tasks.pop(int(to_del) - 1)
                    print("Task deleted.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to delete.")
        elif choice == '4':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    todo_list()
