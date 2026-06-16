class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n--- TO-DO LIST ---")
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else "✗"
            print(f"{i}. {task.title} [{status}]")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted = self.tasks.pop(index)
            print(f"Deleted: {deleted.title}")
        else:
            print("Invalid task number.")


def main():
    todo = TodoList()

    while True:
        print("\n===== TO-DO MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task name: ")
            todo.add_task(title)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            task_no = int(input("Enter task number to complete: ")) - 1
            todo.complete_task(task_no)

        elif choice == "4":
            todo.view_tasks()
            task_no = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(task_no)

        elif choice == "5":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()