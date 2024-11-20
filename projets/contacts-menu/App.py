from showMenu import showMenu
from ContactManager import ContactManager
from Contact import Contact
from os import system
class App:

    def __init__(self):
        self.contactManager = ContactManager()

    def mainMenu(self):
        options = [f"{contact.name} ({contact.tel})" for contact in self.contactManager.contacts.values()]
        options.append("Nouvelle entrée")
        options.append("Quitter")
        while True:
            system("cls")
            choix = showMenu(options)
            if choix == len(options) - 1:
                return False
            if choix == len(options) - 2:
                self.ajouterContact()
            else:
                contact = list(self.contactManager.contacts.values())[choix]
                self.menuContact(contact)
            return True
    
    def menuContact(self, contact):
        options = ["Modifier", "Supprimer", "Retour"]
        choix = showMenu(options)
        if choix == 0:
            self.modifierContact(contact)
        elif choix == 1:
            self.supprimerContact(contact)
        else:
            return


    def ajouterContact(self):
        nom = input("Nom : ")
        tel = input("Téléphone : ")
        Contact(nom,tel)
        system("pause")

    def modifierContact(self, contact):
        nom = input(f"Nom ({contact.name}) : ")
        tel = input(f"Téléphone ({contact.tel}) : ")
        contact.name = nom if nom else contact.name
        contact.tel = tel if tel else contact.tel
        system("pause")

    def supprimerContact(self, contact):
        self.contactManager.delContact(contact)
        system("pause")

    def run(self):
        while self.mainMenu():
            pass
if __name__ == "__main__":
    App().run()
