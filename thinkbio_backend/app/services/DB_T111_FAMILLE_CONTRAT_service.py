from app import db
from app.models import T111_FAMILLE_CONTRAT_DIVALTO
import os
import json

def initialisation_T111():
    print('\033[34m * Initialisation table T101 - FAMILLE CONTRAT...\033[0m')
    try:
        data = load_data_from_json()
        insert_data_to_db(data)
        print('\033[32m *** TABLE T101 synchronisée ***\033[0m')
    except Exception as error:  # Ajout du type d'exception et utilisation de 'Exception'
        print('\033[91m ** Erreur lors de l\'initialisation de la table T101 - FAMILLE CONTRAT:\033[0m', error)
    
def load_data_from_json():
    file_path = "../../ressources/input/EQUIV_ISA_DIVALTO/T119_Categorie_client.json"
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, '../../ressources/input/EQUIV_ISA_DIVALTO/T101_FAMILLE_CONTRAT.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def insert_data_to_db(data):
    for item in data:
        new_entry = T111_FAMILLE_CONTRAT_DIVALTO(
            DOSSIER = item['DOSSIER'],
            FAMILLECONTRAT = item['FAMILLECONTRAT'],
            EQUIV_ISFACT_CodeTypeCONTRAT = item['EQUIV_ISFACT_CodeTypeCONTRAT'],
            NUMERONOTE = item['NUMERONOTE'],
            LIBELLE_TABLE_FAMILLECONTRAT = item['LIBELLE_TABLE_FAMILLECONTRAT'],
            CONTRATTYP = item['CONTRATTYP'],
            DATEFINVALID = item['DATEFINVALID'],
            STRUCTUREREFERENCECONTRAT = item['STRUCTUREREFERENCECONTRAT'],
            CRMUPDATEDH = item['CRMUPDATEDH'],
        )
        db.session.add(new_entry)
    
    db.session.commit()