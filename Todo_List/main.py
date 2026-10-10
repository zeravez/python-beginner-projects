tasks = []

while True :
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("Your tasks:")
        for task in tasks:
            print("-", task)
    elif choice == "3":
        task = input("Task to delete:")
        if task in tasks:
            tasks.remove(task)
            print("Task deleted!")
        else:
            print("Task not found")
    elif choice == "4":
        print("Goodbye!")
        break
