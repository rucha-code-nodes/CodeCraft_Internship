# pip install tabulate
import datetime
from tabulate import tabulate

# Task structure
class Task:
    def __init__(self, description, deadline, priority):
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.description} | {self.deadline} | Priority: {self.priority} | Status: {status}"

# Task Manager
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline, priority):
        # Try parsing with both formats
        try:
            # First attempt to parse YYYY-MM-DD format
            deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            try:
                # If the above fails, try parsing DD-MM-YYYY format
                deadline = datetime.datetime.strptime(deadline, "%d-%m-%Y")
            except ValueError:
                print("Invalid date format. Please enter the date as YYYY-MM-DD or DD-MM-YYYY.")
                return

        task = Task(description, deadline, priority)
        self.tasks.append(task)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Invalid task index.")

    def display_tasks(self, filter_completed=False):
        tasks_to_display = self.tasks if not filter_completed else [t for t in self.tasks if not t.completed]
        if tasks_to_display:
            tasks_table = [[idx, task.description, task.deadline.strftime("%Y-%m-%d"), task.priority, "Completed" if task.completed else "Pending"]
                           for idx, task in enumerate(tasks_to_display)]
            print(tabulate(tasks_table, headers=["Index", "Description", "Deadline", "Priority", "Status"]))
        else:
            print("No tasks available.")

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: (x.priority, x.deadline))

# Main program
def main():
    task_manager = TaskManager()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Display Tasks")
        print("4. Display Pending Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            deadline = input("Enter task deadline (YYYY-MM-DD or DD-MM-YYYY): ")
            priority = int(input("Enter task priority (1-High, 2-Medium, 3-Low): "))
            task_manager.add_task(description, deadline, priority)
            task_manager.sort_tasks()

        elif choice == "2":
            task_manager.display_tasks()
            task_index = int(input("Enter task index to complete: "))
            task_manager.complete_task(task_index)

        elif choice == "3":
            task_manager.display_tasks()

        elif choice == "4":
            task_manager.display_tasks(filter_completed=True)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
