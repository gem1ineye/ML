from tkinter import *
from tkmacosx import *   # Optional for better styling on macOS

# -----------------------------------------
# Tkinter: Scale, Spinbox, and Scrollbar Example
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Scale, Spinbox, and Scrollbar Example")

# -----------------------------------------
# Scale Widget
# -----------------------------------------
# The Scale widget allows the user to select a numeric value by sliding a bar.
# 'variable' connects the widget to a control variable (e.g., IntVar).
# 'orient' defines the orientation — can be HORIZONTAL or VERTICAL.

var = IntVar(value=20)   # Control variable for the Scale
s1 = Scale(
    win,
    from_=0, to=100,          # Range of values
    variable=var,             # Linked variable
    orient='horizontal',      # Horizontal slider
    label='Select Value',     # Optional label above the slider
    length=300                # Slider length in pixels
)
s1.pack(pady=10)

# -----------------------------------------
# Spinbox Widget
# -----------------------------------------
# The Spinbox provides up/down arrows for selecting numeric or formatted values.
# 'format' controls number formatting (e.g., number of decimal places).

s2 = Spinbox(
    win,
    from_=0, to=100,          # Range of values
    format='%2.5f',           # Floating-point precision
    increment=0.5              # Step value between spins
)
s2.pack(pady=10)

# -----------------------------------------
# Scrollbar + Text Widget
# -----------------------------------------
# Scrollbar widgets are linked to scrollable widgets like Text or Canvas.
# 'orient' defines scroll direction (vertical or horizontal).

sb1 = Scrollbar(win, orient='vertical')  # Create vertical scrollbar
t1 = Text(win, wrap='word', width=40, height=10)  # Create text area

# Place Scrollbar and Text properly
sb1.pack(side=RIGHT, fill=Y)
t1.pack(side=LEFT, fill=BOTH, expand=True)

# Connect Scrollbar and Text widget to work together
t1.config(yscrollcommand=sb1.set)   # When text scrolls → update scrollbar
sb1.config(command=t1.yview)        # When scrollbar moves → scroll text

# -----------------------------------------
# Start the Tkinter Event Loop
# -----------------------------------------
win.mainloop()
