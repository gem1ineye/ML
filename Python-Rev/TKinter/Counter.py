from tkinter import *
from tkmacosx import *   # Optional — improves button appearance on macOS

# -----------------------------------------
# Event Handler Function
# -----------------------------------------
def myHandler():
    """
    Called when the button is clicked.
    Increments the integer value stored in 'var' by 1.
    Since 'var' is linked to the Label, the display updates automatically.
    """
    var.set(var.get() + 1)   # get() reads current value, set() updates it

# -----------------------------------------
# Tkinter Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Dynamic Label with IntVar")

# -----------------------------------------
# Tkinter Variable
# -----------------------------------------
# IntVar() is a special Tkinter variable class that stores integer values.
# It automatically updates any widget linked to it (e.g., Label, Checkbutton).
var = IntVar(value=0)   # Initial value is 0

# -----------------------------------------
# Label Widget (linked to IntVar)
# -----------------------------------------
# The 'textvariable' parameter binds the Label text to 'var'.
# Whenever 'var' changes, the Label automatically updates.
lb1 = Label(win, textvariable=var, font=('Arial', 18))
lb1.pack(pady=20)

# -----------------------------------------
# Button Widget
# -----------------------------------------
# Clicking this button calls 'myHandler()', which increments the value.
bt1 = Button(win, text='Click Me', command=myHandler)
bt1.pack(pady=10)

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
