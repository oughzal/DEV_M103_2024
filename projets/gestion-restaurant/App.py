from Article import Article
from Commande import Commande
from Restaurant import Restaurant

class App:

    def __init__(self):
        self.restaurant = Restaurant()

    def mainMenu(self):
        while True:
            print("1. Afficher menu")
            print("2. Ajouter Article")
            print("1. prendre Commande")
            print("5. Quiter")
            choix = int(input("choisir une option : "))
            match choix:
                case 1 : pass
                case 2 : pass
                case 3 : pass
                case 4 : pass
                case 5 : break