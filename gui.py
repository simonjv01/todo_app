import FreeSimpleGUI.window
import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a todo")
input_box = sg.Input()

window = sg.Window("My Todo App", layout=[[label, input_box]])

window.read()

window.close()




