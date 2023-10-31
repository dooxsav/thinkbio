# controller/client_controller

from app.services import testFonctionnel, lire_ecrire_fichier_csv
from werkzeug.utils import secure_filename
import os
from datetime import datetime

def populate_DB_Client(file):
    # Gestion des chemins des fichiers :
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Récupérer le répertoire du fichier actuel (GRC_controller.py)
    path_to_input = os.path.join(current_directory, '..', '..', 'ressources', 'input', 'Clients')  # Chemin vers le répertoire "ressources/input"
    
    # Gestion du nommage : 
    datefichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Formater la date
    nom_fichier = f"clients_{datefichier}.pdf"  # Créer un nom de fichier pour sauvegarder le fichier PDF
    file_path = os.path.join(path_to_input, nom_fichier)  # Chemin complet du fichier à enregistrer
    
    # Sauvegarder le fichier avec un nom spécifique dans le dossier spécifié
    file.save(file_path)
    
    result = lire_ecrire_fichier_csv(file_path)
    return result