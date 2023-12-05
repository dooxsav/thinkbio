from app import db
from app.models import TYPE_MATERIEL
import os
import json

def initialisation_typemodel():
    print('\033[34m * Initialisation table TYPE MODEL...\033[0m')
    try:
        data = load_data_from_json()
        insert_data_to_db(data)
        print('\033[32m * table TYPE MODEL synchronisée\033[0m')
    except Exception as error:  # Ajout du type d'exception et utilisation de 'Exception'
        print('\033[91m ** Erreur lors de l\'initialisation de la table TYPE MODEL:\033[0m', error)
    
def load_data_from_json():
    file_path = "../../ressources/input/EQUIV_ISA_DIVALTO/TYPE_MATERIEL_RESSOURCE.json"
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, '../../ressources/input/EQUIV_ISA_DIVALTO/TYPE_MATERIEL_RESSOURCE.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def insert_data_to_db(data):
    for item in data:
        new_entry = TYPE_MATERIEL(
            DOSSIER=item['DOSSIER'],
            CODEGENRE=item['CODEGENRE'],
            CODETYPERESSOURCEMATERIEL=item['CODETYPERESSOURCEMATERIEL'],
            NUMERONOTE=item['NUMERONOTE'],
            PRESENCEJOINT=item['PRESENCEJOINT'],
            INDICEDOCUMENTREFERENCE=item['INDICEDOCUMENTREFERENCE'],
            DATEFINVALID=item['DATEFINVALID'],
            LIBELLE_TYPE=item['LIBELLE_TYPE'],
            INDICATEURSIMOBILE=item['INDICATEURSIMOBILE'],
            QUESTION=item['QUESTION'],
            NATIMMO=item['NATIMMO'],
            UTILISATEURMANAGER=item['UTILISATEURMANAGER'],
            TYPECRMFL=item['TYPECRMFL'],
            CRMUPDATEDH=item['CRMUPDATEDH']
        )
        db.session.add(new_entry)
    
    db.session.commit()