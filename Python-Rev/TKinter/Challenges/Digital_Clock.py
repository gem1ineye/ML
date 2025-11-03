from tkinter import *
import time
from tkmacosx import *

# Create the main window
win = Tk()
win.geometry('600x400')   # width x height of the window

def update_time():
    current_time = time.strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    lb['text'] = current_time
    lb.after(1000, update_time)  # update every 1 second

lb = Label(win, bg='red', fg='white', font=('Helvetica', 40, 'bold'))
lb.pack(fill=BOTH, expand=True)

update_time()  # start the clock

win.mainloop()
