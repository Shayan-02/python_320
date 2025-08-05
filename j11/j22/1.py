from tkinter import *
from tkinter import ttk


root = Tk()  # Create the main window
root.config(bg="gray")
root.title("My App")  # Set window title
root.geometry("400x300")  # Set window size (width x height)
root.resizable(1, 1)
label = Label(root, text="name", font=("Arial", 12))
label.pack()
entry = ttk.Entry(root, width=30)
entry.pack()
text = Text(root, height=6, width=40)
text.pack()
x = IntVar()
y = IntVar()
checkbutton = Checkbutton(root, text="Check me", variable=x)
checkbutton2 = Checkbutton(root, text="Check me", variable=y)
checkbutton.pack()
checkbutton2.pack()
var = IntVar()
radiobutton1 = Radiobutton(root, text="Option 1", variable=var, value=1)
radiobutton2 = Radiobutton(root, text="Option 2", variable=var, value=2)
radiobutton1.pack()
radiobutton2.pack()
listbox = Listbox(root)
listbox.insert(1, "python")
listbox.insert(2, "c")
listbox.insert(3, "js")
listbox.pack()

combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3", "mamad"])
combo.pack()


def on_click():
    print("Button clicked!")


button = Button(root, text="Click Me", command=on_click)
button.pack()

root.mainloop()
