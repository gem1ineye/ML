from tkinter import *
from tkmacosx import *   # Optional — better UI consistency on macOS

# -----------------------------------------
# Tkinter Text Wrapping and Line Spacing
# -----------------------------------------
win = Tk()
win.geometry('600x400')
win.title("Text Wrapping & Spacing Example")

# -----------------------------------------
# Label Widget — Demonstrating Text Wrapping
# -----------------------------------------
# wraplength → Defines at what width (in pixels) text should wrap to the next line.
# width → Width of the label in text units (not pixels).
# You can control text wrapping to avoid overflow beyond the window.

l1 = Label(
    win,
    text="Hello my friend Rodrigo, nice to meet you today.",
    width=100,
    wraplength=100,    # Text wraps every 100px width
    bg='lightyellow',
    fg='black'
)
l1.pack(pady=10)

# -----------------------------------------
# Text Widget — Demonstrating Line Spacing
# -----------------------------------------
# spacing1 → Space before the first line of a paragraph
# spacing2 → Space between wrapped lines within the same paragraph
# spacing3 → Space after the last line of a paragraph

e1 = Text(
    win,
    height=8,
    spacing1=20,   # Space before the first line (top margin)
    spacing2=10,   # Space between lines (line spacing)
    spacing3=15,   # Space after the last line (bottom margin)
    wrap=WORD,     # Wrap text at word boundaries (options: CHAR, WORD, NONE)
    bg='lightblue'
)
e1.pack(padx=20, pady=10, fill=BOTH, expand=True)

# Insert sample text for demonstration
e1.insert(END, "This is a demonstration of text spacing.\n"
               "spacing1 adds margin before the first line.\n"
               "spacing2 adds space between wrapped lines.\n"
               "spacing3 adds space after the paragraph.\n")

# -----------------------------------------
# Run the Tkinter Event Loop
# -----------------------------------------
win.mainloop()
