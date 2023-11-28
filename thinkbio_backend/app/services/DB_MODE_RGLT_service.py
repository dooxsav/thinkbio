import json
from app import db
from datetime import datetime
from app.models import EQUIV_MODE_RGLT_ISA_DIV  # Importez votre modèle de données
import os

def initialisation_mode_paiement():
    print(' * Initialisation des modes de paiement...')
    try:
        data = load_data_from_json()
        insert_data_to_db(data)
        print(' * Application is Ready...')
    except Exception as error:  # Ajout du type d'exception et utilisation de 'Exception'
        print(' ** Erreur lors de l\'initialisation de la table PAIEMENT:', error)
    
    
def load_data_from_json():
    file_path = "../../ressources/input/MODE_RGLT/equiv_mde_rglt.json"
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, '../../ressources/input/MODE_RGLT/equiv_mde_rglt.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def insert_data_to_db(data):
    for item in data:
        new_entry = EQUIV_MODE_RGLT_ISA_DIV(
            code_ISA=item['code_ISA'],
            code_Divalto=item['code_Divalto'],
            libelle_code_rglt=item['libelle_code_rglt'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_entry)
    
    db.session.commit()