from math import pi,sqrt
class Cercle:

    def __init__(self,x,y,r):
        self.__x = x
        self.__y = y
        self.__r = r
    @property
    def x(self):
        return self.__x
    def permitre(self):
        return 2*pi*self.__r
    def surface(self):
        return pi*self.__r**2
    def appartient(self,x,y):
        d = sqrt((self.__x -x)**2 + (self.__y -y)**2)
        return self.__r == d