# from functions import get_todos, write_todos
import functions
import time


curr_time = time.strftime('It is the %d of %B %Y, %I:%M %p')
print(curr_time)
print("Checking committing")

while True:
    user_action = input('Add/edit/show/complete/exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}: {item}')
    elif user_action.startswith('edit'):
        try:
            index = int(user_action[5:])
            index = index - 1

            todos = functions.get_todos()

            todo_edit = input('Enter what you want to do instead: ')
            todos[index] = todo_edit + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            num_to_compl = int(user_action[9:])
            index = num_to_compl - 1

            todos = functions.get_todos()
            todo_to_remove = todos[index].strip('\n')
            print(f'To-do "{todo_to_remove}" was removed from the list')
            todos.pop(index)

            functions.write_todos(todos)
        except IndexError:
            print("There's no to-do with a number provided")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')
print('Bye!')
