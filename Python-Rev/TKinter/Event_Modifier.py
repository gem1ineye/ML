from tkinter import *

# -----------------------------------------
# Tkinter Event Binding: Instance, Class & Global
# -----------------------------------------
# Tkinter lets you bind events at 3 levels:
# 1️⃣ Instance-Level → affects only one widget.
# 2️⃣ Class-Level → affects all widgets of a specific type (e.g., all Entry widgets).
# 3️⃣ Application-Level (Global) → affects the entire window/application.

# -----------------------------------------
# Event Handler Function
# -----------------------------------------
def fun(event, msg):
    """
    Event handler that triggers when the associated event occurs.
    - 'event' → carries event details (x/y position, widget source, etc.)
    - 'msg'   → custom message passed through lambda
    """
    print(msg)

# -----------------------------------------
# Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Event Binding Example")

# -----------------------------------------
# Entry Widgets (Event Sources)
# -----------------------------------------
e = Entry(win, bg='black', fg='skyblue')
e.place(x=400, y=100, width=200, height=50)

e1 = Entry(win, bg='blue', fg='pink')
e1.place(x=400, y=200, width=200, height=50)

# -----------------------------------------
# 1️⃣ Instance-Level Bindings (specific widget)
# -----------------------------------------
# Each of these events applies ONLY to the first Entry widget `e`

# Shift + Left Click
e.bind('<Shift-Button-1>', lambda event: fun(event, 'Shift + Left Button Clicked'))

# Middle Click (or Right Click if your mouse uses Button-3)
e.bind('<Button-2>', lambda event: fun(event, 'Middle Button Clicked'))

# Double Left Click
e.bind('<Double-Button-1>', lambda event: fun(event, 'Double Left Button Clicked'))

# -----------------------------------------
# 2️⃣ Class-Level Binding
# -----------------------------------------
# bind_class() → applies the event to all widgets of the same class/type.
# Here, 'Entry' means this applies to *all Entry widgets*.
win.bind_class('Entry', '<Button-1>', lambda event: fun(event, 'Class-Level: Entry Clicked'))

# -----------------------------------------
# 3️⃣ Application-Level (Global) Binding
# -----------------------------------------
# bind_all() → applies event globally to ALL widgets in the app.
# Here, any Shift + Middle Click triggers across all widgets.
win.bind_all('<Shift-Button-2>', lambda event: fun(event, 'Global: Shift + Middle Click Triggered'))

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
