import tkinter as tk

root = tk.Tk()
root.title("Sinup form")
root.iconbitmap("./ofppt.ico")
root.minsize(width=500,height=400)

def createEntry(text,row):
    global root
    variable = tk.StringVar()
    label = tk.Label(root, text=f"{text} :")
    label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(root, textvariable=variable, width=30)
    entry.grid(row=row, column=1, padx=5, pady=5, sticky="we")
    return variable

def createRadio(text,row,options):
    if not options : return
    global root
    variable = tk.StringVar()
    label = tk.Label(root, text=f"{text} :")
    label.grid(row=row, column=0, padx=5, pady=5, sticky="wn")
    frame = tk.Frame(root)
    frame.grid(row=row, column=1, padx=5, pady=5, sticky="we")
    variable = tk.StringVar(value=options[0])
    for r, option in enumerate(options):
        tk.Radiobutton(frame,text=option,variable=variable,value=option).grid(row=0, column=r, padx=5, pady=5, sticky="w")

    return variable

nom = createEntry("nom",0)
prenom = createEntry("prénom",1)
age = createEntry("age",2)
genre = createRadio("genre",3,["F","M"])
genre = createRadio("Niveau",4,["TS","T","Q","S","FQ"])
# column configugration
root.grid_columnconfigure(0,weight=0)
root.grid_columnconfigure(1,weight=1)



root.mainloop()