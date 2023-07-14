import datetime

tasks = []

def add_task():
    description = input("Enter task description: ")
    start_time = input("Enter start time (hh:mm AM/PM): ")
    end_time = input("Enter end time (hh:mm AM/PM): ")

    try:
        start_time = datetime.datetime.strptime(start_time, "%I:%M %p").strftime("%I:%M %p")
        end_time = datetime.datetime.strptime(end_time, "%I:%M %p").strftime("%I:%M %p")
    except ValueError:
        print("Invalid time format. Please use the format: hh:mm AM/PM")
        return

    task = {
        "description": description,
        "start_time": start_time,
        "end_time": end_time
    }
    tasks.append(task)
    print("Task added:", description)

def view_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. Description: {task['description']}")
            print(f"   Start Time: {task['start_time']}")
            print(f"   End Time: {task['end_time']}")
    else:
        print("No tasks found.")

def mark_task_complete():
    task_index = int(input("Enter the task number to mark as complete: "))
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print("Task marked as complete:", completed_task['description'])
    else:
        print("Invalid task index.")

def delete_task():
    task_index = int(input("Enter the task number to delete: "))
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print("Task deleted:", deleted_task['description'])
    else:
        print("Invalid task index.")

# Display current date and time
current_time = datetime.datetime.now()
current_date = current_time.strftime("%A, %B %d, %Y")
current_time = current_time.strftime("%I:%M:%S %p")
print("Current Date and Time:", current_date, current_time)

# Welcome screen
print("Welcome to the To-Do List Application!")
while True:
    print("\nSelect an option:")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

    option = input("Enter your choice (1-5): ")
    
    if option == '1':
        add_task()
    elif option == '2':
        view_tasks()
    elif option == '3':
        mark_task_complete()
    elif option == '4':
        delete_task()
    elif option == '5':
        print("Thank you for using the To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
