

todos = []

while True:
    user_action = input("Type add, show, complete, edit, or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo item:") + "\n"


            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "show":

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos, start=1):
               # print(index, '-', item, sep='')
                item = item.strip('\n')
                print(f"{index}.{item}")
        case "edit":
            number = int(input("Number of the todo item to edit: "))
            number = number - 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo item:") + "\n"
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo item to complete: "))
            number = number - 1
            todos.pop(number)
        case "exit":
            break
        case whatever:
            print("Invalid action. Please try again.")

print("Bye!")






