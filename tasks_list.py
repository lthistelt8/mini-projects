"""Module designed to create a simple to-do list"""
import json
try:
    with open("tasks_list.json", "r", encoding="utf-8") as file:
        to_do = json.load(file)
except FileNotFoundError:
    to_do = []

while True:
    task = input('Enter a task: ')
    to_do.append(task)

    response = input('Task successfully added! Would you like to add another task? ')
    if response.lower() == 'yes' or response.lower() == 'y':
        print()
        continue
    elif response.lower() == 'no' or response.lower() == 'n':
        print('To do list ended successfully. Here is your current list of things to do. ')
        for item in to_do:
            print(item)
        break
with open("tasks_list.json", "w", encoding='utf-8') as file:
    json.dump(to_do, file)
