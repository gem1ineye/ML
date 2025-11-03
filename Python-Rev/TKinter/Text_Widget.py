from tkinter import *
from tkmacosx import *   # Optional — improves macOS widget rendering

# -----------------------------------------
# Tkinter: Undo/Redo with Scrollbar in Text Widget
# -----------------------------------------
# This program demonstrates:
# ✅ Scrollbar integration with Text widget
# ✅ Undo / Redo operations using buttons

# -----------------------------------------
# Event Handlers
# -----------------------------------------
def myHandler1():
    """Undo the last text edit action."""
    txt1.edit_undo()   # Reverses the most recent change

def myHandler2():
    """Redo the previously undone text edit action."""
    txt1.edit_redo()   # Re-applies the undone change

# -----------------------------------------
# Main Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Undo / Redo Text Editor")

# -----------------------------------------
# Scrollbar Setup
# -----------------------------------------
sc1 = Scrollbar(win, orient=VERTICAL)
sc1.pack(side=RIGHT, fill=Y)

# -----------------------------------------
# Text Widget Setup
# -----------------------------------------
# 'undo=True' enables built-in undo/redo support
# 'yscrollcommand' links Text widget’s scrolling to Scrollbar
txt1 = Text(
    win,
    undo=True,
    yscrollcommand=sc1.set,
    wrap=WORD,
    font=('Consolas', 12),
    width=60,
    height=15
)
txt1.pack(side=LEFT, fill=BOTH, expand=True)

# Connect Scrollbar with Text widget
sc1.config(command=txt1.yview)

# -----------------------------------------
# Buttons for Undo / Redo
# -----------------------------------------
btn1 = Button(win, text='Undo', command=myHandler1, bg='lightblue')
btn1.pack(pady=5)

btn2 = Button(win, text='Redo', command=myHandler2, bg='lightgreen')
btn2.pack(pady=5)

# -----------------------------------------
# Run Tkinter Event Loop
# -----------------------------------------
win.mainloop()
