class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, description):
        self.tasks[task_id] = {'description': description, 'status': 'Pending'}
        print(f"Task '{description}' added with ID {task_id}.")

    def update_status(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = status
            print(f"Task ID {task_id} status updated to '{status}'.")
        else:
            print(f"Task ID {task_id} not found.")

    def view_task(self, task_id):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            print(f"Task ID: {task_id}, Description: {task['description']}, Status: {task['status']}")
        else:
            print(f"Task ID {task_id} not found.")

# Main program
if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. Update task status")
        print("3. View a task status")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = int(input("Enter task ID: "))
            description = input("Enter task description: ")
            manager.add_task(task_id, description)

        elif choice == "2":
            task_id = int(input("Enter task ID to update: "))
            status = input("Enter new status (Pending/In Progress/Completed): ")
            manager.update_status(task_id, status)

        elif choice == "3":
            task_id = int(input("Enter task ID to view: "))
            manager.view_task(task_id)

        elif choice == "4":
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
