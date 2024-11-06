from Employe import Employe

class Cadre(Employe):

    def __init__(self, matricule, nom, prenom, dateNaissance,indice):
        super().__init__(matricule, nom, prenom, dateNaissance)
        self.__indice = indice

    @property
    def indice(self):
        return self.__indice
    @indice.setter
    def indice(self,value):
        self.__indice = value

    def __str__(self):
        return super().__str__() + f"\nindice : {self.__indice}"
    
    def getSalaire(self):
        match self.__indice :
            case 1 : return 13000
            case 2 : return 15000
            case 3 : return 17000
            case 4 : return 20000
            case _ : return 0