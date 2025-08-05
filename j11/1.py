from tkinter import *

def showFullname():
    fullname = fname_ent.get() + " " + lname_ent.get()
    fullname_lbl.config(text=f"نام کامل شما : {fullname}")

bg="gray"
font=("vazir", 20, "bold")

window = Tk()
window.title("game")
window.config(bg="gray")
window.geometry("460x560")
window.resizable(False, False)

fname_lbl = Label(window, text="نام", bg=bg, font=font).pack(pady=30)
fname_ent = Entry(window, width=20, font=font, justify="center")
fname_ent.pack()
lname_lbl = Label(window, text="نام خانوادگی", bg=bg, font=font).pack(pady=30)
lname_ent = Entry(window, width=20, font=font, justify="center")
lname_ent.pack()
fullname_btn = Button(window, text="کلیک کنید", font=font, bg="green", width=15, command=showFullname).pack(pady=40)
fullname_lbl = Label(window, text="", font=font, bg=bg)
fullname_lbl.pack()

window.mainloop()