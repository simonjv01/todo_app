

todos = []

while True:
    user_action = input("Type add, show, or exit:")

    match user_action:
        case "add":
            todo = input("Enter a todo item:")
            todos.append(todo)
        case "show":
            for todo in todos:
                print(todo)
        case "exit":
            break
        case _:
            print("Invalid action. Please try again.")






