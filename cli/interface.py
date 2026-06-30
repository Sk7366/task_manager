from models.task import Task
from database.db_manager import DatabaseManager


class CLI:

    def __init__(self):

        self.db = DatabaseManager()
        self.db.create_table()

    def show_menu(self):

        print("\nTASK MANAGER")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete")
        print("6. Search Tasks")
        print("7. Filter By Status")
        print("8. Filter By Priority")
        print("9. Exit")

    def add_task(self):

        title = input("Title: ")
        description = input("Description: ")
        priority = input("Priority (low/medium/high): ")
        due_date = input("Due Date (YYYY-MM-DD): ")

        task = Task(
            title,
            description,
            priority,
            due_date
        )

        self.db.add_task(task)

        print("Task Added")

    def view_tasks(self):

        tasks = self.db.get_tasks()

        if not tasks:
            print("No tasks found")
            return

        for task in tasks:
            print(task)

    def update_task(self):

        try:
            task_id = int(input("Task ID: "))
        except ValueError:
            print("Invalid ID")
            return

        field = input(
            "Field (title,description,priority,due_date,status): "
        )

        value = input("New Value: ")

        self.db.update_task(
            task_id,
            field,
            value
        )

        print("Task Updated")

    def delete_task(self):

        try:
            task_id = int(input("Task ID: "))
        except ValueError:
            print("Invalid ID")
            return

        self.db.delete_task(task_id)

        print("Task Deleted")

    def mark_complete(self):

        try:
            task_id = int(input("Task ID: "))
        except ValueError:
            print("Invalid ID")
            return

        self.db.mark_complete(task_id)

        print("Task Marked Complete")

    def search_tasks(self):

        keyword = input("Keyword: ")

        results = self.db.search_tasks(keyword)

        for task in results:
            print(task)

    def filter_status(self):

        status = input(
            "Status (pending/completed): "
        )

        tasks = self.db.filter_by_status(status)

        for task in tasks:
            print(task)

    def filter_priority(self):

        priority = input(
            "Priority (low/medium/high): "
        )

        tasks = self.db.filter_by_priority(priority)

        for task in tasks:
            print(task)

    def run(self):

        while True:

            self.show_menu()

            choice = input("Choice: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.update_task()

            elif choice == "4":
                self.delete_task()

            elif choice == "5":
                self.mark_complete()

            elif choice == "6":
                self.search_tasks()

            elif choice == "7":
                self.filter_status()

            elif choice == "8":
                self.filter_priority()

            elif choice == "9":
                print("Goodbye")
                break

            else:
                print("Invalid Choice")