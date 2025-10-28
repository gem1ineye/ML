from tkinter import *
from tkinter.messagebox import *

def my_handler(e):
    showinfo('My_info',lbl.cget('bg'))
    lbl.config(bg='white')


win=Tk()
win.title('My FIrst Application')
win.geometry('600x400')

lbl=Label(win,text='blue color',bg='red',width=20,height=2)
lbl.pack()
lbl.bind('<Button-1>',my_handler)



win.mainloop()