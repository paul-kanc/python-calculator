import tkinter as tk
import Design as dsn

win = tk.Tk()
win.title("Paul's Calculator")
win.resizable(False, False)
win.configure(bg = "#707070")

# label to display the current equation
lbl = tk.Label()
dsn.style_equation_label(lbl)

# entry to dislay the number to insert/the answer to the equation
ent = tk.Entry()
dsn.style_entry(ent)

# buttons to operate the calculator
dsn.create_buttons(win, lbl, ent)

win.mainloop()
