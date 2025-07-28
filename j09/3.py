from tkinter import *

def showFullname ():
    fullName = fname_ent.get() + " " + lname_ent.get()
    fullname_lbl.configure(text=fullName)


root = Tk()

root.geometry("350x350")

fname_lbl = Label(root, text="نام", font=("vazir", 20, "bold")).pack()
fname_ent = Entry(root, width=20, font=("vazir", 18), justify="right")
fname_ent.pack()
fname_lbl = Label(root, text="نام خانوادگی", font=("vazir", 20, "bold")).pack()
lname_ent = Entry(root, width=20, font=("vazir", 18), justify="center")
lname_ent.pack()
fullName_btn = Button(root, text="تایید", font=("vazir", 20, "bold"), bg="#4a5", width=15, command=showFullname).pack(pady=10)
fullname_lbl = Label(root, text="", font=("vazir", 20, "bold"))
fullname_lbl.pack()

root.mainloop()