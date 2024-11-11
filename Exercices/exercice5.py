class Stagiaire:
    nbObject = 0
    def __init__(self,matricule,nom,filiere):
            self.__matricule = matricule
            self.__nom = nom
            self.__filiere = filiere
            self.__notes = []
            Stagiaire.nbObject += 1
    
    @property
    def matricule(self):
          return self.__matricule
    
    @matricule.setter
    def matricule(self,value):
          self.__matricule = value

    @classmethod
    def RAZ(cls):
          cls.nbObject = 0

    def __eq__(self, other):
          return self.matricule == other.matricule
    
    def add(self,note):
          if 0<= note <= 20:
            self.__notes.append(note)
    def moyenne(self):
          if len(self.__notes)==0 :
                return 0
          return sum(self.__notes) / len(self.__notes)

s1 = Stagiaire(123,"nom","DEV")
s2 = Stagiaire(123,"nom","DEV")
print(s1==s2)