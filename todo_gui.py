import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

# Current system time
clock = sg.Text('', key='clock')

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter a to-do: ', key='todo')

# Buttons
add_button = sg.Button('Add', key='add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete', key='complete')
exit_button = sg.Button('Exit')

# List of all todos in the 'todos.txt' file
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

sg.theme('Black')

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 14))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime('%B %d %Y, %I:%M %p'))

    match event:
        case 'add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 14))
        case 'complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 14))
        case 'Exit':
            break
        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                sg.popup('An empty to-do list! Add something to it', font=('Helvetica', 14))
        case sg.WIN_CLOSED:
            break

window.close()