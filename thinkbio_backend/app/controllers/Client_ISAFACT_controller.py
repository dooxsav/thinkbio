# controller/Client_ISAFACT_controller.py
import os
from datetime import datetime

def importISAFACTDataFromExcel(file):
    # Enregistrer le fichier source
    # Gestion des chemins des fichiers :
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Récupérer le répertoire du fichier actuel (GRC_controller.py)
    path_to_input = os.path.join(current_directory, '..', '..', 'ressources', 'input', 'ISFACT')  # Chemin vers le répertoire "ressources/input"
    
    # Gestion du nommage : 
    datefichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Formater la date
    nom_fichier = f"clients_{datefichier}.xlsx"  # Créer un nom de fichier pour sauvegarder le fichier PDF
    file_path = os.path.join(path_to_input, nom_fichier)  # Chemin complet du fichier à enregistrer
    
    # Sauvegarder le fichier avec un nom spécifique dans le dossier spécifié
    file.save(file_path)
    
    
    
    return 'data from ISA OK...'