from app import db
from app.models import SITUATION_ISAFACT
from datetime import datetime
import pandas as pd
import os

def lire_BD_SITUATION_ISFACT():
    records = SITUATION_ISAFACT.query.all()
    return [record.to_dict() for record in records]  # Convertir les objets en dictionnaires

def intialisation_BD_SITUATION_ISFACT():
    print('\033[33m * Import de la base SITUATION via fichier Excel... \033[0m')
    ligne_ajoute = 0
    ligne_modifie = 0
    ligne_ignore = 0
    # Chemin du répertoire du script
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Chemin vers le fichier Excel en utilisant os.path.join pour construire le chemin
    file_path = os.path.join(script_directory, "..", "..", "ressources", "input", "ISAFACT", "ISFACT_DONNES_SITUATION_INI.xlsx")

    # Maintenant, utilisez file_path dans votre code pour charger le fichier Excel
    dataFrame = pd.read_excel(file_path)
    longueur_df = len(dataFrame)
    
    for index, row in dataFrame.iterrows():
        if row['Libellé famille tiers'] == "PARTICULIER pour le SAV":
            new_ecriture = SITUATION_ISAFACT(
                date_document = datetime.strptime(str(row['Date document']), '%d/%m/%Y').date() if str(row['Date document']) else None,
                numero_document = str(row['Numéro document']),
                nom= str(row['Nom']),
                prenom= str(row['Prénom']),
                CodeClient= str(row['Code']),
                libelle_famille_tiers= str(row['Libellé famille tiers']),
                code_postal= str(row['Code postal']),
                nom_representant= str(row['Nom représentant']),
                code_article= str(row['Code Article']),
                designation_courte_article= str(row['Désignation courte article']),
                code_lot_articles= str(row['Code lot articles']),
                code_lot_facture= str(row['Code lot facture']),
                libelle_lot_facture= str(row['Libellé lot facture']),
                code_famille_article= str(row['Code famille article']),
                libelle_famille_article= str(row['Libellé famille article']),
                compte_de_vente= str(row['Compte de vente']),
                quantite_unit= str(row['Quantité unit']).replace(',', '.'),
                montant_HT= row['Mt HT'].replace(',', '.'),
                volume= str(row['Volume']),
                code_divers= str(row['Code divers']),
                date_livraison_document= datetime.strptime(str(row['Date de livraison document']), '%d/%m/%Y').date() if str(row['Date document']) else None
            )
            db.session.add(new_ecriture)
            ligne_ajoute += 1
        else:
            ligne_ignore += 1
        print(f"\r * Progression : {round(((ligne_ajoute + ligne_ignore) / longueur_df) * 100, 1)}%", end='', flush=True)
    print('\033[0;32m * DONE ! => ECRITURE EN BD')
    db.session.commit()
    print(f'\033[92m * Base de données SITUATION écrite. {ligne_ajoute} ligne(s) ont été ajoutée(s), {ligne_ignore} ligne(s) ont été ignorée(s)\033[0m')
    return None