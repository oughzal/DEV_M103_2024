import Livre
from Utilisateur import Utilisateur

class Bibliotheque:

    def __init__(self):
        self.livres = {}
        self.utilisateurs = {}

    def ajouterLivre(self,livre:Livre):
        self.livres[livre.id] = livre
    
    def ajouterUtilisateur(self,utilisateur:Utilisateur):
        self.utilisateurs[utilisateur.id] = utilisateur

    def emprunterLivre(self,idLivre,idUtilisateur):
        if idUtilisateur in self.utilisateurs:
            if idLivre in self.livres:
                livre = self.livres[idLivre]
                self.utilisateurs[idUtilisateur].ajouterLivre(livre)
    
    def supprimerLivre(self,id):
        for user in self.utilisateurs:
            for l in user.livres:
                if l.id == id:
                    user.retirerLivre(l)
                    return
    
    def emprunter(self,idl, idu):
        if  idl not in self.livres or idu not in self.utilisateurs:
            return None
        self.utilisateurs[idu].ajouterLivre(self.livres[idl])

    def retournerLivre(self,idl,idu):
        if  idl not in self.livres or idu not in self.utilisateurs:
            return None
        #suit
        self.utilisateurs[idu].retirerLivre(self.livres[idl])

    def rechercherLivre(self,s):
        L =[]
        for livre in self.livres.values():
            if s in Livre.titre:
                L.append(livre)
        return L
    
    def afficherLives(self):
        for livre in self.livres.values():
            print(f"{livre.id} {livre.titre} - {livre.auteur}")
    

    


    