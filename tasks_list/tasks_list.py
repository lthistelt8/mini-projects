"""A simple to-do list."""
import json
import os
print("Current working directory:", os.getcwd(),"\n")

try:
    with open("tasks_list.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        to_do = data.get("to_do", [])
        archive = data.get("archive", [])
except FileNotFoundError:
    print("WARNING: File tasks_list not found (double-check your directory). Starting fresh...")
    to_do = []
    archive = []
except json.JSONDecodeError:
    print('WARNING: Could not read tasks_list.json (file may be corrupted). Starting fresh...')
    to_do = []
    archive = []

while True:
    if to_do:
        active_count = 0

        if active_count > 0:
            print(f"\n Active tasks: {active_count}")
        else:
            print("No active tasks found.")

        for i, item in enumerate(to_do, 1):
            status = "C" if item['complete'] else "IN"
            if not item['complete']:
                active_count +=1
                print(f"{i}. {item['task']}")


    print("\nWhat would you like to do today?")
    print("1. Add a task")
    print("2. Mark task as complete")
    print ('3. View completed (archived) tasks')
    print("4. Quit")

    choice = input("Enter the number (1-4) denoting your choice. ")
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
                archive.append({'task': to_do[choice - 1]})
                print(f"\nMarked '{to_do[choice - 1]['task']}' as complete. Archive updated.")

                with open("tasks_list.json", "w",encoding="utf-8") as file:
                    json.dump({ "to_do": to_do, "archive": archive}, file)
            else:
                print("\nInvalid task number.")
        except ValueError:
            print("\nPlease enter a valid number.")
        continue

    elif choice == "3":
        print("\nCompleted tasks: ")
        for i, item in enumerate(archive, 1):
            if item['task']['complete']:
                print(f"{i}. {item['task']['task']}")
        revers =int(input("Enter the number of the task to return to 'incomplete' status. Otherwise, press 0 to return to the main menu. "))
        if 1 <= revers <=len(archive):
            archive[revers - 1]['task']["complete"] = False
            to_do.append(archive[revers - 1]['task'])
            archive.pop(revers - 1)
            with open("tasks_list.json", "w", encoding="utf-8") as file:
                json.dump({"to_do": to_do, "archive": archive}, file)
            print('Task has been returned to active list.')
        elif revers == 0:
            print("\nReturning to main menu...\n")
            continue
        else:
            print("\nInvalid key. Please select the number corresponding with the task, or press 0 to return to the main menu.")
            continue
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
        print("Invalid input. Please enter a number between 1-4.")
