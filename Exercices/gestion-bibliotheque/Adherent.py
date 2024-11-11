from Emprunt import Emprunte
from Livre import Livre
from datetime import date
class Adherent:
    def __init__(self,num,nom,adresse):
        self.num = num
        self.nom = nom
        self.adresse = adresse
        self.empruntes = []
    def emprunter (self,livre:Livre):
        e = Emprunte(self,livre)
        livre.disponible = False
        self.empruntes.append(e)
    def retourner(self,livre):
        for e in self.empruntes:
            if e.livre == livre :
                e.livre.disponible = True
                e.date_retoure = date.today()
                break
    def afficher (self):
        for e in self.empruntes :
            print (f"livre : {e.livre}  date emprunt : {e.date_emprunt }   date retour : {e.date_retour }")


