import FreeSimpleGUI.window
import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My Todo App", 
                   layout=[[label], [input_box], [add_button]], 
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)


window.close()




