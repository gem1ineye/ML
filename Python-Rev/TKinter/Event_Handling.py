# -----------------------------------------
# Introduction to Event and Event Handling in Tkinter
# -----------------------------------------
# Event Handling = Responding to user actions like button clicks,
# key presses, mouse movements, etc.
# The 'command' parameter or 'bind()' method is used to handle events.

from tkinter import *

# -----------------------------------------
# Event Handler Function
# -----------------------------------------
def fun(msg):
    # This function will be called when the button is clicked
    print(msg)

# -----------------------------------------
# Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')     # Set window size

# -----------------------------------------
# Button Widget with Event Binding
# -----------------------------------------
# The 'command' parameter links a function to the button click event
# 'lambda' is used to pass an argument to the function
b1 = Button(win, text='My Button', command=lambda: fun('Button is clicked!'))
b1.pack(pady=20)

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
