class Animal:
    def __init__(self,name):
        self.name = name
    def seDeplacer(self): pass

class Oiseau(Animal):
    def seDeplacer(self): return f"l'oiseau vole"

class Poisson(Animal):
    def seDeplacer(self): return f"l'oiseau nage"
class Tigre(Animal):
    def seDeplacer(self): return f"l'oiseau coure"

animaux = [Oiseau("A"),Poisson("B"),Tigre("C")]
for a in animaux:
    print(a.seDeplacer())

a : Animal = Oiseau("D")