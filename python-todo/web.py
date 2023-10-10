import streamlit as st
from modules import functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.set_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is a ToDo app")
st.write("This app aims to help you with your daily tasks")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a ToDo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# st.session_state
