from task_manager import TaskManager

manager = TaskManager()
while True:
    print("Hello, ToDo List!")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        manager.add_task(task_name, task_description)
        print(f"Task '{task_name}' added!")
    
    elif choice == '2':
        print("Viewing all tasks...")
        tasks = manager.view_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                status = "✓" if task.status == "Complete" else "✗"
                print(f"[{status}] {task.id}. {task.title} - {task.description}")
    
    elif choice == '3':
        print("Exiting the ToDo List. Goodbye!")
        break