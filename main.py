

todos = []

while True:
    user_action = input("Type add, show, edit, or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo item:")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("Number of the todo item to edit: "))
            existing_todo = todos[number]
            print(existing_todo)
        case "exit":
            break
        case whatever:
            print("Invalid action. Please try again.")

print("Bye!")






