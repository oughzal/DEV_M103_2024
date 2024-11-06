class Person:
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        
    def afficher(self):
        print(f"{self.nom} {self.prenom} {self.age}")

class Stagiaire(Person):
    def __init__(self,nom,prenom,age,formation):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        super().__init__(nom,prenom,age)
        self.formation = formation

s1 = Stagiaire("Doe","John",25,"Python")
print(isinstance(s1,Stagiaire))
print(isinstance(s1,Person))
print(isinstance(s1,object))
print(issubclass(Stagiaire,Person))
print(issubclass(Stagiaire,object))
print(issubclass(Person,Stagiaire))

s1 = Stagiaire("Doe","John",25,"Python")
s2 = Stagiaire("Doe","John",25,"Python")
s3 = s1
print(s1 == s2)
print(s1 == s3)
print(s1 is s2) # === (identité)

L1 = [1,2,3]
L2 = [1,2,3]
L3 = L1
print(L1 == L2)
print(L1 is L2)
print(L1 == L3)
print(L1 is L3)


