from ContactManager import ContactManager
from Contact import Contact
import os
class App:
    contactManger = ContactManager()

    def ajouter(self):
        nom = input("nom : ")
        tel = input("tel : ")
        contact = Contact(nom,tel)
        App.contactManger.add(contact)

    def afficher(self):
        print("***********************************")
        print("********Liste des contact *********")
        print("***********************************")
        App.contactManger.afficher()
        os.system("pause")

    def mainMenu(self):
        while True:
            os.system("cls")
            print("1. Ajouter")
            print("2. Afficher")
            print("3. Supprimer")
            print("4. rechercher par nom")
            print("5. rechercher par tel")
            print("6. Quiter")
            choix = int(input("Donner votre choix : "))
            match choix:
                case 1 : self.ajouter()
                case 2 : self.afficher()
                case 3 : pass
                case 4 : pass
                case 5 : pass
                case 6 : break


app =App()
app.mainMenu()
