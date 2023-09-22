# from functions import get_todos, set_todos
from modules import functions

while True:
    user_action = input("Typer add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.set_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
            number = int(input("Type the number of the todo to edit: "))
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.set_todos(todos)

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print('Updated todo list', row)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
            number = int(input("Type the number of the todo to remove: "))
            number = number - 1

            todos = functions.get_todos()

            index = number
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.set_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print('Bye!')


