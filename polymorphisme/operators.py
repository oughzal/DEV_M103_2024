class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, autre): return Vecteur(self.x + autre.x, self.y + autre.y)
v1 = Vecteur(3, 5)
v2 = Vecteur(2, 7)
v3 = v1 + v2 
print(v3.x, v3.y)  # Affiche : 5, 12