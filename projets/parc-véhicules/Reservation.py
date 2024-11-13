from Vehicule import Vihecule

class Reservation:
    cmp = 0

    def __init__(self,v,client,dateDebut,dateFin):
        Reservation.cmp += 1
        self.id = Reservation.cmp
        self.vehicule = v
        self.dateDebut = dateDebut
        self.dateFin = dateFin
    
    def afficherDetails(self):
        print(f"id : {self.id}")
        print(f"vehicule : {self.vehicule}")
        print(f"date Debut : {self.dateDebut}")
        print(f"date Fin : {self.dateFin}")