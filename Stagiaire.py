class Stagiaire:
    groupe = "DEV101" # attribut de class

    def __init__(self,nom,prenom): # constructeur
        self.nom = nom # Attribut d'instance
        self.prenom = prenom

    def __del__(self): 
        print("objet détruit")
    
    def afficher(self):
        print(f"{self.nom} {self.prenom}")
    
    @classmethod
    def modifierGroupe(cls,nomGroupe):
        cls.groupe = nomGroupe


s1 = Stagiaire("nom1","prénom1") # créer une instance + référence
s2 = Stagiaire("nom2","prénom2")
s3 = s1 # créer un référence
