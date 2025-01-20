from functions import get_todos, write_todos


while True:
    user_action = input("Type add or new then a todo, show, complete, edit, or exit:")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
            todo = user_action[4:] + "\n"
            
            todos = get_todos()

            todos.append(todo)

            write_todos(todos, "files/todos.txt")

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

            write_todos(todos, "files/todos.txt")
    elif 'complete' in user_action:
            number = int(input("Number of the todo item to complete: "))

            todos = get_todos()
            index = number - 1
            todo_to_complete = todos[index].strip('\n')

            todos.pop(index)

            write_todos(todos, "files/todos.txt")

            message = f"Todo item {todo_to_complete} has been completed."
            print(message)
    elif 'exit' in user_action:
        break
    else:
        print("Invalid action. Please try again.")
        continue    

print("Bye!")






