from tkinter import *
from tkinter.font import *      # For working with custom fonts
from tkmacosx import *          # Optional — improves button visuals on macOS

# -----------------------------------------
# Tkinter: Dynamic Font Styling Example
# -----------------------------------------
# This program demonstrates how to:
# ✅ Use Checkbuttons to toggle Bold, Italic, and Underline
# ✅ Dynamically update font styling using tkinter.font.Font class

# -----------------------------------------
# Event Handler — Update Label Font
# -----------------------------------------
def update_label():
    """
    Triggered whenever a Checkbutton is toggled.
    Reads the current states of bold, italic, and underline variables,
    and updates the Label’s font in real-time.
    """
    # Determine font weight (bold/normal)
    b = ['bold' if varbold.get() == 1 else 'normal'][0]
    
    # Determine font slant (italic/roman)
    i = ['italic' if varitl.get() == 1 else 'roman'][0]
    
    # Create a Font object with selected attributes
    fnt = Font(
        family='Times New Roman',
        size=45,
        weight=b,
        slant=i,
        underline=varunderline.get()  # 1 = Underline On, 0 = Off
    )
    
    # Apply updated font to the Label widget
    lbl1['font'] = fnt

# -----------------------------------------
# Main Window Setup
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Dynamic Font Styler")

# -----------------------------------------
# Label Widget (Text Display)
# -----------------------------------------
lbl1 = Label(
    win,
    text='Hello World',
    font=('Times New Roman', 45)
)
lbl1.grid(row=0, column=0, columnspan=3, pady=20)

# -----------------------------------------
# Bold Checkbutton
# -----------------------------------------
varbold = IntVar(value=0)  # Stores 1 if checked, 0 if unchecked
chk1 = Checkbutton(
    win,
    text='Bold',
    onvalue=1,
    offvalue=0,
    variable=varbold,
    command=update_label   # Calls function when toggled
)
chk1.grid(row=1, column=0, padx=10)

# -----------------------------------------
# Italic Checkbutton
# -----------------------------------------
varitl = IntVar(value=0)
chk2 = Checkbutton(
    win,
    text='Italic',
    onvalue=1,
    offvalue=0,
    variable=varitl,
    command=update_label
)
chk2.grid(row=1, column=1, padx=10)

# -----------------------------------------
# Underline Checkbutton
# -----------------------------------------
varunderline = IntVar(value=0)
chk3 = Checkbutton(
    win,
    text='Underline',
    onvalue=1,
    offvalue=0,
    variable=varunderline,
    command=update_label
)
chk3.grid(row=1, column=2, padx=10)

# -----------------------------------------
# Start Tkinter Main Loop
# -----------------------------------------
win.mainloop()
