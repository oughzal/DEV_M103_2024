class Stagiaire:
    __groupe = "DEV101"
    def __init__(self):
        self.__nom = "nom"
        self.prenom = "prenom"
        self.__note = 20
 
    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self,value):
        if 0<=value<=20:
            self.__note = value
        else:
            raise Exception("note invalide")
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,value):
        self.__nom = value

    def afficher(self):
        self.__calculerNote()

    @classmethod
    def methodeClasse(cls):
        print("méthode de classe")
        cls.__groupe ="DEVOAM201"

    @staticmethod
    def static():
        pass

    def __calculerNote(self):
        print("20/20")

    def __del__(self):
        print("objet détruit")



# instanciation
s1 = Stagiaire()
s1.afficher()
s1.methodeClasse()
Stagiaire.methodeClasse()
try:
    s1.note = 99 # setter -> value = 99
except:
    print("note non valide")
print(s1.note) # getter 
