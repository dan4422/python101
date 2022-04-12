def list_of_tasks(tasks):
    for task in tasks:
        print(f"{tasks.index(task)} - {task['title']} - {task['priority']}")

tasks = []
while True:
    user_input = input('''Press 1 to add task
Press 2 to delete task
press 3 to view all tasks
press q to quit:
''')
    
    if user_input == '1':
        title = input('What is the title of the task?: ')
        priority = input('What level priority?(high/medium/low): ')
        if priority != 'high' or priority != 'medium' or priority != 'low':
            print('Use only high, medium, or low!')
        entered_task = {'title': title,
        'priority':priority}
        tasks.append(entered_task)
    elif user_input == '2': #deletes a task based on index number
        for task in tasks:
            print(f"{tasks.index(task)} - {task['title']} - {task['priority']}")
        user_delete = int(input('Enter the number of the task to delete: '))
        del tasks[user_delete]
        print('Remaining tasks:')
        for task in tasks:
            print(f"{tasks.index(task)} - {task['title']} - {task['priority']}")
    elif user_input == '3':
        #view all the tasks by index number then title then priority
        for task in tasks:
            print(f"{tasks.index(task)} - {task['title']} - {task['priority']}")
    elif user_input == 'q':
        break
    else:
        print('Try again!')

print('See you next time!')
