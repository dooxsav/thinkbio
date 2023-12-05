from app.services import *

def lireBaseCLientContrat():
    #Lecture de la base client
    result = lire_table_base_client_contrat_isafact()
    return result