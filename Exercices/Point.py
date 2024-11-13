from math import sqrt
class Point:
    nb = 0 # nombre d'instances

    def __init__(self,abs,ord):
        self.__abs = abs
        self.__ord = ord
        Point.nb += 1
    
    @property # getter
    def abs(self):
        return self.__abs
    @abs.setter  # setter
    def abs(self,value):
        self.__abs = value
    
    @property
    def ord(self):
        return self.__ord
    
    @ord.setter
    def ord(self,value):
        self.__ord =value

    # toString
    def __str__(self):
        return f"({self.__abs},{self.__ord})"
    
    def __eq__(self,other):
        if isinstance(other,Point):
            return self.abs == other.abs and self.__ord == other.__ord
        return False
    def distance(self,other):
        #if isinstance(other,Point):
        return sqrt((self.abs - other.abs)**2 + (self.ord - other.ord)**2)
        # return 0
    def milieu(self,other):
        if isinstance(other,Point):
            x = (self.abs + other.abs)/2
            y = (self.ord + other.ord)/2
            return Point(x,y)

p1 = Point(1,1)
p2 = Point(3,3)
print(p1)
print(p1!=p2)
print(p1.distance(p2))
print(p1.milieu(p2))