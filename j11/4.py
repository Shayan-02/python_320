from tkinter import *
from random import *

def number():
    global correct_number
    start = int(start_ent.get())
    end = int(end_ent.get())
    correct_number = randint(start, end)
    print(correct_number)

def check_number():
    guess_number = int(guess_ent.get())
    if guess_number == correct_number:
        result.config(text="you win")
    elif guess_number > correct_number:
        result.config(text="enter lower")
    elif guess_number < correct_number:
        result.config(text="enter bigger")

font=("vazir", 20, "bold")
bg = "gray"

root = Tk()
root.title("guess number game")
root.geometry("400x500")
root.resizable(0, 0)
root.config(bg=bg)

start_lbl = Label(root, text="start range", font=font, bg=bg).place(x=10, y=20)

start_ent = Entry(root, width=10, font=font)
start_ent.place(x=210, y=20)

end_lbl = Label(root, text="end range", font=font, bg=bg).place(x=10, y=90)

end_ent = Entry(root, width=10, font=font)
end_ent.place(x=210, y=90)

start_game_btn = Button(root, text="start game", font=font, bg="green", width=15, command=number).place(x=80, y=150)

guess_lbl = Label(root, text="guess", font=font, bg=bg).place(x=160, y=250)
guess_ent = Entry(root, font=font, width=10)
guess_ent.place(x=120, y=300)

check_btn = Button(root, text="check", font=font, bg="lightblue", command=check_number).place(x=150, y=370)

result = Label(root, text="", font=font, bg=bg)
result.place(x=150, y=450)

root.mainloop()