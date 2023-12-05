import json
from app import db
from datetime import datetime
from app.models import CONTRAT_MODEL  # Importez votre modèle de données
import os

def initialisation_mode_paiement():
    print('\033[34m * Initialisation de la table CONTRAT MODELE...\033[0m')
    try:
        data = load_data_from_json()
        insert_data_to_db(data)
        print('\033[32m * CONTRAT MODELE synchronisée\033[0m')
    except Exception as error:  # Ajout du type d'exception et utilisation de 'Exception'
        print('\033[91m ** Erreur lors de l\'initialisation de la table CONTRAT MODELE:\033[0m', error)
      
def load_data_from_json():
    file_path = "../../ressources/input/EQUIV_ISA_DIVALTO/CONTRAT_MODEL.json"
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, '../../ressources/input/EQUIV_ISA_DIVALTO/CONTRAT_MODEL.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def insert_data_to_db(data):
    for item in data:
        new_entry = CONTRAT_MODEL(
            DOSSIER = item["DOSSIER"],
            EQUIV_ISAFACT = item["EQUIV_ISAFACT"],
            CODECONTRAT = item["CODECONTRAT"],
            NUMERONOTE = item["NUMERONOTE"],
            LIBELLE_CONTRAT_MODELE = item["LIBELLE_CONTRAT_MODELE"],
            CODEOPERATION = item["CODEOPERATION"],
            REFERENCE = item["REFERENCE"],
            INDICEARTICLE = item["INDICEARTICLE"],
            SREFERENCE1 = item["SREFERENCE1"],
            SREFERENCE2 = item["SREFERENCE2"],
            CODETARIF = item["CODETARIF"],
            CODETARIFTTC = item["CODETARIFTTC"],
            FACTUREMANUELLE = item["FACTUREMANUELLE"],
            AXE1 = item["AXE1"],
            AXE2 = item["AXE2"],
            AXE3 = item["AXE3"],
            AXE4 = item["AXE4"],
            MODECALCULMONTANT = item["MODECALCULMONTANT"],
            MONTANT = item["MONTANT"],
            TXTPREENREG = item["TXTPREENREG"],
            TEXTETYP = item["TEXTETYP"],
            TYPECALENDRIERFACTURATION = item["TYPECALENDRIERFACTURATION"],
            TAUXSURPRIXVENTE = item["TAUXSURPRIXVENTE"],
            TAUX1SURPRIXVENTE = item["TAUX1SURPRIXVENTE"],
            INDICATEURSIREGROUPEMENT = item["INDICATEURSIREGROUPEMENT"],
            FACTURATIONCONDITIONNELLE = item["FACTURATIONCONDITIONNELLE"],
            TAFAMINTER = item["TAFAMINTER"],
            TAFAMXINTER = item["TAFAMXINTER"],
            PROMOTACODINTER = item["PROMOTACODINTER"],
            TACODINTER = item["TACODINTER"],
            REFAMXINTER = item["REFAMXINTER"],
            REFAMINTER = item["REFAMINTER"],
            PROMOREMCODINTER = item["PROMOREMCODINTER"],
            REMCODINTER = item["REMCODINTER"],
            REMINTER1 = item["REMINTER1"],
            REMINTER2 = item["REMINTER2"],
            REMINTER3 = item["REMINTER3"],
            REMTYPINTER1 = item["REMTYPINTER1"],
            REMTYPINTER2 = item["REMTYPINTER2"],
            REMTYPINTER3 = item["REMTYPINTER3"],
            CODEINTERVENTION = item["CODEINTERVENTION"],
            FAMODTYP = item["FAMODTYP"],
            CODECOMPTEUR = item["CODECOMPTEUR"],
            CPTACTUFL = item["CPTACTUFL"],
            MOINCLUFLG = item["MOINCLUFLG"],
            PCEINCLUFLG = item["PCEINCLUFLG"],
            DEPINCLUFLG = item["DEPINCLUFLG"],
            FADETAILTYP = item["FADETAILTYP"],
        )
        db.session.add(new_entry)
    
    db.session.commit()