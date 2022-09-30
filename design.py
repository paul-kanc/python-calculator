import tkinter.ttk as ttk
import buttons as btn
from functools import partial

def style_equation_label(lbl):
    lbl.config(font = ("Comic Sans", 16),
               width = 11,
               foreground = "grey",
               background = "#303030",
               bd = 0,
               anchor = "se")

    lbl.grid(row = 0,
             column = 0,
             columnspan = 4,
             ipady = 5,
             padx = 1,
             sticky = "nesw")

def style_entry(ent):
    ent.config(state = "readonly", 
               font = ("Comic Sans", 32),
               width = 11,
               foreground = "white",
               background = "#303030",
               readonlybackground = "#303030",
               bd = 0,
               justify = "right")

    ent.grid(row = 1, 
             column = 0, 
             columnspan = 4, 
             ipady = 5, 
             padx = 1,
             sticky = "nesw")

def create_buttons(win, lbl, ent):
    style = ttk.Style()
    style.theme_use("alt")

    style.map("Main.TButton",
              foreground = [("!active", "white"), ("pressed", "white"), ("active", "white")],
              background = [("!active", "black"), ("pressed", "#707070"), ("active", "#505050")])
    style.configure("Main.TButton", 
                    font = ("Comic Sans", 24), 
                    width = 3)
    
    style.map("Light.TButton",
              foreground = [("!active", "white"), ("pressed", "white"), ("active", "white")],
              background = [("!active", "#303030"), ("pressed", "#707070"), ("active", "#505050")])
    style.configure("Light.TButton", 
                    font = ("Comic Sans", 24), 
                    width = 3)
    
    style.map("Accent.TButton",
              foreground = [("!active", "white"), ("pressed", "white"), ("active", "white")],
              background = [("!active", "#46007f"), ("pressed", "#922de5"), ("active", "#7e00e5")])
    style.configure("Accent.TButton", 
                    font = ("Comic Sans", 24), 
                    width = 3)

    r = 2
    ttk.Button(win, text = "+/-", style = "Light.TButton", command = partial(btn.negate, lbl, ent)).grid(row = r, column = 0, padx = 1, pady = 1)
    ttk.Button(win, text = "C", style = "Light.TButton", command = partial(btn.clear_all, lbl, ent)).grid(row = r, column = 1, padx = 1, pady = 1)
    ttk.Button(win, text = "CE", style = "Light.TButton", command = partial(btn.clear_entry, lbl, ent)).grid(row = r, column = 2, padx = 1, pady = 1)
    ttk.Button(win, text = "⟵", style = "Light.TButton", command = partial(btn.backspace, ent)).grid(row = r, column = 3, padx = 1, pady = 1)
    
    r = 3
    ttk.Button(win, text = "(", style = "Light.TButton", command = partial(btn.insert, lbl, ent, "(")).grid(row = r, column = 0, padx = 1, pady = 1)
    ttk.Button(win, text = ")", style = "Light.TButton", command = partial(btn.insert, lbl, ent, ")")).grid(row = r, column = 1, padx = 1, pady = 1)
    ttk.Button(win, text = "𝑥ʸ", style = "Light.TButton", command = partial(btn.operation, lbl, ent, "^")).grid(row = r, column = 2, padx = 1, pady = 1)
    ttk.Button(win, text = "÷", style = "Light.TButton", command = partial(btn.operation, lbl, ent, "/")).grid(row = r, column = 3, padx = 1, pady = 1)
    
    r = 4
    ttk.Button(win, text = "7", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "7")).grid(row = r, column = 0, padx = 1, pady = 1)
    ttk.Button(win, text = "8", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "8")).grid(row = r, column = 1, padx = 1, pady = 1)
    ttk.Button(win, text = "9", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "9")).grid(row = r, column = 2, padx = 1, pady = 1)
    ttk.Button(win, text = "x", style = "Light.TButton", command = partial(btn.operation, lbl, ent, "*")).grid(row = r, column = 3, padx = 1, pady = 1)
    
    r = 5
    ttk.Button(win, text = "4", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "4")).grid(row = r, column = 0, padx = 1, pady = 1)
    ttk.Button(win, text = "5", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "5")).grid(row = r, column = 1, padx = 1, pady = 1)
    ttk.Button(win, text = "6", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "6")).grid(row = r, column = 2, padx = 1, pady = 1)
    ttk.Button(win, text = "-", style = "Light.TButton", command = partial(btn.operation, lbl, ent, "-")).grid(row = r, column = 3, padx = 1, pady = 1)
    
    r = 6
    ttk.Button(win, text = "1", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "1")).grid(row = r, column = 0, padx = 1, pady = 1)
    ttk.Button(win, text = "2", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "2")).grid(row = r, column = 1, padx = 1, pady = 1)
    ttk.Button(win, text = "3", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "3")).grid(row = r, column = 2, padx = 1, pady = 1)
    ttk.Button(win, text = "+", style = "Light.TButton", command = partial(btn.operation, lbl, ent, "+")).grid(row = r, column = 3, padx = 1, pady = 1)
    
    r = 7
    ttk.Button(win, text = "0", style = "Main.TButton", command = partial(btn.insert, lbl, ent, "0")).grid(row = r, column = 0, columnspan = 2, padx = 1, pady = 1, sticky = "ew")
    ttk.Button(win, text = ".", style = "Main.TButton", command = partial(btn.insert, lbl, ent, ".")).grid(row = r, column = 2, padx = 1, pady = 1)
    ttk.Button(win, text = "=", style = "Accent.TButton", command = partial(btn.equals, lbl, ent)).grid(row = r, column = 3, padx = 1, pady = 1)

