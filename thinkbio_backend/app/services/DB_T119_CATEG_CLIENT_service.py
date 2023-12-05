from app import db
from app.models import T119_CATEG_CLIENT
import os
import json

def initialisation_T119():
    print('\033[34m * Initialisation table T119 - catégorie clients...\033[0m')
    try:
        data = load_data_from_json()
        insert_data_to_db(data)
        print('\033[32m * table T119 synchronisée\033[0m')
    except Exception as error:  # Ajout du type d'exception et utilisation de 'Exception'
        print('\033[91m ** Erreur lors de l\'initialisation de la table T119 - categ client:\033[0m', error)
    
def load_data_from_json():
    file_path = "../../ressources/input/EQUIV_ISA_DIVALTO/T119_Categorie_client.json"
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, '../../ressources/input/EQUIV_ISA_DIVALTO/T119_Categorie_client.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def insert_data_to_db(data):
    for item in data:
        new_entry = T119_CATEG_CLIENT(
            CATCLICOD=item['CATCLICOD'],
            LIBELLE_TABLE_CATEGORIECLIENT=item['LIBELLE_TABLE_CATEGORIECLIENT'],
            EQUIV_ISAFACT=item['EQUIV_ISAFACT'],
        )
        db.session.add(new_entry)
    
    db.session.commit()