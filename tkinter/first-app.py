import tkinter as tk
from tkinter import ttk, messagebox

# Fonctionnalités CRUD
def ajouter():
    # Récupérer les données saisies
    nom = entry_nom.get()
    age = entry_age.get()
    ville = entry_ville.get()

    # Vérifier que tous les champs sont remplis
    if not nom or not age or not ville:
        messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")
        return

    # Ajouter une nouvelle ligne dans le Treeview
    tree.insert("", tk.END, values=(nom, age, ville))
    # Réinitialiser les champs
    entry_nom.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_ville.delete(0, tk.END)

def supprimer():
    # Récupérer la sélection actuelle
    selection = tree.selection()
    if not selection:
        messagebox.showwarning("Sélection vide", "Veuillez sélectionner une ligne à supprimer.")
        return

    # Supprimer la ligne sélectionnée
    for item in selection:
        tree.delete(item)

def modifier():
    # Récupérer la sélection actuelle
    selection = tree.selection()
    if not selection:
        messagebox.showwarning("Sélection vide", "Veuillez sélectionner une ligne à modifier.")
        return

    # Récupérer les données saisies
    nom = entry_nom.get()
    age = entry_age.get()
    ville = entry_ville.get()

    # Vérifier que tous les champs sont remplis
    if not nom or not age or not ville:
        messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")
        return

    # Modifier la ligne sélectionnée
    for item in selection:
        tree.item(item, values=(nom, age, ville))
    
    # Réinitialiser les champs
    entry_nom.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_ville.delete(0, tk.END)

def remplir_champs(event):
    # Remplir les champs avec les données de la ligne sélectionnée
    selection = tree.selection()
    if selection:
        item = tree.item(selection[0])  # Récupérer le premier élément sélectionné
        values = item["values"]
        entry_nom.delete(0, tk.END)
        entry_nom.insert(0, values[0])
        entry_age.delete(0, tk.END)
        entry_age.insert(0, values[1])
        entry_ville.delete(0, tk.END)
        entry_ville.insert(0, values[2])

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("CRUD avec Treeview")
fenetre.geometry("600x400")

# Frame pour les champs de saisie
frame_form = tk.Frame(fenetre)
frame_form.pack(pady=10,fill="x")

# Champs de saisie
tk.Label(frame_form, text="Nom :").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nom = tk.Entry(frame_form)
entry_nom.grid(row=0, column=1, padx=5, pady=5,sticky="ew")

tk.Label(frame_form, text="Âge :").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_age = tk.Entry(frame_form)
entry_age.grid(row=1, column=1, padx=5, pady=5,sticky="ew")

tk.Label(frame_form, text="Ville :").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_ville = tk.Entry(frame_form)
entry_ville.grid(row=2, column=1, padx=5, pady=5,sticky="ew")

frame_form.grid_columnconfigure(0,weight=0)
frame_form.grid_columnconfigure(1,weight=1)

# Boutons CRUD
frame_buttons = tk.Frame(fenetre)
frame_buttons.pack(pady=10)

btn_ajouter = tk.Button(frame_buttons, text="Ajouter", command=ajouter, bg="lightgreen")
btn_ajouter.grid(row=0, column=0, padx=10)

btn_modifier = tk.Button(frame_buttons, text="Modifier", command=modifier, bg="lightblue")
btn_modifier.grid(row=0, column=1, padx=10)

btn_supprimer = tk.Button(frame_buttons, text="Supprimer", command=supprimer, bg="red", fg="white")
btn_supprimer.grid(row=0, column=2, padx=10)

# Treeview pour afficher les données
columns = ("Nom", "Âge", "Ville")
tree = ttk.Treeview(fenetre, columns=columns, show="headings")

# Configuration des colonnes
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

tree.pack(expand=True, fill="both", padx=10, pady=10)

# Remplir les champs lors de la sélection d'une ligne
tree.bind("<ButtonRelease-1>", remplir_champs)

# Lancement de la fenêtre
fenetre.mainloop()
