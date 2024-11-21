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
            system("cls")
            index = showMenu(menu)
            match index:
                case 0 : 
                    self.magasin.afficherProduits()
                    system("pause")
                case 1 : self.ajouterProduit()
                case 2 : pass
                case 3 : pass
                case 4 : self.magasin.afficherMouvements()
                case 5 : break

    def ajouterProduit(self):
        nom = input("nom du produit : ")
        qt = int(input("Quatité du produit : "))
        prix = float(input("prix du produit : "))
        p = Produit(nom,qt,prix)
        self.magasin.ajouterProduit(p)

app = App()
app.mainMenu()