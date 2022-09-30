# counter to keep track of the number of unclosed brackets
brc_count = 0

def clear_all(lbl, ent):
    global brc_count
    # clear entry
    ent.config(state = "normal")
    ent.delete(0, "end")
    ent.config(state = "readonly")
    # clear label
    lbl.config(text = "")
    # reset bracket counter
    brc_count = 0

def clear_entry(lbl, ent):
    if "=" in lbl.cget("text"):
        global brc_count
        # clear entry
        ent.config(state = "normal")
        ent.delete(0, "end")
        ent.config(state = "readonly")
        # clear label
        lbl.config(text = "")
        # reset bracket counter
        brc_count = 0
    else:
        # clear entry
        ent.config(state = "normal")
        ent.delete(0, "end")
        ent.config(state = "readonly")


def backspace(ent):
    # remove the last character in the entry
    ent.config(state = "normal")
    ent.delete(ent.index("end") - 1)
    ent.config(state = "readonly")

def prepare_ent(ent):
    # if the number is empty, add a 0
    if ent.get() == "":
        ent.insert("end", 0)
    # if the number contains a decimal point...
    elif "." in ent.get():
        # remove any 0s on the end...
        while ent.get()[-1] == "0":
            ent.delete(ent.index("end") - 1)
    
        # and then remove the decimal point if it is on the end
        if ent.get()[-1] == ".":
            ent.delete(ent.index("end") - 1)

def insert(lbl, ent, item):
    global brc_count
    ent.config(state = "normal")

    new_lbl = lbl.cget("text")

    if new_lbl != "" and new_lbl[-1] == "=":
        new_lbl = ""
    
    # if a natural number is inserted when only a 0 is present, replace the 0 with the natural number 
    if item != "." and ent.get() == "0": 
        ent.delete(0, "end")
        ent.insert("end", item)
    # if a decimal place is entered without another number before it, insert a 0 with the decimal
    elif item == "." and ent.get() == "":
        ent.insert("end", "0" + item)
    # if a decimal place is already present, dont add another one
    elif item == "." and "." in ent.get():
        None
    elif item == "(":
        # if the most recent character in the equation is a ")", dont insert the new bracket
        if new_lbl == "" or new_lbl[-1] != ")":
            new_lbl += "("
            brc_count += 1
    elif item == ")":
        if brc_count != 0:
            # if the last character in the label is a closing bracket, add just the new bracket without the number
            if new_lbl[-1] != ")":
                prepare_ent(ent)
                new_lbl += ent.get()

            new_lbl += ")"
            brc_count -= 1
            ent.delete(0, "end")
    else:
        ent.insert("end", item)
        
    lbl.config(text = new_lbl)

    ent.config(state = "readonly")
    ent.xview_moveto(1)

def operation(lbl, ent, op):
    ent.config(state = "normal")
    prepare_ent(ent)

    new_lbl = lbl.cget("text")
    
    # if the label is empty or has a "=", replace the label text wirh the number
    if new_lbl == "" or new_lbl[-1] == "=":
        new_lbl = ent.get()
        ent.delete(0, "end")
    # if the last character in label is a closing bracket, dont add the number to label
    elif new_lbl[-1] != ")":
        new_lbl += ent.get()
        ent.delete(0, "end")

    lbl.config(text = new_lbl + op)
    ent.config(state = "readonly")

def negate(lbl, ent):
    if lbl.cget("text") != "" and lbl.cget("text")[-1] == "=":
        lbl.config(text = "")

    ent.config(state = "normal")
    prepare_ent(ent)
    new_ent = 0 - float(ent.get())
    ent.delete(0, "end")
    ent.insert("end", new_ent)
    # prepare_ent() is called here again because an insignificant 0 and decimal point would be present if float() was called on an integer
    prepare_ent(ent)
    ent.config(state = "readonly")

def equals(lbl, ent):
    ent.config(state = "normal")
    prepare_ent(ent)

    if len(lbl.cget("text")) > 0 and lbl.cget("text")[-1] != "=":
        global brc_count

        new_lbl = lbl.cget("text")

        # if the label is empty or the last item is a ")", dont add the number to the end of the label
        if len(new_lbl) == 0 or new_lbl[-1] != ")":
            new_lbl += ent.get()

        # closes any unclosed brackets
        while (brc_count > 0):
            new_lbl += ")"
            brc_count -= 1
            
        ent.delete(0, "end")
        ent.insert("end", eval(new_lbl.replace("^", "**")))
        lbl.config(text = new_lbl + "=")

        
    ent.config(state = "readonly")