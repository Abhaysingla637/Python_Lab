from collections import deque

# Task queue
tasks = deque()

print("Task Scheduler")

while True:
    print("\n1. Add Task")
    print("2. Run Next Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add a task
    if choice == "1":
        task = input("Enter task name: ")
        priority = input("Is it high priority (yes/no): ").lower()

        # Boolean logic
        if priority == "yes" and task != "":
            tasks.append(task)
            print("Task added successfully.")

        elif priority == "no" or task == "":
            if task == "":
                print("Task name cannot be empty.")
            else:
                tasks.append(task)
                print("Normal priority task added.")

    # Run next task
    elif choice == "2":
        if len(tasks) > 0:
            task = tasks.popleft()
            print("Running task:", task)
        else:
            print("No tasks available.")

    # Display all tasks
    elif choice == "3":
        if tasks:
            print("\nScheduled Tasks:")
            for task in tasks:
                print("-", task)
        else:
            print("No tasks scheduled.")

    # Exit
    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    # Invalid input
    else:
        print("Invalid choice. Please try again.")