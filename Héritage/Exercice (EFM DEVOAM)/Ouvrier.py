from datetime import date
from Employe import Employe
class Ouvrier(Employe):
    SMIG = 2500

    def __init__(self, matricule, nom, prenom, dateNaissance,dateEmbouche):
        super().__init__(matricule, nom, prenom, dateNaissance)
        self.__dateEmbouche = dateEmbouche
    
    @property
    def dateEmbouche(self):
        return self.__dateEmbouche
    @dateEmbouche.setter
    def dateEmbouche(self,value):
        self.__dateEmbouche = value

    def __str__(self):
        return f"{super().__str__()}\ndate Embouche : {self.__dateEmbouche}"
    
    def getSalaire(self):
        encienite = date().year - self.__dateEmbouche.year
        salaire = Ouvrier.SMIG + encienite*100
        if salaire >= 2*Ouvrier.SMIG:
            return 2*Ouvrier.SMIG
        else:
            return salaire
