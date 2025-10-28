from tkinter import *

from tkmacosx import *

# Create the main window
win = Tk()
win.geometry('600x400')   # width x height of the window

# Create a button widget
b1 = Button(
    win,                  # parent window
    text='Hello',         # text on the button
    bg='red',           # background color
    fg='white',           # text color (foreground)
    relief=GROOVE,         # gives the button a raised 3D look
    overrelief=SUNKEN,
    bd=10
)
b1.pack()                 # places the button in the window (default center)

# Run the GUI loop
win.mainloop()
