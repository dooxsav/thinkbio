# Controller/Geogaphy.py
import os 
from datetime import datetime
from app.services import lire_ercrire_mettre_a_jour_table_geography, lire_donnees_BD_geography

def HelloGeography():
    return "Geography WORK !"

def PopulateDB_geography(file):

    # Gestion des chemins des fichiers :
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Récupérer le répertoire du fichier actuel (geography_controller.py)
    path_to_input = os.path.join(current_directory, '..', '..', 'ressources', 'input', 'Geography')  # Chemin vers le répertoire "ressources/input"
    
    # Gestion du nommage : 
    datefichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Formater la date
    nom_fichier = f"geography_{datefichier}.xlsx"  # Créer un nom de fichier pour sauvegarder le fichier PDF
    file_path = os.path.join(path_to_input, nom_fichier)  # Chemin complet du fichier à enregistrer
    
    # Sauvegarder le fichier avec un nom spécifique dans le dossier spécifié
    file.save(file_path)
    
    result = lire_ercrire_mettre_a_jour_table_geography(file_path)
    
    return result

def lireDB_geography():
    # Lire la base de données géographique
    result = lire_donnees_BD_geography()
    return result