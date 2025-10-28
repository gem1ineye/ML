from tkinter import *

# -----------------------------------------
# Tkinter: grid() Geometry Manager
# -----------------------------------------
# The grid() method places widgets in a tabular (row × column) structure.
# You can control:
#   - row / column position
#   - rowspan / columnspan
#   - internal & external padding
# It’s more precise than pack() when building form-like layouts.

win = Tk()
win.title("Grid Layout Example")

# -----------------------------------------
# Creating Labels (widgets)
# -----------------------------------------
l1 = Label(win, text='Label 1', bg='lightblue', fg='blue')
l2 = Label(win, text='Label 2', bg='lightblue', fg='blue')
l3 = Label(win, text='Label 3', bg='lightblue', fg='blue')
l4 = Label(win, text='Label 4', bg='lightblue', fg='blue')
l5 = Label(win, text='Label 5', bg='lightblue', fg='blue')
l6 = Label(win, text='Label 6', bg='lightblue', fg='blue')
l7 = Label(win, text='Label 7', bg='lightblue', fg='blue')
l8 = Label(win, text='Label 8', bg='lightblue', fg='blue')
l9 = Label(win, text='Label 9', bg='lightblue', fg='blue')

# -----------------------------------------
# Placing Labels Using grid()
# -----------------------------------------
# grid(row=r, column=c, padx= , pady= , rowspan= , columnspan= )

# Row 0
l1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)   # Spans across 2 columns
# l2.grid(row=0, column=1, padx=5, pady=5)               # Example if you want Label 2 visible
l3.grid(row=0, column=2, padx=5, pady=5)

# Row 1
l4.grid(row=1, column=0, rowspan=2, padx=5, pady=5)      # Spans 2 rows vertically
l5.grid(row=1, column=1, padx=5, pady=5)
l6.grid(row=1, column=2, padx=5, pady=5)

# Row 2
# l7.grid(row=2, column=0, padx=5, pady=5)               # Commented out intentionally
l8.grid(row=2, column=1, padx=5, pady=5)
l9.grid(row=2, column=2, padx=5, pady=5)

# -----------------------------------------
# Start Tkinter Main Loop
# -----------------------------------------
win.mainloop()
