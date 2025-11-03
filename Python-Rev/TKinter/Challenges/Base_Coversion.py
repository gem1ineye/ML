from tkinter import *
from tkinter.font import Font

# Create the main window
win = Tk()
win.geometry('600x400')   # width x height of the window

def update_base():
    # read the global value variable and update the label based on the selected base
    if base_type.get() == 0:          # Decimal
        lb1['text'] = str(value)
    elif base_type.get() == 1:        # Binary
        lb1['text'] = format(value, 'b')  # convert to binary string

fnt = Font(size=15)
value = 35

lb1 = Label(win, text=str(value), font=('Times New Roman', 45), fg='yellow', bg='black')
lb1.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

base_type = IntVar(value=0)

rbn1 = Radiobutton(win, text='Decimal', font=fnt, variable=base_type, value=0, command=update_base)
rbn1.grid(row=1, column=0, padx=10, pady=10)

rbn2 = Radiobutton(win, text='Binary', font=fnt, variable=base_type, value=1, command=update_base)
rbn2.grid(row=1, column=1, padx=10, pady=10)

win.mainloop()
