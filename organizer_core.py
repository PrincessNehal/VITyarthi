my_tasks = []  

def add_item():
    task_item = input("Enter a task: ").strip() 
    if task_item == "":
        print(" You cannot add an empty task") 
    else:
        my_tasks.append({"task": task_item, "done": False})
        print(f"Successfully added: {task_item}")


def show_item():
    if not my_tasks:
        print("No tasks have been added yet.")
        return

    print("\n--- TASK LIST ---")
    for index, task_entry in enumerate(my_tasks, start=1):
        status = "Done" if task_entry["done"] else "Pending"
        print(f"{index}. {task_entry['task']}  -->  {status}") 


def complete_item():
    show_item()
    if not my_tasks:
        return

    try:
        number = int(input("Enter the task number you have completed: "))
        if 1 <= number <= len(my_tasks):
            my_tasks[number - 1]["done"] = True
            print(f" Task '{my_tasks[number - 1]['task']}' marked as done")
        else:
            print("Invalid task number, try again.")
    except ValueError:
        print("Please enter a valid number.") 



