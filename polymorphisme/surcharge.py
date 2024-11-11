from math import pi
from multipledispatch import dispatch
class Surface:
    @dispatch(float)
    def surface(r:float):
        return pi*r**2
    @dispatch(float,float)
    def surface(lon:float,lar:float):
        return lon*lar
    @dispatch(float,float,float)
    def surface(lon,lar,hau):
        return 2*(lon*lar + lon*hau+ lar*hau)
    
s = Surface()
print(s.surface(6))