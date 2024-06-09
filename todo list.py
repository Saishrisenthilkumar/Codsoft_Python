class Task:
    def __init__(self, title, status='Not Started'):
        self.title = title
        self.status = status
    def __str__(self):
        return f'{self.title} - {self.status}'
class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
    def update_task(self, title, status):
        for task in self.tasks:
            if task.title == title:
                task.status = status
    def view_tasks(self):
        for task in self.tasks:
            print(task)
todo_list = ToDoList()
while True:
    print("\n1. Add task")
    print("2. Update task")
    print("3. View tasks")
    print("4. Exit")
    print("5. Restart")
    choice = input("Enter your choice: ")
    if choice == '1':
        title = input("Enter the task: ")
        todo_list.add_task(title)
    elif choice == '2':
        title = input("Enter the task to update: ")
        status = input("Enter the new status: ")
        todo_list.update_task(title, status)
    elif choice == '3':
        todo_list.view_tasks()
    elif choice == '4':
        break
    elif choice == '5':
        ToDoList()
    else:
        print("Invalid choice. Please try again.")