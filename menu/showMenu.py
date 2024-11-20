import keyboard,sys,time
from colorama import Fore, Back, Style, init


def showMenu(options):
    # Initialisation de colorama
    init(autoreset=True)
    option_actuelle = 0
    def afficher_menu(options, option_actuelle):
        for i, option in enumerate(options):
            # Surligner l'option actuelle en blanc avec arrière-plan noir
            if i == option_actuelle:
                sys.stdout.write(f"\r{Fore.GREEN}> {i+1} : {option}{Style.RESET_ALL}\n")
            else:
                sys.stdout.write(f"\r  {i+1} : {option}\n")
        # Remettre le curseur en haut du menu pour le prochain rafraîchissement
        sys.stdout.write(f"\033[{len(options)}A")


    # Afficher le menu initial
    afficher_menu(options, option_actuelle)

    while True:
        # Vérifie les pressions de touches
        if keyboard.is_pressed('up'):
            option_actuelle = (option_actuelle - 1) % len(options)
            afficher_menu(options, option_actuelle)
            time.sleep(0.15)  # Petit délai pour éviter une détection trop rapide de la touche

        elif keyboard.is_pressed('down'):
            option_actuelle = (option_actuelle + 1) % len(options)
            afficher_menu(options, option_actuelle)
            time.sleep(0.15)  # Petit délai pour éviter une détection trop rapide de la touche

        elif keyboard.is_pressed('enter'):
            # Efface les lignes du menu et retourne l'option sélectionnée
            sys.stdout.write("\033[J")
            return option_actuelle
if __name__ == "__main__":
    # Exemple d'utilisation
    options = ["Option 1", "Option 2", "Option 3", "Quitter"]
    index_choisi = showMenu(options)
    print(f"\nVous avez choisi l'option : {options[index_choisi]} (Index : {index_choisi})")
