import json
from app import db
from datetime import datetime
from app.models import ARTICLE_FACTURATION_CONTRAT  # Importez votre modèle de données
import os

def initialisation_Article_facturation_contrat():
    print('\033[34m * Initialisation de la table ArticleFacturationContrat...\033[0m')
    try:
        data = load_data_from_json()
        insert_data_to_db(data)
        print('\033[32m * ArticleFacturationContrat synchronisée\033[0m')
    except Exception as error:  # Ajout du type d'exception et utilisation de 'Exception'
        print(' ** Erreur lors de l\'initialisation de la table ArticleFacturationContrat:', error)
      
def load_data_from_json():
    file_path = "../../ressources/input/EQUIV_ISA_DIVALTO/ArticleFacturationContrat.json"
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, '../../ressources/input/EQUIV_ISA_DIVALTO/ArticleFacturationContrat.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def insert_data_to_db(data):
    for item in data:
        new_entry = ARTICLE_FACTURATION_CONTRAT(
                CODECONTRAT=item['CODECONTRAT'],
                LIGNE=item['LIGNE'],
                REFERENCE=item['REFERENCE'],
                DESIGNATION=item['DESIGNATION'],
                POURCENT=item['POURCENT'],
                EQUIV_ISAFACT=item['EQUIV_ISAFACT']
        )
        db.session.add(new_entry)
    
    db.session.commit()