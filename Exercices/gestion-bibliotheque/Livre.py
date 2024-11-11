class Livre:
    def __init__(self,ISBN, titre, auteur, annee):
        self.ISBN= ISBN
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
    def afficherdetails(self):
        print(f"ISBN : {self.ISBN}")
        print(f"titre is : {self.titre}")
        print(f"auteur is : {self.auteur}")
        print(f"annee is : {self.annee}")


livre = Livre(123,"Titre","auteur",2024)
print(livre.ISBN)
livre.afficherdetails()


