# controller/Client_ISAFACT_controller.py
import os
from datetime import datetime
from app.services import Ecrire_MAJ_Clients_ISFACT, lire_donnees_ISAFACT, MaJ_Table_CLI_BY_ISAFACT, lire_donnees_CLI_ISAFACT

def importISAFACTDataFromExcel(file):
    # Enregistrer le fichier source
    # Gestion des chemins des fichiers :
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Récupérer le répertoire du fichier actuel (GRC_controller.py)
    path_to_input = os.path.join(current_directory, '..', '..', 'ressources', 'input', 'ISAFACT')  # Chemin vers le répertoire "ressources/input"
    
    # Gestion du nommage : 
    datefichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Formater la date
    nom_fichier = f"ISAFACT_{datefichier}.xlsx"  # Créer un nom de fichier pour sauvegarder le fichier PDF
    file_path = os.path.join(path_to_input, nom_fichier)  # Chemin complet du fichier à enregistrer
    
    # Sauvegarder le fichier avec un nom spécifique dans le dossier spécifié
    file.save(file_path)
    
    # Traitement du fichier excel
    result = Ecrire_MAJ_Clients_ISFACT(file_path)
    
    return result

def lireDonnesClientISAFACT():
    return lire_donnees_ISAFACT()

def extraire_CLI_from_DATA_brut_ISFACT():
    result = MaJ_Table_CLI_BY_ISAFACT()
    return result

def lire_BD_CLI_ISFACT():
    result = lire_donnees_CLI_ISAFACT()
    return result