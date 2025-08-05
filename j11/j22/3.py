from calendar import c
from tkinter import *

def click_shod():
    lbl.config(text="کلیک شد")

root = Tk()
root.title("Tkinter")
root.geometry("500x400")

test_lbl = Label(root, text="سلام", font=("Arial", 16))
test_lbl.pack(pady=10)

test_ent = Entry(root, width=40)
test_ent.pack()

test_btn = Button(root, text="کلیک کنید", bg="lightgreen", command=click_shod)
test_btn.pack()

lbl = Label(root, text="")
lbl.pack()

test_txt = Text(root, width=40, height=5)
test_txt.pack()

root.mainloop()
