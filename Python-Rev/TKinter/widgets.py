from tkinter import *

# -----------------------------------------
# Tkinter GUI Window Setup
# -----------------------------------------
win = Tk()   # Create the main GUI window

win.title('My First Application')  # Set window title
win.geometry('600x400+300+100')    # Width=600, Height=400, X=300, Y=100 offset
win.resizable(False, True)         # Fixed width, resizable height
win.attributes('-alpha', 0.9)      # Slightly transparent window (90% opacity)


# -----------------------------------------
# Tkinter Widgets
# -----------------------------------------

# 1️⃣ Label — displays static text
win_label = Label(win, text='Hola Amigo')
win_label.pack()   # .pack() places widget automatically in the window

# 2️⃣ Entry — single-line text input
win_entry = Entry(win)
win_entry.pack()

# 3️⃣ Button — triggers actions when clicked
win_button = Button(win, text='Click Me')
win_button.pack()

# 4️⃣ Text — multi-line text input area
text_window = Text(win, width=30, height=10)
text_window.pack()

# 5️⃣ Checkbutton — toggle option (checkbox)
win_checkbox = Checkbutton(win, text='Yes')
win_checkbox.pack()

# 6️⃣ Radiobuttons — single-choice options
# 'variable' should be a shared variable (e.g., IntVar/StringVar) for proper grouping
v1 = IntVar()
win_radio1 = Radiobutton(win, text='I will do', variable=v1, value=1)
win_radio1.pack()
win_radio2 = Radiobutton(win, text='I will not do', variable=v1, value=2)
win_radio2.pack()

# 7️⃣ OptionMenu — dropdown selection menu
v = StringVar()   # holds selected option value
win_option = OptionMenu(win, v, *('Java', 'C++', 'Python'))
win_option.pack()

# 8️⃣ Scale — slider for numeric values
win_scale = Scale(win, from_=0, to=100)
win_scale.pack()


# -----------------------------------------
# Tkinter Mainloop — keeps window open
# -----------------------------------------
win.mainloop()
