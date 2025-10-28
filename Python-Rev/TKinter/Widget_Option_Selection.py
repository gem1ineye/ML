from tkinter import *
from tkmacosx import *  # Optional — improves button & widget appearance on macOS

# -----------------------------------------
# Tkinter GUI Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')   # Set window size: width x height
win.title('Selection Customization Example')

# -----------------------------------------
# Entry Widget
# -----------------------------------------
# 'selectforeground' → text color when selected
# 'selectbackground' → background color of selected text
# 'selectborderwidth' → border width around selection (visible on some OS)
e1 = Entry(
    win,
    selectforeground='yellow',
    selectbackground='red',
    selectborderwidth=10
)
e1.pack(pady=5)

# -----------------------------------------
# Text Widget
# -----------------------------------------
# 'exportselection=False' ensures that selection stays active
# even when another widget (like Listbox) is clicked.
t1 = Text(
    win,
    height=5,
    selectforeground='yellow',
    selectbackground='red',
    exportselection=False
)
t1.pack(pady=5)

# -----------------------------------------
# Listbox Widget
# -----------------------------------------
# 'exportselection=False' prevents Tkinter from removing selection
# when another widget gets focus (useful for multi-widget selection UIs).
lb1 = Listbox(
    win,
    selectbackground='red',
    selectforeground='yellow',
    selectborderwidth=10,
    exportselection=False
)
lb1.insert(0, 'Python')
lb1.insert(1, 'Tkinter')
lb1.insert(2, 'FastAPI')
lb1.insert(3, 'Django')
lb1.pack(pady=5)

# -----------------------------------------
# Start Tkinter Main Loop
# -----------------------------------------
win.mainloop()
