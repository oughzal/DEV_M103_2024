from Vehicule import Vihecule
from Reservation import Reservation
import os
import json
class parcVehicules:

    def __init__(self):
        self.vehicules = []
        self.reservations = []
        self.load()
    
    def ajouterVehicule(self, vehicule):
        self.vehicules.append(vehicule)
        self.save()
    
    def afficherVehiculesDisponible(self):
        for v in self.vehicules:
            if v.disponible == True :
                print(v)

    def reserver(self,id,client,dateDebut,dateFin):
        vihecule = None
        for v in self.vehicules:
            if v.id == id:
                vihecule = v
                break
        if vihecule != None and vihecule.disponible:
            res = Reservation(vihecule,client,dateDebut,dateFin)
            self.reservations.append(res)
            self.save()
        else :
            print("resevation non effectué")

    def retourner(self,id):
        res = None 
        for r in self.reservations:
            if r.vehicule.id == id:
                res = r
                break
        if res:
            res.vehicule.marquerDisponible()
            self.save()
    
    def afficherReservations(self):
        for r in self.reservations:
            print(f"id:{r.id}; véhicule:{r.vehicule} date début : {r.dateDebut} dateFin : {r.dateFin}")

    def save(self):
        vs = []
        for v in self.vehicules:
            vs.append({
                "id" : v.id,
                "marque" : v.marque,
                "modèle" : v.model,
                "disponible" : v.disponible,
            })
        data = {"v" : vs, "r": self.reservations}
        with open("data.json","w") as file:
            json.dump(data,file)

    def load(self):
        if os.path.exists("data.json") == False : return
        with open("data.json","r") as file:
            data = json.loads(file) 
            self.vehicules = data["v"]
            self.reservations = data["r"]



