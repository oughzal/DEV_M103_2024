class Etudiant :
    cmp = 0
    def __init__(self,nom) :
        Etudiant.cmp += 1
        self.id = Etudiant.cmp 
        self.nom = nom
        self.coursInscrits = []
    def inscrireCours(self,cours):
        self.coursInscrits.append(cours)
    def afficherCours(self):
        print(f"id : {self.id} ; nom : {self.nom} ")
        for cours in self.coursInscrits :
            print(cours)
        map(lambda cours : print(cours),self.coursInscrits)
