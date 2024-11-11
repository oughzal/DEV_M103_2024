from math import gcd
class Fraction:

    def __init__(self,a,b):
        if b == 0 :
            raise Exception("B = 0")
        d = gcd(a,b)
        self.a = a//d
        self.b = b//d
        
    
    def __str__(self):
        return f"{self.a}/{self.b}"

    
    #  +
    def __add__(self,other):
        return Fraction(self.a*other.b + self.b*other.a,self.b*other.b)
    # -
    def __sub__(self,other):
        return Fraction(self.a*other.b - self.b*other.a,self.b*other.b)
    # *
    def __mul__(self,other):
        return Fraction(self.a*other.a, self.b*other.b)
    # /
    def __truediv__(self,other):
        return Fraction(self.a*other.b, self.b*other.a)
    # > : greater than gt
    def __gt__(self,other):
        return self.a*other.b > self.b*other.a
    # >= : ge
    def __ge__(self,other):
        return self.a*other.b >= self.b*other.a
    # < : lt ; <= le
    def __lt__(self,other):
        return self.a*other.b < self.b*other.a
    
    def __le__(self,other):
        return self.a*other.b < self.b*other.a
    
    # ==
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    # !=
    def __ne__(self, other):
        return self.a != other.a or self.b != other.b

f1 = Fraction(6,8)
print(f1)
