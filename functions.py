def get_todos(file_path='todos.txt'):
    """ Reads a file and returns a
    list of todos
    """
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos, file_path='todos.txt'):
    """ Opens a file and writes the
    current todos to it
    """
    with open(file_path, 'w') as file:
        file.writelines(todos)

def show_todos(todos):
    """ Prints out all todos """
    for index, item in enumerate(todos):
        item = item.strip('\n')
        print(f"{index + 1}: {item}")