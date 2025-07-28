from tkinter import *

root = Tk()
root.geometry("300x400")

lbl1 = Label(root, text="سلام", font=("arial", 40, "bold"), fg="blue", bg="pink").grid(row=0, column=0, padx=200, pady=150)
lbl2 = Label(root, text="چطوری", font=("arial", 40, "bold"), fg="blue", bg="pink").grid(row=0, column=1)
lbl3 = Label(root, text="خوبم", font=("arial", 40, "bold"), fg="blue", bg="pink").grid(row=1, column=0)
lbl4 = Label(root, text="تو چطوری", font=("arial", 40, "bold"), fg="blue", bg="pink").grid(row=1, column=1)

root.mainloop()