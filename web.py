import streamlit as st

import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)

todos = functions.get_todos()

st.title("My Todo WebApp")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

st.checkbox("Buy grocery.")
st.checkbox("Throw the trash.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state