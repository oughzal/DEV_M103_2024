class Livre:
    cmpt = 0
    def __init__(self,titre,auteur,anneePub):
        Livre.cmpt +=1
        self.id = Livre.cmpt
        self.titre = titre
        self.auteur = auteur
        self.anneePub = anneePub

l1 = Livre("tire 1","auteur1",2024)
l2 = Livre("tire 1","auteur1",2024)
l3 = Livre("tire 1","auteur1",2024)
print(l3.id)