
from organizer_core import add_item, show_item, complete_item

def interface(): 
    print("Welcome to My Task Organizer") 

    while True:
        print("~~~ORGANIZER MENU~~~")
        print("1 → Add a new task")
        print("2 → View all tasks")
        print("3 → Complete a task")
        print("4 → Exit organizer")

        user_choice = input("Select an option (1-4):") 

        if user_choice == "1":
            add_item()
        elif user_choice == "2":
            show_item()
        elif user_choice == "3":
            complete_item()
        elif user_choice == "4":
            print("Exiting My Task Organizer.goodbye!") 
            break
        else:
            print("Inappropiate option.Please select 1-4 only.") 













