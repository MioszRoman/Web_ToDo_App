import streamlit as st

st.title("My To-Do App")
st.subheader("This app is to increase your productivity")

st.text_input(label="", placeholder="Add new todo...", key="new_todo")