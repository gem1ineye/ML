from tkinter import *
from tkmacosx import *   # Optional — improves menu & button look on macOS

# -----------------------------------------
# Tkinter: Menu Bar Example
# -----------------------------------------
# This program demonstrates:
# ✅ How to create a Menu bar
# ✅ Add menu items (File menu)
# ✅ Attach commands to menu actions
# ✅ Insert text into a Text widget dynamically

# -----------------------------------------
# Event Handler Function
# -----------------------------------------
def myHandler():
    """
    Triggered when the 'New' menu option is clicked.
    Inserts 'Hello World' at the start of the Text widget.
    """
    # Insert text at position (line=1, column=0)
    tx.insert(1.0, 'Hello World\n')

# -----------------------------------------
# Main Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Menu Bar Example")

# -----------------------------------------
# Text Widget
# -----------------------------------------
# Acts as an editor area where text is inserted
tx = Text(win, font=('Consolas', 14))
tx.pack(fill=BOTH, expand=True)

# -----------------------------------------
# Menu Bar Setup
# -----------------------------------------
menubar = Menu(win)           # Create the main menu bar
win['menu'] = menubar         # Attach it to the window

# -----------------------------------------
# File Menu
# -----------------------------------------
file_menu = Menu(menubar, tearoff=0)  # tearoff=0 removes dashed line at top

# Add File menu to the menubar
menubar.add_cascade(label='File', menu=file_menu)

# Add menu items under 'File'
file_menu.add_command(label='New', command=myHandler)   # Calls myHandler
file_menu.add_command(label='Open')                     # Placeholder
file_menu.add_command(label='Save')                     # Another placeholder

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
