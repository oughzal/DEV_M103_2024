from Point import Point
class TroisPoint:

    def __init__(self, p1:Point, p2:Point,p3:Point):
        self.__point1 = p1
        self.__point2 = p2
        self.__point3 = p3
    
    @property
    def point1(self):
        return self.__point1
    @point1.setter
    def point1(self,value):
        self.__point1 = value

    @property
    def point2(self):
        return self.__point2
    @point2.setter
    def point2(self,value):
        self.__point2 = value
    @property
    def point3(self):
        return self.__point3
    @point3.setter
    def point3(self,value):
        self.__point3 = value
    
    def sonAlignees(self):
        AB = self.point1.distance(self.point2)
        AC = self.point1.distance(self.point3)
        BC = self.point2.distance(self.point3)
        return AC==AB+BC or AB==BC+AC or BC==AB+AC
    def estIsosel(self):
        AB = self.point1.distance(self.point2)
        AC = self.point1.distance(self.point3)
        BC = self.point2.distance(self.point3)
        return AB==AC or AB==BC or BC==AC
    
    @staticmethod
    def distance(p1:Point,p2:Point):
        if isinstance(p1,Point) and isinstance(p2,Point):
            return p1.distance(p2) 
        
    @staticmethod
    def milieu(p1:Point,p2:Point):
        if isinstance(p1,Point) and isinstance(p2,Point):
            return p1.milieu(p2) 

    

p1 = Point(1,1)
p2 = Point(2,20)
p3 = Point(0,3)
tp = TroisPoint(p1,p2,p3)
print(tp.sonAlignees())
print(tp.estIsosel())