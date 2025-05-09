"""Module designed to create a simple to-do list"""
import json
try:
    with open("tasks_list.json", "r", encoding="utf-8") as file:
        to_do = json.load(file)
except FileNotFoundError:
    to_do = []
except json.JSONDecodeError:
    print('Warning: Could not read tasks_list.json (file may be corrupted). Starting fresh')
    to_do = []

if to_do:
    print("Here are your saved tasks:")
    for i, item in enumerate(to_do, 1):
        status = "C" if item["complete"] else "IN"
    print(f"{i}. [{status}] {item['task']}")
else:
    print("No saved tasks found.\n")

while True:
    print("\nWhat would you like to do today?")
    print("1. Add a task")
    print("2. Mark task as complete")
    print("3. Quit")

    choice = input("Enter the number (1-3) denoting your choice. ")
    if choice == "1":

        print("Adding task...")
        task = input("Enter a task: ")
        to_do.append({'task': task, "complete": False})
        print(f"Task '{task}' created successfully!")
        with open("tasks_list.json", "w", encoding="utf-8") as file:
            json.dump(to_do, file)

    elif choice == "2":
        if not to_do:
            print("No tasks to mark complete.")
            continue

        for i, item in enumerate(to_do, 1):
            status = "C" if item["complete"] else "IN"
            print(f"{i}. [{status}] [{item['task']}]")

        try:
            choice = int(input("Enter the number of the task to mark complete: "))
            if 1 <= choice <= len(to_do):
                to_do[choice - 1]["complete"] = True
                print(f"Marked '{to_do[choice - 1]['task']}' as complete.")

                with open("tasks_list.json", "w",encoding="utf-8") as file:
                    json.dump(to_do, file)
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


    elif choice == "3":
        print("Exiting program. ")

    else:
        print("Invalid input. Please enter a number between 1-3.")
mark_done = input("\nWould you like to mark any task as complete? (y/n) ")
if mark_done.lower() in ('yes', 'y'):
    for i, item in enumerate(to_do, 1):
        print(f"{i}. {item['task']}")
    try:
        choice = int(input("Enter the number of tasks to mark complete: "))
        if 1 <= choice <= len(to_do):
            to_do[choice - 1]['complete'] = True
            print(f"Marked '{to_do[choice - 1]['task']}' as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Not a number.")

with open("tasks_list.json", "w", encoding='utf-8') as file:
    json.dump(to_do, file)

input("Program complete. Click any button to exit.")
