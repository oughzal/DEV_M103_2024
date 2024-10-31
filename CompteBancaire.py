class CompteBancaire :
    # Constructeur ; initialiser les attributs
    def __init__(self,nom,num,solde):
        self.nom=nom
        self.num=num
        self.solde=solde
    #  destructeur : appelé avant la supression de l'objet
    def __del__(self):
        print("objet supprimé")
    # méthode l'instance
    def consulter(self):
        return f"votre solde est : {self.solde} dh"
    
    def depot(self,montant):
        if montant > 0:
            self.solde += montant
        else:
            print("erreur : montant négatif")
    
    def retrait(self,montant):
        if montant <= self.solde :
            self.solde -= montant 
        else :
           print("erreur : solde insuffisant") 
    def afficher(self):
        print(f"num:{self.num}\nnom:{self.nom}\nsolde:{self.solde}")
    
    def __str2__(self): # toString()
        return f"num:{self.num}\nnom:{self.nom}\nsolde:{self.solde}"

c1 = CompteBancaire("nom",1,10000)
print(c1.consulter())
c1.depot(1000)
print(c1.consulter())
c1.depot(-1000)
print(c1.consulter())
c1.afficher()
print(c1)

