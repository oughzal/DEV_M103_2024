from Employe import Employe
class Patron(Employe):
    chiffreAffaire = 100,000,000

    def __init__(self, matricule, nom, prenom, dateNaissance,pourcentage):
        super().__init__(matricule, nom, prenom, dateNaissance)
        self.__pourcentage = pourcentage
    
    def getSalaire(self):
        return Patron.chiffreAffaire * (self.__pourcentage/100)
