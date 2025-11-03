from tkinter import *
from tkmacosx import *   # Optional — better button rendering on macOS

# -----------------------------------------
# Tkinter: Listbox with MULTIPLE Selection
# -----------------------------------------
# This example shows how to:
# 1️⃣ Create a Listbox with multiple selection mode
# 2️⃣ Get selected indices using .curselection()
# 3️⃣ Display the selection in an Entry widget

# -----------------------------------------
# Event Handler Function
# -----------------------------------------
def myhandler():
    """
    Triggered when the button is clicked.
    Fetches currently selected items (indices) from the Listbox
    and updates the Entry widget.
    """
    # Get indices of selected items (as a tuple)
    selected_indices = lst.curselection()

    # Retrieve the actual selected text values
    selected_items = [lst.get(i) for i in selected_indices]

    # Join selected items as a comma-separated string
    var.set(", ".join(selected_items))

# -----------------------------------------
# Tkinter Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Listbox Selection Example")

# -----------------------------------------
# Entry Widget — Displays Selected Items
# -----------------------------------------
var = StringVar()
ent1 = Entry(win, textvariable=var, width=40)
ent1.pack(pady=10)

# -----------------------------------------
# Listbox Widget — with Multiple Selection
# -----------------------------------------
# selectmode options:
# SINGLE → only one item
# BROWSE → drag to select one
# MULTIPLE → select multiple freely
# EXTENDED → allows Shift/Ctrl + click for range selection
lst = Listbox(win, selectmode=MULTIPLE, height=5)
lst.insert(0, "Python")
lst.insert(1, "C/C++")
lst.insert(2, "Java")
lst.insert(3, "JavaScript")
lst.insert(4, "Ruby")
lst.pack(pady=10)

# -----------------------------------------
# Button — Triggers Selection Display
# -----------------------------------------
bt1 = Button(win, text='Click Me', command=myhandler)
bt1.pack(pady=10)

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
