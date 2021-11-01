import tkinter as tk 
from tkinter import *
from tkinter import messagebox

def mainScreen():
    main_screen = Tk()
    main_screen.title("F.R.E.S")
    main_screen.mainloop()

class Buttons():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x100")
        
        Label(text="Face Recognition Emotional Support",bg = "orange",width="300", height="2").pack()
        Label(text="").pack()
        Label(text="").pack()
        self.butt1 = Button(self.root,
                                text="Scan",
                                height="2",
                                width="30",
                                command=''
                                )
  
        self.butt2 = Button(self.root,text="Message",height="2",width="30")

        self.butt1.pack(side=tk.TOP)
        Label(text="").pack()
        self.butt2.pack(side=tk.TOP)
        self.root.mainloop()
    def showInfo(self):
        self.butt1['command'] = messagebox.showinfo( "Look at the Camera", "Press q to stop scanning")
        
test = Buttons()
mainScreen()