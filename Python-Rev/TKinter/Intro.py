from tkinter import *
# from tkmacosx import *

# -----------------------------------------
# Tkinter Window Setup (Basic GUI Window)
# -----------------------------------------

# Create the main window object
win = Tk()   # Tk() initializes the main GUI window (root window)

# Set window title
win.title('My First Application')

# Set window size and position
# Format: 'widthxheight+x_offset+y_offset'
win.geometry('600x400+300+100')   # 600x400 window placed 300px right, 100px down from screen top-left

# Control whether the window is resizable
# (width_resizable, height_resizable)
win.resizable(False, True)   # ❌ Width fixed, ✅ Height can be resized

# Set window transparency (alpha value)
# Range: 0.0 (fully transparent) → 1.0 (fully opaque)
win.attributes('-alpha', 0.9)   # Slightly transparent window

# Start the Tkinter event loop (keeps window open)
win.mainloop()
