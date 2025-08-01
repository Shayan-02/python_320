from tkinter import *

def showFullname():
    fullName = firstname_ent.get() + " " + lastname_ent.get()
    fullName_lbl.config(text=fullName)

root = Tk()
root.title("fullname app")
root.geometry("380x380")
root.config(bg="red")

bg_r = "red"
c_font=("vazir", 20, "bold")

firstname_lbl = Label(root, text="نام", font=c_font, bg=bg_r).pack()
firstname_ent = Entry(root, width=20, font=c_font, justify="center")
firstname_ent.pack()
lastname_lbl = Label(root, text="نام خانوادگی", font=c_font, bg=bg_r).pack()
lastname_ent = Entry(root, width=20, font=c_font, justify="center")
lastname_ent.pack()
fullname_btn = Button(root, text="تایید", font=c_font, bg="blue", width=15, command=showFullname).pack(pady=30)
fullName_lbl = Label(root, text="", font=c_font, bg=bg_r)
fullName_lbl.pack()

root.mainloop()