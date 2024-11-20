class Article:
    cmp = 0
    def __init__(self,nom,prix):
        Article.cmp += 1
        self.id = Article.cmp
        self.nom = nom
        self.prix = prix
    
    def afficherInfo(self):
        print(f"{self.id}. {self.nom}\t {self.prix}")

    def __str__(self):
        return f"{self.id}\t{self.nom}\t{self.prix}"
    