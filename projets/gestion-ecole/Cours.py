class Cours:
    cmp = 0
    def __init__(self,titre,enseignant):
        Cours.cmp += 1
        self.id = Cours.cmp
        self.titre = titre
        self.etudiants =[]
        self.enseignant = enseignant
    def ajouterEtudiant(self,etudiant):
        self.etudiants.append(etudiant)
    
    def afficherEtudiants (self):
        print(f"id : {self.id} \n Titre : {self.titre} \n Enseignant : {self.enseignant} \n Etudiants : ")
        map(lambda e : print(e), self.etudiants)

        
        