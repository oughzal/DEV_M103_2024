class Animal:
    def __init__(self, nom):  self.nom = nom
    def se_deplacer(self):   pass
class Oiseau(Animal):
    def se_deplacer(self): print(f"{self.nom} vole.")
class Poisson(Animal):
    def se_deplacer(self): print(f"{self.nom} nage.")
class Tigre(Animal):
    def se_deplacer(self): print(f"{self.nom} court.")

from multipledispatch import dispatch
class Test:
    @dispatch(Tigre)
    def typeAnimal(a):
        return "Tigre"
    @dispatch(Poisson)
    def typeAnimal(a):
        return "Poisson"
    @dispatch(Oiseau)
    def typeAnimal(a):
        return "Oiseau"
    
a1 = Tigre("A")
a2 = Oiseau("B")
a3 = Poisson("C")

t = Test()
print(t.typeAnimal(a3))
    


