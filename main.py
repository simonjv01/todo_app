

def get_todos(filepath="files/todos.txt"):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
     with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

while True:
    user_action = input("Type add or new then a todo, show, complete, edit, or exit:")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
            todo = user_action[4:] + "\n"
            
            todos = get_todos()

            todos.append(todo)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

    elif 'show' in user_action:

            todos = get_todos()

            for index, item in enumerate(todos, start=1):
               # print(index, '-', item, sep='')
                item = item.strip('\n')
                print(f"{index}.{item}")
    elif 'edit' in user_action:
            number = int(input("Number of the todo item to edit: "))
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo item:") + "\n"
            todos[number] = new_todo

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
    elif 'complete' in user_action:
            number = int(input("Number of the todo item to complete: "))

            todos = get_todos()
            index = number - 1
            todo_to_complete = todos[index].strip('\n')

            todos.pop(index)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo item {todo_to_complete} has been completed."
            print(message)
    elif 'exit' in user_action:
        break
    else:
        print("Invalid action. Please try again.")
        continue    

print("Bye!")






