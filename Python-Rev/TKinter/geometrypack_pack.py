from tkinter import *

# -----------------------------------------
# Tkinter Geometry Manager: pack()
# -----------------------------------------
# pack() is one of the three geometry managers in Tkinter:
#   1️⃣ pack()  → simple auto placement (stacking)
#   2️⃣ grid()  → table-style layout (rows & columns)
#   3️⃣ place() → exact coordinate-based layout
# Here, we’re experimenting with pack() parameters.

win = Tk()
win.title("Pack Geometry Example")

# -----------------------------------------
# Example 1 (commented): Using 'side' option
# -----------------------------------------
'''
l1 = Label(win, text='Label One', bg='yellow', fg='red')
l1.pack(side=LEFT)     # Place label on the left edge

l2 = Label(win, text='Label Two', bg='yellow', fg='red')
l2.pack(side=TOP)      # Place label on top

l3 = Label(win, text='Label Three', bg='yellow', fg='red')
l3.pack(side=RIGHT)    # Place label on right edge
'''

# -----------------------------------------
# Example 2 (commented): Using 'anchor' option
# -----------------------------------------
'''
l1 = Label(win, text='Label One', bg='yellow', fg='red')
l1.pack(anchor=NW)     # NW = Top-Left corner

l2 = Label(win, text='Label Two', bg='yellow', fg='red')
l2.pack(anchor=S)      # S = Bottom-Center

l3 = Label(win, text='Label Three', bg='yellow', fg='red')
l3.pack(anchor=SE)     # SE = Bottom-Right corner
'''

# -----------------------------------------
# Example 3 (active): Using padding options
# -----------------------------------------
# padx / pady → external padding (space outside the widget)
# ipadx / ipady → internal padding (space inside the widget)
l1 = Label(win, text='Label One', bg='yellow', fg='red')
l1.pack(padx=2, pady=2, ipadx=2, ipady=2)

l2 = Label(win, text='Label Two', bg='yellow', fg='red')
l2.pack(padx=2, pady=2, ipadx=2, ipady=2)

l3 = Label(win, text='Label Three', bg='yellow', fg='red')
l3.pack(padx=2, pady=2, ipadx=2, ipady=2)


# -----------------------------------------
# Run the Tkinter main event loop
# -----------------------------------------
win.mainloop()
