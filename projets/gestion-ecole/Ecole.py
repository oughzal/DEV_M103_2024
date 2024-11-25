from Etudiant import Etudiant
from Cours import Cours
class Ecole:
    def __init__(self):
        self.etudiants=[]
        self.cours=[]
    def ajouterEtudiant(self,etudiant):
        self.etudiants.append(etudiant)
    def ajouterCours(self,cour):
        self.cours.append(cour)
    def inscrireEtudiantCour(self,idetudiant,idcour):
        etudiant = list(filter(lambda e : e.id==idetudiant,self.etudiants))[0]
        cours = list(filter(lambda e : e.id==idcour,self.cours))[0]
        cours.ajouterEtudiant(etudiant)
        etudiant.inscrireCours(cours)
    def afficherEtudiants(self):
        for e in self.etudiants:
            print(e)
    def afficherCours(self):
        for c in self.cours:
            print(c)
