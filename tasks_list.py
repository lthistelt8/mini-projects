to_do = []

while True:
    task = input('Enter a task: ')
    to_do.append(task)
    task = input('Task successfully added! Would you like to add another task? ')
    if task.lower() == 'yes':
        print()
        continue
    elif task.lower() == 'no':
        print('To do list ended successfully. Here is your current list of things to do. ')
        for item in to_do:
            print(item)
        break