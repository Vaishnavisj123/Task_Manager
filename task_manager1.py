from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, description, due_date, priority):
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            self.tasks[task_id] = {
                'description': description,
                'status': 'Pending',
                'due_date': due_date_obj,
                'priority': priority
            }
            print(f"✅ Task '{description}' added with ID {task_id}, Due Date: {due_date}, Priority: {priority}.")
        except ValueError:
            print("⚠️ Invalid date format! Please use YYYY-MM-DD.")

    def update_task(self, task_id, status=None, due_date=None):
        if task_id in self.tasks:
            if status:
                self.tasks[task_id]['status'] = status
                print(f"🔄 Task ID {task_id} status updated to '{status}'.")

            if due_date:
                try:
                    due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
                    self.tasks[task_id]['due_date'] = due_date_obj
                    print(f"📅 Task ID {task_id} due date updated to {due_date}.")
                except ValueError:
                    print("⚠️ Invalid date format! Please use YYYY-MM-DD.")

        else:
            print("❌ Task ID not found.")

    def view_task(self, task_id):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            due_date = task['due_date'].strftime("%Y-%m-%d")
            days_remaining = (task['due_date'] - datetime.today()).days
            print(f"""
            📌 **Task ID:** {task_id}
            📝 **Description:** {task['description']}
            📊 **Status:** {task['status']}
            🎯 **Priority:** {task['priority']}
            ⏳ **Due Date:** {due_date}
            ⏳ **Days Remaining:** {days_remaining} days
            """)
        else:
            print("❌ Task ID not found.")

    def search_task(self, keyword):
        found = False
        for task_id, task in self.tasks.items():
            if keyword.lower() in task['description'].lower() or keyword.lower() == task['status'].lower():
                due_date = task['due_date'].strftime("%Y-%m-%d")
                days_remaining = (task['due_date'] - datetime.today()).days
                print(f"""
                🔍 **Task ID:** {task_id}
                📝 **Description:** {task['description']}
                📊 **Status:** {task['status']}
                🎯 **Priority:** {task['priority']}
                ⏳ **Due Date:** {due_date}
                ⏳ **Days Remaining:** {days_remaining} days
                """)
                found = True
        if not found:
            print("🚫 No matching tasks found.")

# Main program
if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. Update task status or due date")
        print("3. View a task status")
        print("4. Search task by description or status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = int(input("Enter task ID: "))
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            if priority not in ["High", "Medium", "Low"]:
                print("⚠️ Invalid priority! Setting priority to 'Medium'.")
                priority = "Medium"
            manager.add_task(task_id, description, due_date, priority)

        elif choice == "2":
            task_id = int(input("Enter task ID to update: "))
            status = input("Enter new status (Pending/In Progress/Completed) or leave blank to skip: ")
            due_date = input("Enter new due date (YYYY-MM-DD) or leave blank to keep the same: ")
            manager.update_task(task_id, status if status else None, due_date if due_date else None)

        elif choice == "3":
            task_id = int(input("Enter task ID to view: "))
            manager.view_task(task_id)

        elif choice == "4":
            keyword = input("Enter task description or status to search: ")
            manager.search_task(keyword)

        elif choice == "5":
            print("👋 Exiting Task Manager.")
            break

        else:
            print("⚠️ Invalid choice. Please enter a valid option.")
