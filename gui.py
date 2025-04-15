import FreeSimpleGUI.window
import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My Todo App", 
                   layout=[[label], [input_box], [add_button]], 
                   font=("Helvetica", 20))

event = window.read()
print(event)
window.close()




