import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is a ToDo app")
st.write("This app aims to help you with your daily tasks")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a ToDo:", placeholder="Add new todo...")
