import Livre


class Utilisateur:
    cmp = 0
    def __init__(self,nom):
        Utilisateur.cmp += 1
        self.id = Utilisateur.cmp
        self.nom = nom
        self.livres = []
    
    def ajouterLivre(self,livre:Livre):
        if livre.disponible :
            self.livres.append(livre)
            livre.empunter()
    
    def retirerLivre(self,livre:Livre):
        if livre in self.livres:
            livre.retourner()
            self.livres.remove(livre)

    def afficherEmrunts(self):
        for i,l in enumerate(self.livres):
            print(f"{i+ 1}. titre : {l.titre} - auteur : {l.auteur}")