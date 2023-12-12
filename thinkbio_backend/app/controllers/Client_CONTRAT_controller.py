from app.services import *
from flask import jsonify

def lireBaseCLientContrat():
    #Lecture de la base client
    result = lire_table_base_client_contrat_isafact()
    return result

def nombre_enregistrement_Client_Contrat():
    result = "toto"
    return jsonify({f"message": {result}})