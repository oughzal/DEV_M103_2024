import keyboard
import sys
import time
from colorama import Fore, Style, init

# Codes de scan pour les touches fléchées sous Windows
SCAN_CODE_UP = 72    # Flèche Haut
SCAN_CODE_DOWN = 80  # Flèche Bas
SCAN_CODE_ENTER = 28 # Touche Entrée

def showMenu(options):
    # Initialisation de colorama pour une coloration automatique
    init(autoreset=True)
    option_actuelle = 0

    def afficher_menu(options, option_actuelle):
        # Effacer le contenu précédent
        sys.stdout.write("\033[F" * len(options))  # Remonte à la première ligne du menu
        sys.stdout.write("\033[J")  # Efface toutes les lignes en dessous
        # Affiche le menu mis à jour
        for i, option in enumerate(options):
            if i == option_actuelle:
                # Surligner l'option actuelle
                sys.stdout.write(f"{Fore.GREEN}> {i + 1} : {option}{Style.RESET_ALL}\n")
            else:
                sys.stdout.write(f"  {i + 1} : {option}\n")

    # Afficher le menu initial
    afficher_menu(options, option_actuelle)
    time.sleep(0.2)  # Délai initial pour que le menu soit bien visible

    while True:
        # Capturer les événements de touches
        event = keyboard.read_event(suppress=True)  # Supprime l'effet normal des touches
        if event.event_type == "down":  # Seuls les événements "key down" sont pris en compte
            if event.scan_code == SCAN_CODE_UP:  # Flèche Haut
                option_actuelle = (option_actuelle - 1) % len(options)
                afficher_menu(options, option_actuelle)
                time.sleep(0.15)  # Petit délai pour éviter une détection trop rapide
            elif event.scan_code == SCAN_CODE_DOWN:  # Flèche Bas
                option_actuelle = (option_actuelle + 1) % len(options)
                afficher_menu(options, option_actuelle)
                time.sleep(0.15)  # Petit délai pour éviter une détection trop rapide
            elif event.scan_code == SCAN_CODE_ENTER:  # Entrée
                # Efface les lignes du menu et retourne l'option sélectionnée
                sys.stdout.write("\033[J")
                return option_actuelle

if __name__ == "__main__":
    # Exemple d'utilisation
    options = ["Option 1", "Option 2", "Option 3", "Quitter"]

    while True:
        index_choisi = showMenu(options)
        sys.stdout.write("\033[J")  # Nettoyer après affichage
        if options[index_choisi] == "Quitter":
            print("Au revoir !")
            break
        else:
            print(f"Vous avez choisi : {options[index_choisi]}")
            time.sleep(0.5)  # Délai pour bien voir la sélection avant de revenir au menu
