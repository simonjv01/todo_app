

todos = []

while True:
    user_action = input("Type add, show, complete, edit, or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo item:") + "\n"

            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos, start=1):
               # print(index, '-', item, sep='')
                print(f"{index}.{item}")
        case "edit":
            number = int(input("Number of the todo item to edit: "))
            number = number - 1
            todos[number] = input("Enter new todo: ")

            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "complete":
            number = int(input("Number of the todo item to complete: "))
            number = number - 1
            todos.pop(number)
        case "exit":
            break
        case whatever:
            print("Invalid action. Please try again.")

print("Bye!")






