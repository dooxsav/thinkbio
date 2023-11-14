# controllers/Client_DIVALTO_controller.py
#
# Controller de gestion DIVALTO
#
#
#

from app.services import lire_donnees_ISAFACT, Ecrire_MAJ_Clients_DIVALTO, Lire_BD_DIVALTO
from datetime import datetime
import os

# Fonction de récupération des informations des tables
def process_and_store_data():
    # Récupération des données de la table client
    data_from_table_ClientISAFACT = lire_donnees_ISAFACT()
    
    return None

def importDIVALTODataFromExcel(file):
    # Enregistrer le fichier source
    # Gestion des chemins des fichiers :
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Récupérer le répertoire du fichier actuel (GRC_controller.py)
    path_to_input = os.path.join(current_directory, '..', '..', 'ressources', 'input', 'DIVALTO')  # Chemin vers le répertoire "ressources/input"
    
    # Gestion du nommage : 
    datefichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Formater la date
    nom_fichier = f"DIVALTO_{datefichier}.xlsx"  # Créer un nom de fichier pour sauvegarder le fichier PDF
    file_path = os.path.join(path_to_input, nom_fichier)  # Chemin complet du fichier à enregistrer
    
    # Sauvegarder le fichier avec un nom spécifique dans le dossier spécifié
    file.save(file_path)
    
    # Traitement du fichier excel
    result = Ecrire_MAJ_Clients_DIVALTO(file_path)
    
    
    return result

def lireBDDDIVALTO():
    return Lire_BD_DIVALTO()