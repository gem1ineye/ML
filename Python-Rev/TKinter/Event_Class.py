from tkinter import *

# -----------------------------------------
# Event Object in Tkinter
# -----------------------------------------
# When an event (like a mouse click or key press) occurs,
# Tkinter automatically passes an 'event object' to the handler function.
# This 'event' contains all information about what triggered the event
# (mouse position, key pressed, widget source, etc.)

def my_handler(e):
    """
    Event handler for mouse click.
    The 'e' (event) object carries multiple attributes:
        e.x, e.y        → Coordinates inside the widget
        e.x_root, e.y_root → Coordinates on the full screen
        e.widget         → Widget that triggered the event
        e.type           → Type of event (e.g., ButtonPress)
        e.state          → Modifier key state (Shift, Ctrl, etc.)
    """
    print(e)                        # Prints event type summary (e.g., <ButtonPress event>)
    print("Modifier key state:", e.state)
    print("Mouse Position (Screen):", e.x_root, e.y_root)
    print("Mouse Position (Widget):", e.x, e.y)
    print("Widget Source:", e.widget)
    print('-' * 40)

# -----------------------------------------
# Window Setup
# -----------------------------------------
win = Tk()
win.title('My First App')
win.geometry('600x400')

# -----------------------------------------
# Entry Widget (Event Source)
# -----------------------------------------
ent = Entry(win)
ent.pack(pady=20)

# Bind left mouse button click to the handler
ent.bind('<Button-1>', my_handler)

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
