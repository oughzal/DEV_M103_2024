from ParcVehicles import parcVehicules
from Vehicule import Vihecule
class Application:
    parc = parcVehicules()

    def AjouterVehicule(self):
        marque = input("Donner la marque :")
        model = input("Donner le modèle : ")
        v = Vihecule(marque,model)
        Application.parc.ajouterVehicule(v)
    
    def afficherVehicules(self):
        Application.parc.afficherVehiculesDisponible()

    def mainMenu(self):
        while True:
            print("1. Ajouter une véhicule")
            print("2. Afficher les véhicules disponible")
            print("3. réserver un véhicule")
            print("4. retourner un véricule")
            print("5. Afficher toutes les réservation")
            print("6. Quit")
            choix = int(input("Entrer votre choix : "))

            match choix:
                case 1 :self.AjouterVehicule()
                case 2 :self.afficherVehicules()
                case 3 :pass
                case 4 :pass
                case 5 :pass
                case 6 : break
     

app = Application()
app.mainMenu()