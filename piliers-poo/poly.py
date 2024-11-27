# pip install multipledispach
from multipledispatch import dispatch

class Stagiaire:

    @dispatch(str,str)
    def __init__(self,nom,prenom):
        self.prenom = prenom
        self.nom = nom
    # @dispatch(str)
    # def __init__(self,nom):
    #     self.nom = nom
    #     self.prenom ="DEV"

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
    def claculer(self):
        return 10

class Developpeur(Stagiaire):

    def __init__(self, nom,prenom):
        super().__init__(nom,prenom) # chaînage

    def __str__(self):
        return f"le développeur {super().__str__()}"
    
    # override
    def claculer(self):
        return 20

    
# ob1 = Stagiaire("nom1")
ob2 = Stagiaire("nom2","prenom")
print(ob2)
ob3 = Developpeur("nom3","prenom3")
print(ob3)
