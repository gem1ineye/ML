from tkinter import *

# -----------------------------------------
# Tkinter Geometry Manager: place()
# -----------------------------------------
# The place() method positions widgets by exact coordinates or relative positions.
# It’s the most precise geometry manager — ideal for pixel-perfect layouts.

win = Tk()
win.title('My Application')
win.geometry('600x400')   # Window size: width=600, height=400

# -----------------------------------------
# Creating Buttons
# -----------------------------------------
Button1 = Button(win, text='Button1')
Button2 = Button(win, text='Button2')
Button3 = Button(win, text='Button3')

# -----------------------------------------
# Placing Buttons using absolute coordinates
# -----------------------------------------
Button1.place(x=100, y=100, width=100, height=100)
# ✅ x, y → absolute coordinates (in pixels) from top-left corner of window
# ✅ width, height → exact size in pixels

Button2.place(x=200, y=100, width=100, height=50)
# Another button placed 100px to the right, smaller height

# -----------------------------------------
# Using relative positioning (percentage of window)
# -----------------------------------------
Button3.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.1)
# ✅ relx, rely → relative position (0.0 = 0%, 1.0 = 100%)
# ✅ relwidth, relheight → relative size (% of total window)
# This button appears centered (50% x, 50% y) and scales with window size

# -----------------------------------------
# Run the Tkinter main loop
# -----------------------------------------
win.mainloop()
