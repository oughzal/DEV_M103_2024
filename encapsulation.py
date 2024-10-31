class Compte:
    def __init__(self,solde):
        self.__solde = solde
    
    @property # getter
    def solde(self):
        return self.__solde
    @solde.setter
    def solde(self,value):
        if value > 0:
            self.__solde = value

    def getSolde(self):
        return self.__solde
    
    def setSolde(self,value):
        if value > 0:
            self.__solde = value


c1 = Compte(10000)
print(c1.getSolde())
c1.setSolde(15000)
print(c1.getSolde())
print(c1.solde) # c1.solde()
c1.solde = 2000 # c1.solde(20000)
