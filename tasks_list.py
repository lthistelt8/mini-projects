"""A simple to-do list."""
import json
import os
print("Current working directory:", os.getcwd())

try:
    with open("tasks_list.json", "r", encoding="utf-8") as file:
        to_do = json.load(file)
except FileNotFoundError:
    to_do = []
    archive = []
except json.JSONDecodeError:
    print('Warning: Could not read tasks_list.json (file may be corrupted). Starting fresh...')
    to_do = []
    archive = []

while True:
    if to_do:
        print("Here are your active tasks:")
        for i, item in enumerate(to_do, 1):
            status = "C" if item['complete'] else "IN"
            print(f"{i}. [{status}] {item['task']}")
    else:
        print('No saved tasks found.\n')


    print("\nWhat would you like to do today?")
    print("1. Add a task")
    print("2. Mark task as complete")
    print ('3. View completed (archived) tasks')
    print("4. Quit")

    choice = input("Enter the number (1-3) denoting your choice. ")
    if choice == "1":

        print("\nAdding task...")
        task = input("Enter a task: ")
        to_do.append({'task': task, "complete": False})
        print(f"\nTask '{task}' created successfully!")

        try:
            with open("tasks_list.json", "w", encoding="utf-8") as file:
                json.dump(to_do, file)
        except Exception as e:
            print("Error writing to file:", e)
            input("Press Enter to exit... ")
        continue

    elif choice == "2":
        if not to_do:
            print("\nNo tasks to mark complete.")
            continue

        for i, item in enumerate(to_do, 1):
            status = "C" if item["complete"] else "IN"
            print(f"{i}. [{status}] [{item['task']}]")

        try:
            choice = int(input("Enter the number of the task to mark complete: "))
            if 1 <= choice <= len(to_do):
                to_do[choice - 1]["complete"] = True
                archive.append({'task': choice})
                print(f"\nMarked '{to_do[choice - 1]['task']}' as complete. Archive updated.")

                with open("tasks_list.json", "w",encoding="utf-8") as file:
                    json.dump(to_do, file)
            else:
                print("\nInvalid task number.")
        except ValueError:
            print("\nPlease enter a valid number.")
        continue

    elif choice == "3":
        print("\nCompleted tasks: ")
        for i, item in enumerate(archive, 1):
            if status == "C":
                print(status)
        revers = "Enter the number of the task to return to 'incomplete' status. Otherwise, press the Space bar to return to the main menu."
        if 1 <= revers <=len(archive):
            archive[revers - 1]["complete"] = False
        elif revers == " ":
            print("\nReturning to main menu...")
            continue


    elif choice == "4":
        print("\nExiting program. ")
        break

    elif choice == 'tstadminluthi':
        confirm = input("!!! ADMIN MODE: clear ALL tasks? (y/n This cannot be undone!) ")
        if confirm.lower()in ('y', 'yes'):
            to_do.clear()
            with open('tasks_list.json',"w", encoding="utf-8") as f:
                json.dump(to_do, f)
            print("All tasks have been cleared.")
        else:
            print("Admin action cancelled. Returning to main menu.\n")

    else:
        print("Invalid input. Please enter a number between 1-3.")
