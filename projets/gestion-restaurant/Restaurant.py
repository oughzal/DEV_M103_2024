from Article import Article
from Commande import Commande
class Restaurant:

    def __init__(self):
        self.menu = {}
        self.commandes = {}

    def ajouterArticle(self,article):
        if isinstance(article,Article):
            self.menu[article.id] = article
    
    def afficherMenu(self):
        print(f"id\tArticle\t\tprix")
        for a in self.menu:
            print(a)
    
    def prendreCommande(self,client,idsArticles):
        c = Commande(client)
        for id in idsArticles:
            if id in self.menu: #{1:1,2:2,3:4}
                c.ajouterArticle(self.menu[id])
        self.commandes[c.id] = c
    def afficherCommandes(self):
        print("id\tclient\tstatus\ttotal")
        for c in self.commandes:
            print(f"{c.id}\t{c.client}\t{c.status}\t{c.total}")
    
    def afficherCommande(self,id):
        c = self.commandes[id]
        c.afficherCommande()
    
    def changerStatus(self,id,status):
        self.commandes[id].changerStatus(status)

