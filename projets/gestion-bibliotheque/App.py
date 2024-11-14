from Bibliotheque import Bibliotheque
from Livre import Livre
from os import system
class App:

    def __init__(self):
        self.biblio = Bibliotheque()


    def supprimerLivre(self):
        self.biblio.afficherLives()
        id = int(input("donner l'id du livre : "))
        if id in self.biblio.livres:
            del self.biblio.livres[id]

    def ajouterLivre(self):
        titre = input("titre : ")
        auteur = input("auteur : ")
        livre = Livre(titre,auteur)
        self.biblio.ajouterLivre(livre)
   
    def menu(self):
        while True:
            system("cls")
            print("1. Afficher tous les livres ")
            print("2. Ajouter un livre ")
            print("3. supprimer un livre ")
            print("4. rechercher un livre ")
            print("5. emprunter un livre ")
            print("6. retourner un livre ")
            print("7. afficher  emprunts d'un utilisateur ")
            print("8. Quiter")
            choix = int(input("Enter le numéro de votre choix :"))

            match choix:
                case 1 : 
                    self.biblio.afficherLives()
                    system("pause")
                case 2 : self.ajouterLivre()
                case 3 : self.supprimerLivre()
                case 4 : pass
                case 5 : pass
                case 6 : pass
                case 7 : pass
                case 8 : break


app = App()
app.menu()