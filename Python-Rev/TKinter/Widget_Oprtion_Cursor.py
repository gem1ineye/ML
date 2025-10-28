from tkinter import *
from tkmacosx import *   # Optional for macOS UI improvements

# -----------------------------------------
# Tkinter: Insert Cursor Customization in Text Widget
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Insert Cursor Example")

# -----------------------------------------
# Text Widget Configuration
# -----------------------------------------
# Parameters explained:
# -----------------------------------------
# insertbackground → color of the insertion cursor (caret)
# insertwidth → width/thickness of the caret (in pixels)
# insertborderwidth → extra border width around caret (visible only on some systems)
# insertontime → blinking "on" duration in milliseconds (controls blink speed)
# cursor → mouse cursor icon when hovering over the Text widget

e1 = Text(
    win,
    insertbackground='red',   # Color of blinking cursor
    insertwidth=10,           # Make cursor thick
    insertborderwidth=5,      # Border around cursor (cosmetic)
    insertontime=100,         # Cursor blink interval (on-time in ms)
    cursor='pencil'           # Mouse pointer shape (e.g., 'arrow', 'cross', 'pencil')
)
e1.pack(pady=20)

# -----------------------------------------
# Start Tkinter Event Loop
# -----------------------------------------
win.mainloop()
