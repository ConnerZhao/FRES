from tkinter import *

def mainScreen():
    main_screen = Tk()
    main_screen.title("F.R.E.S")
    main_screen.mainloop()

#choose to see message or scan face
Label(text="Face Recognition Emotional Support",bg = "orange",width="300", height="2").pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()

Button(text="Scan",height="2",width="30").pack()
Label(text="").pack()

Button(text="Message",height="2",width="30").pack()

mainScreen()