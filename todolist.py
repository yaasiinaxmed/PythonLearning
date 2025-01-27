# Simple To-Do List Manager

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("""
=== To-Do List Menu ===
1. Add a new task
2. View tasks
3. Mark a task as completed
4. Exit
    """)

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        task = input("Enter the task: ").strip()
        tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")
    
    elif choice == "2":
        if not tasks:
            print("No tasks found!")
        else:
            print("\n=== To-Do List ===")
            for i, t in enumerate(tasks):
                status = "✔" if t["completed"] else "✘"
                print(f"{i+1}. {t['task']} [{status}]")
    
    elif choice == "3":
        if not tasks:
            print("No tasks to complete!")
        else:
            print("\n=== Tasks ===")
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t['task']}")
            task_num = int(input("Enter the task number to mark as completed: ")) - 1
            
            if 0 <= task_num < len(tasks):
                tasks[task_num]["completed"] = True
                print(f"Task '{tasks[task_num]['task']}' marked as completed!")
            else:
                print("Invalid task number!")
    
    elif choice == "4":
        print("Goodbye! Have a productive day!")
        break
    
    else:
        print("Invalid choice. Please try again.")

