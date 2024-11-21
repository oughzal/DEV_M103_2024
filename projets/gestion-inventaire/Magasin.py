from Produit import Produit
from MouvementStock import MouvementStock
class Magasin:

    def __init__(m):
        m.produits = {}
        m.mouvements = {}

    def ajouterProduit(m,produit):
        m.produits[produit.id] = produit
    
    def afficherProduits(m):
        print("*******************************")
        print("*****    List Produit   *******")
        print("*******************************")
        for p in m.produits.values():
            print(p)

    def enregisterEntree(m,id,Qt):
        if  Qt < 0 : return
        if id in m.produits:
            p = m.produits[id]
            p.ajouterQuantite(Qt)
            m = MouvementStock(p,"Entee",Qt)
            m.mouvements[m.id] = m
    def enregisterSortie(m,id,Qt):
        if id in m.produits:
            p = m.produits[id]
            if p.quatity < Qt : return
            p.ajouterQuantite(Qt)
            m = MouvementStock(p,"Sortie",Qt)
            m.mouvements[m.id] = m
    def afficherMouvements(m):
        for m in m.mouvements:
            print(m)
            print(f"{m.produit}\t{m.type}\t{m.Qt}\t{m.date}")