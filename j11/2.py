from tkinter import *

def showFullname():
    fullname = fname_ent.get() + " " + lname_ent.get()
    fullname_lbl.config(text=f"نام کامل شما : {fullname}")

bg="gray"
font=("vazir", 20, "bold")

window = Tk()
window.title("game")
window.config(bg="gray")
window.geometry("460x300")
window.resizable(False, False)

fname_lbl = Label(window, text="name", bg=bg, font=font).place(x=20, y=10)
fname_ent = Entry(window, width=20, font=font, justify="center")
fname_ent.place(x=120, y=10)
lname_lbl = Label(window, text="familly", bg=bg, font=font).place(x=20, y=80)
lname_ent = Entry(window, width=20, font=font, justify="center")
lname_ent.place(x=120, y=80)
fullname_btn = Button(window, text="کلیک کنید", font=font, bg="green", width=15, command=showFullname).place(x=100, y=200)
fullname_lbl = Label(window, text="", font=font, bg=bg)
fullname_lbl.place(x=100, y=140)

window.mainloop()