from tkinter import *
from tkinter.font import *   # For working with font objects
from tkmacosx import *       # Optional — improves UI consistency on macOS

# -----------------------------------------
# Tkinter: Dynamic Font Resizing Example
# -----------------------------------------
# This program allows you to control the font size of an Entry widget
# using a Scale slider.

# -----------------------------------------
# Event Handler Function
# -----------------------------------------
def myhandler(e):
    """
    This function is triggered every time the Scale slider moves.
    It reads the current scale value and updates the Entry widget's font size.
    """
    # Create a Font object with the new size from the Scale value
    f = Font(size=int(sc1.get()))   # Must convert to int for size
    
    # Update the Entry widget font dynamically
    ent['font'] = f

# -----------------------------------------
# Tkinter Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Font Size Controller")

# -----------------------------------------
# Entry Widget — Text Display
# -----------------------------------------
# 'textvariable' binds a StringVar so text can be dynamically updated if needed
var = StringVar(value="Hello World")
ent = Entry(win, textvariable=var, width=30, font=('Arial', 14))
ent.pack(pady=20)

# -----------------------------------------
# Scale Widget — Font Size Controller
# -----------------------------------------
# from_ → minimum value
# to → maximum value
# resolution → step size for each slider movement
# tickinterval → numeric marks on the scale
# command → function called on slider movement
sc1 = Scale(
    win,
    from_=0,
    to=100,
    resolution=5,       # Move in steps of 5
    tickinterval=10,    # Show scale ticks every 10 units
    showvalue=True,     # Display current scale value
    orient='horizontal',
    label='Adjust Font Size',
    command=myhandler   # Calls function when slider moves
)
sc1.pack(pady=20)

# -----------------------------------------
# Start Tkinter Main Event Loop
# -----------------------------------------
win.mainloop()
