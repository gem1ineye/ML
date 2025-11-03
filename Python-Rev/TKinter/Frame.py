from tkinter import *

from tkmacosx import *

# Create the main window
win = Tk()
win.geometry('600x400')   # width x height of the window


f1=Frame(win,bg='pink',width=300)
f1.pack(side=LEFT,fill=Y)

f2=Frame(win,bg='blue',width=300)
f2.pack(side=RIGHT,fill=Y)

b1=Button(f1,text='btn1',bg='green')
b1.pack()

                

# Run the GUI loop
win.mainloop()
