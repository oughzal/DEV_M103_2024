from datetime import date
class Employe:

    def __init__(self,matricule,nom,prenom,dateNaissance):
        self.__matricule = matricule
        self.__nom = nom
        self.__prenom = prenom
        self.__dateNaissance = dateNaissance
    @property
    def matricule(self):
        return self.__matricule
    @matricule.setter
    def matricule(self,value):
        self.__matricule = value

    def getSalaire():
        pass

    def __str__(self): # toString()
        return f"matricule : {self.matricule}\n"

e1 = Employe(123,'nom',"prenom",date(2002,5,7))
print(e1)