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
        status = "complete" if item["complete"] else "incomplete"
    print(f"{i}. [{status}] {item['task']}")
else:
    print("No saved tasks found.\n")

while True:
    task = input('Enter a task: ')
    to_do.append({"task": task, "complete": False})

    response = input('Task successfully added! Would you like to add another task?(y/n) ')
    if  response.lower() == 'y':
        print()
        continue
    elif response.lower() == 'n':
        print('To do list ended successfully. Here is your current list of things to do. ')
        for i, item in enumerate(to_do, 1):
            status = "complete" if item["complete"] else "incomplete"
            print(f'{i}. [{status}] {item["task"]}')
        break

mark_done = input("\nWould you like to mark any task as complete (y/n)")
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
