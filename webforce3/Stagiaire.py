class Stagiaire:
    def __init__(self,nom,prenom): # constructeur paramétré 
          self.nom = nom
          self.prenom = prenom

    def __del__(self):
         print("objet supprimé")

    def copy(self):
        return Stagiaire(self.nom,self.prenom)


s1 = Stagiaire("nom1","prenom1")
s2 = s1.copy() # affectation
s3 = s1
s1.nom ="DEV"
s1 = Stagiaire("nom2","prenom2")
print(s2.nom)

