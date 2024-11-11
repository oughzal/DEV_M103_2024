# pip install multipledispatch
from multipledispatch import dispatch
import math
# Calcul de l'aire d'un cercle
@dispatch(float)
def surface(rayon): return math.pi * rayon * rayon
# Calcul de l'aire d'un rectangle
@dispatch(float, float)
def surface(longueur, largeur): return longueur * largeur
# Calcul de l'aire d'un triangle
@dispatch(float, float)
def surface(base, hauteur): return 0.5 * base * hauteur
# Utilisation
print("Aire du cercle (rayon=5) :", surface(5.0))                 # Cercle
print("Aire du rectangle (longueur=4, largeur=6) :", surface(4.0, 6.0))  # Rectangle
print("Aire du triangle (base=3, hauteur=8) :", surface(3.0, 8.0))   # Triangle
