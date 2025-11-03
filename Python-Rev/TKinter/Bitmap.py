from tkinter import *

from tkmacosx import *

# Create the main window
win = Tk()
win.geometry('600x400')   # width x height of the window

e1=Checkbutton(win,text='Click Me',bitmap='warning')
e1.pack()

                

# Run the GUI loop
win.mainloop()
