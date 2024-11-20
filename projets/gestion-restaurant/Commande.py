from Article import Article
class Commande:
    cmp = 0
    def __init__(self,client):
        Commande.cmp += 1
        self.id = Commande.cmp
        self.client = client
        self.status = "en préparation"
        self.articles = []
    
    @property
    def total(self):
        t = 0 
        for a in self.articles:
            t += a.prix
        return t

    def ajouterArticle(self,article:Article):
        if isinstance(article,Article):
            self.articles.append(article)
        
    
    def changerStatus(self,status):
        self.status = status

    def afficherCommande(self):
        print(f"id : {self.id}")
        print(f"Client : {self.client}")
        print(f"id\tArticle\t\tprix")
        total = 0
        for a in self.articles:
            print(a)
            total += a.prix
        print(f"\t\ttatal  : {total}")

if __name__ == "__main__":
    c = Commande("Nom Prénom")
    c.ajouterArticle(Article("Article1",20))
    c.ajouterArticle(Article("Article2",30))
    c.ajouterArticle(Article("Article3",15))
    c.ajouterArticle(Article("Article4",40))
    c.afficherCommande()

