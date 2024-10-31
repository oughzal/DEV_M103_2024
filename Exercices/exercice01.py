class Rectangle:
    pass

class Parallelepipede:
    # constructeur
    def __init__(self,larg,long, haut):
        self.__longueur = long
        self.__largeur = larg
        self.__hauteur = haut
    @property
    def longueur(self):
        return self.__longueur
    @longueur.setter
    def longueur(self,value):
        self.__longueur = value
    
    def perimetre(self):
        return 4*(self.__longueur+self.__largeur+self.__hauteur)
    def surface(self):
        2*(self.__largeur*self.__largeur + self.__largeur*self.__hauteur + self.__longueur*self.__hauteur)
    def volume(self):
        return self.__hauteur*self.__largeur*self.__longueur