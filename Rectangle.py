class Rectangle:

    #Constructeur
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur
    
    # Getter
    @property
    def longeur(self):
        return self.__longeur
    # Setter
    @longeur.setter
    def longeur(self,value):
        if value >= 0:
            self.longeur = value
    @property
    def largeur(self):
        return self.__largeur
    @ largeur.setter
    def largeur (self,value) :
        if value >= 0 :
            self.__largeur = value
    
    # TODO : périmètre 
    def peremetre(self):
        return 2* (self.__largeur+self.__longeur)
    # TODO : aire
    def aire(self):
        return self.__longeur * self.largeur
    
    @property
    def surface(self):
        return self.__largeur * self.__longeur
    # TODO : estCarre
    def estCarre(self):
        return self.__largeur == self.__longeur
    #TODO : AfficherRectangle
    def afficher(self):
        print(f"longeur :{self.__longeur}")
        print(f"largeur :{self.__largeur}")
        print(f"périmètre :{self.peremetre()}")
        print(f"aire :{self.aire()}")
        print(f"est carré :{self.estCarre()}")

R = Rectangle(10,20)
print(f"Longeur : {R.longeur}")
R.largeur = 300 # setter value = 300
print(f"surface : {R.aire()}")
print(f"surface : {R.surface}")
R.afficher()