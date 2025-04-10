import streamlit as st
from functions import get_todos, write_todos

st.title("My To-Do App")
st.subheader("This app is to increase your productivity")

st.text_input(label="", placeholder="Add new todo...", key="new_todo")