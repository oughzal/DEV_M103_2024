from showMenu import showMenu
from Magasin import Magasin
from Produit import Produit
from MouvementStock import MouvementStock
from os import system
class App:
    def __init__(self):
        self.magasin = Magasin()

    def mainMenu(self):
        menu = [
            "Afficher Produits",
            "Ajouter Produit",
            "Enregistrer Entrée",
            "Enregistrer Sortie",
            "Afficher Mouvements",
            "Quiter"
        ]
        while True:
            index = showMenu(menu)
            system("cls")
            match index:
                case 0 : 
                    self.afficherProduits()
                    system("pause")
                case 1 : self.ajouterProduit()
                case 2 : pass
                case 3 : pass
                case 4 : self.magasin.afficherMouvements()
                case 5 : break

    def ajouterProduit(self):
        system("cls")
        nom = input("nom du produit : ")
        qt = int(input("Quatité du produit : "))
        prix = float(input("prix du produit : "))
        p = Produit(nom,qt,prix)
        self.magasin.ajouterProduit(p)

    def afficherProduits(self):
        menu = list(self.magasin.produits.values()) + ["retour"]
        l = len(menu)
        while True:
            index = showMenu(menu)
            if index-1 == l : index = -1
            print(index)
            match index:
                case -1 : return

app = App()
app.mainMenu()