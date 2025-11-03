from tkinter import *
from tkmacosx import *   # Optional — improves macOS widget rendering

# -----------------------------------------
# Event Handler: Checkbox Action
# -----------------------------------------
def myhandler():
    """
    This function is called automatically whenever the Checkbutton state changes.
    It checks the value of 'var' (linked IntVar) to determine if the box is checked.
    """
    if var.get() == 1:   # 1 means checked, 0 means unchecked
        lb1['text'] = ch1['text']   # Display checkbox label text in Label
    else:
        lb1['text'] = 'Not Selected'  # Reset label text if unchecked


# -----------------------------------------
# Event Handler: Button Click
# -----------------------------------------
def butHandler():
    """
    This function is called when the button is clicked.
    'invoke()' programmatically toggles (clicks) the Checkbutton.
    """
    ch1.invoke()   # Triggers Checkbutton's action (like manual click)


# -----------------------------------------
# Tkinter Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Checkbutton Event Example")

# -----------------------------------------
# Label Widget — displays status
# -----------------------------------------
lb1 = Label(win, text='Hola', font=('Arial', 14))
lb1.pack(pady=10)

# -----------------------------------------
# Checkbutton Widget
# -----------------------------------------
# variable → stores the state (0 = unchecked, 1 = checked)
# command → callback function when state changes
var = IntVar()
ch1 = Checkbutton(
    win,
    text='Java',
    variable=var,
    command=myhandler,
    font=('Arial', 12)
)
ch1.pack(pady=10)

# -----------------------------------------
# Button Widget — triggers invoke() on Checkbutton
# -----------------------------------------
cb1 = Button(win, text='Click Me', command=butHandler)
cb1.pack(pady=10)

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
