from tkinter import *
from tkmacosx import *           # Optional — improves UI rendering on macOS
import tkinter.messagebox as msg # Import messagebox module for dialogs

# -----------------------------------------
# Tkinter: Message Box Example
# -----------------------------------------
# This program demonstrates:
# ✅ How to display a Yes/No dialog box
# ✅ How to capture the user’s response

# -----------------------------------------
# Event Handler Function
# -----------------------------------------
def myHandler():
    """
    Triggered when the button is clicked.
    Displays a confirmation message box and prints the user's response.
    """
    # askyesno() → Displays a Yes/No popup dialog
    # Returns: True if "Yes" clicked, False if "No" clicked
    ans = msg.askyesno('My', 'Do you want to continue?')
    print(ans)   # Output: True or False

# -----------------------------------------
# Main Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Message Box Example")

# -----------------------------------------
# Button Widget
# -----------------------------------------
btn1 = Button(win, text='Click Me', command=myHandler)
btn1.pack(pady=50)

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
