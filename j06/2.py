from tkinter import*
from random import choice as ch
lst=["Rock", "Paper" , "Scissors"]
ch=ch(lst)

class Game (Tk):
    def __init__(self):
        super().__init__()
        self.title("calculator")
        self.geometry("381x389")
        self.config(bg="black")
                
        self.var=IntVar()
        # create radiobuttons
        self.r1=Radiobutton(self, text="Rock", variable=self.var, value=1, command=self.won
                            , bg="black", fg="white")
        self.r1.pack()
        self.r2=Radiobutton(self, text="Paper", variable=self.var, value=2 , command=self.won
                            , bg="black", fg="white")
        self.r2.pack()
        self.r3=Radiobutton(self, text="Scissors", variable=self.var, value=3 , command=self.won
                            , bg="black", fg="white")
        self.r3.pack()

    def won(self):
        """it is a function for showing result
        """
        v=self.var.get()
        if v==1 and ch=="Rock" or v==2 and ch=="Paper" or v== 3 and ch=="Scissors":
            lbl=Label(self, text="you and computer chose option "+ str(v)
                      , bg="black", fg="white")
            lbl.pack()    
        elif ch=="Rock" and v==3 or ch=="Paper"and v==1 or ch=="Scissors" and v==2:
            lbl=Label(self, text="you chose option " + str(v) +"\n"+ " and computer chose option "+ ch+"\n so computer won"
                      , bg="black", fg="white") 
            lbl.pack()
        elif v==1 and ch=="Scissors" or v==2 and ch=="Rock" or v==3 and ch=="Paper" :
            lbl=Label(self, text="you chose option " + str(v) + "\n"+" and computer chose option "+ ch+"\n so you won" 
                      , bg="black", fg="white") 
            lbl.pack()
              
game=Game()
game.mainloop()