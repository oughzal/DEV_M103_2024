class Vihecule:
    cmp = 0 # Attribut de class (partagé)
    def __init__(self,marque,model):
        Vihecule.cmp += 1
        self.id = Vihecule.cmp # id automatque
        self.marque = marque
        self.model = model
        self.disponible = True

    def marquerIndisponible(self):
        self.disponible = False

    def marquerDisponible(self):
        self.disponible = True
    
    def __str__(self):
        return f"id:{self.id} ; marque : {self.marque}"
    
    def afficherInfo(self):
        print(f"id : {self.id}")
        print(f"marque : {self.marque}")
        print(f"modèle : {self.model}")
        print(f"disponible : {self.disponible}")



