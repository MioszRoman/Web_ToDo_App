import streamlit as st
from functions import get_todos, write_todos
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

todos = get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] +'\n'
    todos.append(new_todo)
    write_todos(todos)

st.title("My To-Do App")
st.subheader("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo,  key="new_todo")