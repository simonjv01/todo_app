def get_todos():
    with open("files/todos.txt", "r") as file:
        todos = file.readlines()
    return todos



while True:
    user_action = input("Type add or new then a todo, show, complete, edit, or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
            todo = user_action[4:] + "\n"
            
            get_todos()

            todos.append(todo)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

    elif 'show' in user_action:

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos, start=1):
               # print(index, '-', item, sep='')
                item = item.strip('\n')
                print(f"{index}.{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            number = number - 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo item:") + "\n"
            todos[number] = new_todo

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
             print("Invalid number. Please try again.")
             continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_complete = todos[index].strip('\n')

            todos.pop(index)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo item {todo_to_complete} has been completed."
            print(message)
        except IndexError:
            print("Invalid number. Please try again.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid action. Please try again.")
        continue    

print("Bye!")






