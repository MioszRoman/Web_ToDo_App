def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as local_file:
        todos = local_file.readlines()
    return todos

def write_todos(local_todos, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(local_todos)
