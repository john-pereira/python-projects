from modules import functions
import PySimpleGUI as sg
import time

# PySimpleGUI must be installed in order to the code work correctly

sg.theme("Reddit")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=10, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add New Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(size=10, image_source="complete.png", mouseover_colors="LightBlue2", tooltip="Mark Todo as Completed", key="Complete")
exit_button = sg.Button("Exit")


layout = [[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]]
window = sg.Window('My To-Do App',
                   layout=[[clock], [layout]],
                   font=('Helvetica', 16))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            try:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.set_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.set_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first")
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.set_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case    sg.WIN_CLOSED:
            break

window.close()
