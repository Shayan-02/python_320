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

fname_lbl = Label(window, text="name", bg=bg, font=font).grid(row=0, column=0, padx=20, pady=10)
fname_ent = Entry(window, width=20, font=font, justify="center")
fname_ent.grid(row=0, column=1)
lname_lbl = Label(window, text="familly", bg=bg, font=font).grid(row=1, column=0, padx=10, pady=20)
lname_ent = Entry(window, width=20, font=font, justify="center")
lname_ent.grid(row=1, column=1)
fullname_btn = Button(window, text="کلیک کنید", font=font, bg="green", width=15, command=showFullname).grid(row=2, column=1)
fullname_lbl = Label(window, text="", font=font, bg=bg)
fullname_lbl.grid(row=3, column=1)

window.mainloop()