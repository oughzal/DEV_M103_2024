import tkinter as tk
from tkinter import ttk, messagebox

# Fonction appelée par le bouton "Soumettre"
def soumettre():
    # Récupérer les données des widgets
    texte = entry.get()
    choix_check = var_check.get()
    choix_radio = var_radio.get()
    valeur_spinbox = spinbox.get()
    valeur_scale = scale.get()
    selection_listbox = listbox.get(listbox.curselection()) if listbox.curselection() else "Aucun"
    selection_combobox = combobox.get()

    # Afficher un résumé des choix
    message = f"""
    Texte saisi : {texte}
    Checkbutton : {'Activé' if choix_check else 'Désactivé'}
    Radiobutton : {choix_radio}
    Spinbox : {valeur_spinbox}
    Scale : {valeur_scale}
    Listbox : {selection_listbox}
    Combobox : {selection_combobox}
    """
    messagebox.showinfo("Résumé", message)

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Widgets Tkinter")
fenetre.geometry("600x500")

# Création d'un frame pour organiser les widgets
frame = tk.Frame(fenetre)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Label et Entry
tk.Label(frame, text="Texte :", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=1, padx=5, pady=5)

# Checkbutton
var_check = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, text="Option", variable=var_check)
checkbutton.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

# Radiobuttons
tk.Label(frame, text="Choix :", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
var_radio = tk.StringVar(value="Option 1")
tk.Radiobutton(frame, text="Option 1", variable=var_radio, value="Option 1").grid(row=2, column=1, sticky="w", padx=5)
tk.Radiobutton(frame, text="Option 2", variable=var_radio, value="Option 2").grid(row=3, column=1, sticky="w", padx=5)

# Spinbox
tk.Label(frame, text="Nombre :", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
spinbox = tk.Spinbox(frame, from_=0, to=100, width=5)
spinbox.grid(row=4, column=1, sticky="w", padx=5, pady=5)

# Scale
tk.Label(frame, text="Valeur :", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
scale = tk.Scale(frame, from_=0, to=100, orient="horizontal")
scale.grid(row=5, column=1, sticky="w", padx=5, pady=5)

# Listbox
tk.Label(frame, text="Liste :", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
listbox = tk.Listbox(frame, height=4, selectmode="single")
listbox.grid(row=6, column=1, sticky="w", padx=5, pady=5)
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)

# Combobox
tk.Label(frame, text="Choix déroulant :", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=5, pady=5)
combobox = ttk.Combobox(frame, values=["Option A", "Option B", "Option C"], state="readonly")
combobox.grid(row=7, column=1, sticky="w", padx=5, pady=5)
combobox.set("Option A")  # Valeur par défaut

# Text (zone de texte)
tk.Label(frame, text="Zone de texte :", font=("Arial", 12)).grid(row=8, column=0, sticky="nw", padx=5, pady=5)
text = tk.Text(frame, height=5, width=40)
text.grid(row=8, column=1, sticky="w", padx=5, pady=5)

# Bouton "Soumettre"
button_soumettre = tk.Button(frame, text="Soumettre", command=soumettre, bg="lightblue")
button_soumettre.grid(row=9, column=0, columnspan=2, pady=10)

# Treeview
tk.Label(fenetre, text="Tableau :", font=("Arial", 14)).pack(pady=5)
columns = ("Colonne 1", "Colonne 2", "Colonne 3")
treeview = ttk.Treeview(fenetre, columns=columns, show="headings", height=5)
for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, anchor="center", width=120)
treeview.pack(padx=10, pady=10)

# Ajouter des données au Treeview
for i in range(1, 6):
    treeview.insert("", tk.END, values=(f"Valeur {i}", f"Valeur {i*2}", f"Valeur {i*3}"))

fenetre.mainloop()
