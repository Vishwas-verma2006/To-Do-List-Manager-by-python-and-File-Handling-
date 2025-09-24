# This script uses only built-in file handling. No libraries are imported.

'''FILENAME = "D:\CODING\python language\Task.txt"


# --- File Handling Functions ---

def load_tasks_from_file():
    """
    Loads tasks from a plain text file.
    Each line is parsed to rebuild the task list.
    """
    tasks = []
    try:
        with open(FILENAME, 'r') as f:
            for line in f:
                # Remove leading/trailing whitespace, like the newline character
                line = line.strip()
                if line.startswith("[x] "):
                    # The task is the string after the first 4 characters
                    tasks.append({"task": line[4:], "completed": True})
                elif line.startswith("[ ] "):
                    tasks.append({"task": line[4:], "completed": False})
    except FileNotFoundError:
        # If the file doesn't exist, it's the first run.
        # An empty list is fine, the file will be created on the first save.
        return []
    return tasks

def save_tasks_to_file(tasks_list):
    """Saves the current list of tasks to the plain text file."""
    with open(FILENAME, 'w') as f:
        for task_item in tasks_list:
            status = "[x]" if task_item["completed"] else "[ ]"
            # Write each task as a formatted string on its own line
            f.write(f"{status} {task_item['task']}\n")

# --- Core Task Functions ---

def add_task(tasks):
    """Prompts the user for a task, adds it, and saves the file."""
    task_name = input("Enter the task you want to add: ")
    tasks.append({"task": task_name, "completed": False})
    save_tasks_to_file(tasks) # Save changes immediately
    print(f"\nTask '{task_name}' has been added successfully!")

def view_tasks(tasks):
    """Displays all current tasks with their status and index."""
    if not tasks:
        print("\nYour to-do list is empty. Add a task to get started!")
        return

    print("\n--- Your To-Do List ---")
    for idx, task_item in enumerate(tasks):
        status = "✓" if task_item["completed"] else " "
        print(f"{idx + 1}. [{status}] {task_item['task']}")
    print("-----------------------")

def mark_task_complete(tasks):
    """Marks a task as complete and saves the file."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks_to_file(tasks) # Save changes immediately
            print(f"\nTask {task_num} has been marked as complete.")
        else:
            print("\nInvalid task number. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task and saves the file."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks_to_file(tasks) # Save changes immediately
            print(f"\nTask '{removed_task['task']}' has been deleted.")
        else:
            print("\nInvalid task number. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

# --- Main Application Loop ---

def show_menu():
    """Prints the main menu of options."""
    print("\n===== To-Do List Manager =====")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("==============================")

if __name__ == "__main__":
    # Load all tasks from the file right when the program starts.
    current_tasks = load_tasks_from_file()

    while True:
        show_menu()
        choice = input("Please enter your choice (1-5): ")

        if choice == '1':
            add_task(current_tasks)
        elif choice == '2':
            view_tasks(current_tasks)
        elif choice == '3':
            mark_task_complete(current_tasks)
        elif choice == '4':
            delete_task(current_tasks)
        elif choice == '5':
            print("\nThank you for using the To-Do List Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")
'''

# TO DO LIST MANAGER WITH FILE HANDLING

# file for file handling
File = "D:\CODING\python language\Task.txt"

def load_task():
    tasks = []
    try:
        with open(File , "r") as f:
            for line in f:
                line = line.strip()
                if "[#] " in line: # you can use this if line.startswith("[#] "):
                    tasks.append({"task": line[4:] , "completed": True})
                elif line.startswith("[ ] "):
                    tasks.append({"task": line[4:], "completed": False})
    except FileNotFoundError:
        print("File not found !")

    return tasks 
def save_task(tasks):
    try:
        with open(File, "w") as f:
            for task in tasks:
                status = "[#]" if task["completed"] else "[ ]"
                f.write(f"{status} {task["task"]}\n")
    except Exception as e:
        print("Error saving tasks !",e)

#core function

def add_task(tasks):
    task = input("Enter the task you want to add:- ")
    tasks.append({"task": task, "completed": False})
    save_task(tasks)
    print(f"Task '{task}' has saved successfully !")

def view_task(tasks):
    if len(tasks)==0:
        print("You TO-DO list is empty !")
    
    else:
        print("\n-----Your TO DO List------")
        for i, task in enumerate(tasks):
            status = "✅" if task["completed"] else "❎"
            print(f"{i+1}. {status} {task['task']}")
            
            
def edit_task(tasks):
    view_task(tasks)
    
    if len(tasks)==0:
        return 
    
    else:
        task_num = int(input("Enter the number of the task to edit:- "))
        if task_num >= 1 and task_num <= len(tasks):
            new_task = input("Enter the new task:- ")
            tasks[task_num -1]["task"] = new_task
            save_task(tasks)
            # task saved on file
            print(f"Task '{new_task}' has edited sucessfully !")
        else:
            print("Invalid task number !")

def mark_task(tasks):
    view_task(tasks)

    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the number of the task to mark as complete:- "))
        if task_num >= 1 and task_num <=len(tasks):
            tasks[task_num -1]["completed"] = True
            save_task(tasks)
            print(f"Task '{task_num}' has marked as completed !")
        else:
            print("Invalid task number !")

    except ValueError:
        print("Invalid input ! Please enter a number. ")

def delete_task(tasks):
    view_task(tasks)

    if not tasks:
        return 

    try:
        task_num = int(input("Enter the number of the task to delete:- "))
        delete = tasks.pop(task_num - 1)
        save_task(tasks)
        print(f"Task '{delete["task"]}' has deleted successfully !")
    except ValueError:
        print("Invalid input ! Please enter a number.")

# main function 
tasks = load_task()

while True:
    print("\n============================")
    print("Welcome to TO-DO List Manager !")
    print("1. Add Task")
    print("2. View Task")
    print("3. Edit Task")
    print("4. Mark Task")
    print("5. Delete Taks")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice (1-6):- "))
    except ValueError:
        print("Invalid input ! Please enter a number.")
        continue

    match choice:
        case 1:
            add_task(tasks)
        
        case 2:
            view_task(tasks)
        
        case 3:
            edit_task(tasks)
        
        case 4:
            mark_task(tasks)
        
        case 5:
            delete_task(tasks)
        
        case 6:
            print("Exting program Good Beye !")
            break
        case _:
            print("Invalid choice !")


    
















































