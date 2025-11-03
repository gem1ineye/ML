from tkinter import *
from tkmacosx import *   # Optional – improves macOS widget rendering

# -----------------------------------------
# Tkinter: Entry Validation, Cursor, and Selection
# -----------------------------------------
# This program validates Entry input (blocks alphabets),
# sets focus automatically, controls the cursor, and highlights text.

# -----------------------------------------
# Validation Function
# -----------------------------------------
def myHandler(txt):
    """
    Called on every keypress inside the Entry widget.
    '%S' (passed automatically by Tkinter) represents the character being typed.
    
    Returns:
        False → Reject input (block character)
        True  → Allow input
    """
    if txt.isalpha():   # Reject alphabetic characters
        return False
    else:
        return True     # Allow numbers/symbols

# -----------------------------------------
# Tkinter Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Entry Validation Example")

# -----------------------------------------
# Register Validation Command
# -----------------------------------------
# 'register()' converts Python function into a Tcl/Tk-compatible callback
# '%S' passes the typed character to the function
handler = (win.register(myHandler), '%S')

# -----------------------------------------
# Entry Widget Setup
# -----------------------------------------
# validate='key' → validation occurs on every keystroke
# validatecommand → function that decides if keypress is accepted
var = StringVar(value="Hello Gem1ineye")

et1 = Entry(
    win,
    textvariable=var,
    validate='key',
    validatecommand=handler,
    font=('Arial', 14),
    fg='blue',
    justify='center'
)
et1.pack(pady=20)

# -----------------------------------------
# Cursor and Selection Control
# -----------------------------------------
et1.focus()            # Set focus automatically to Entry box
et1.icursor(4)         # Place cursor at position index 4 (0-based)
et1.select_range(2, 7) # Highlight text from index 2 to 6 (7 excluded)

# -----------------------------------------
# Start Tkinter Main Loop
# -----------------------------------------
win.mainloop()
