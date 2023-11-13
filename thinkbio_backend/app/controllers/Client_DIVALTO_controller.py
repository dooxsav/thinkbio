# controllers/Client_DIVALTO_controller.py
from app.services import lire_donnees_ISAFACT

# Fonction de récupération des informations des tables
def process_and_store_data():
    # Récupération des données de la table client
    data_from_table_ClientISAFACT = lire_donnees_ISAFACT()
    
    return None
