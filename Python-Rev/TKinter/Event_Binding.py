from tkinter import *

# -----------------------------------------
# Instance-Level Event Binding
# -----------------------------------------
# Event binding connects specific widget events (like mouse clicks or key presses)
# to custom handler functions.

def fun(event, msg):
    """
    Event handler function.
    'event' parameter automatically receives event info (like x/y position, widget, etc.)
    'msg' is a custom message we’re passing via lambda.
    """
    print(msg)

# ----------------------------------------- 
# Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Event Binding Example")

# -----------------------------------------
# Entry Widget (acts as event source)
# -----------------------------------------
e = Entry(win, bg='black', fg='skyblue')
e.place(x=400, y=100, width=200, height=50)

# -----------------------------------------
# Binding Events to the Entry Widget
# -----------------------------------------
# <Button-1> → Left mouse click
# <Button-2> → Middle mouse button click (in some systems, right-click = <Button-3>)

# Use lambda to pass custom message + event argument together
e.bind('<Button-1>', lambda event: fun(event, 'Left Button Clicked'))
e.bind('<Button-2>', lambda event: fun(event, 'Middle Button Clicked'))  # or Right depending on OS
# Tip: Try <Button-3> if Button-2 doesn’t trigger (on most laptops, right-click = Button-3)

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
