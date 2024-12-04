

todos = []

while True:
    user_action = input("Type add, show, edit, or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo item:")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos, start=1):
               # print(index, '-', item, sep='')
                print(f"{index}.{item}")
        case "edit":
            number = int(input("Number of the todo item to edit: "))
            number = number - 1
            todos[number] = input("Enter new todo: ")
        case "exit":
            break
        case whatever:
            print("Invalid action. Please try again.")

print("Bye!")






