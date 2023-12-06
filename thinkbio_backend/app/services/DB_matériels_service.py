from app import db
from app.models import MATERIEL_ISAFACT
import pandas as pd
from tqdm import tqdm
from unidecode import unidecode
import numpy as np  # Importation du module numpy
import os

def lire_BD_materiel():
    stations = MATERIEL_ISAFACT.query.all()
    return [station.to_dict() for station in stations]  # Convertir les objets en dictionnaires

def initialisation_table_materiel():
    print('\033[33m * Ecriture des matériels...\033[0m')
    ligne_ajoutee = 0
    ligne_modifie = 0
    # Chemin du répertoire du script
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Chemin vers le fichier Excel en utilisant os.path.join pour construire le chemin
    file_path = os.path.join(script_directory, "..", "..", "ressources", "input", "MATERIELS", "ressource_materiel_base.xlsx")

    # Maintenant, utilisez file_path dans votre code pour charger le fichier Excel
    dataFrame = pd.read_excel(file_path)

    for index, row in dataFrame.iterrows():
        station_existante = MATERIEL_ISAFACT.query.filter_by(CodeClient=row['CodeClient']).first()
        if station_existante:
            station_existante.NO_SERIE_BIONEST = str(row['NO_SERIE_BIONEST']).upper()
            station_existante.MODELE_SYSTEME = str(row['MODELE_SYSTEME']).upper()
            station_existante.MATERIAUX = unidecode(str((row['MATERIAUX']))).upper()
            station_existante.FABRIQUANT_CUVE = unidecode(str((row['FABRIQUANT_CUVE']))).upper()
            station_existante.GENRE = unidecode(str(row['GENRE'])).upper()  # Correction ici
            station_existante.TYPE = unidecode(str(row['TYPE'])).upper()
            ligne_modifie += 1
        else:
            new_station = MATERIEL_ISAFACT(
                NO_SERIE_BIONEST=str(row['NO_SERIE_BIONEST']).upper(),
                MODELE_SYSTEME=str(row['MODELE_SYSTEME']).upper(),
                MATERIAUX=unidecode(str(row['MATERIAUX'])).upper(),
                FABRIQUANT_CUVE=unidecode(str(row['FABRIQUANT_CUVE'])).upper(),
                GENRE=unidecode(str(row['GENRE'])).upper(),
                TYPE=unidecode(str(row['TYPE'])).upper(),
                CodeClient=str(row['CodeClient']).upper()  # Correction ici
            )
            db.session.add(new_station)
            ligne_ajoutee += 1

    
    db.session.commit()
    print(f'\033[38;2;0;255;0m * Données matériels synchronisée {ligne_ajoutee} ligne(s) ont été ajoutée(s) et {ligne_modifie} ligne(s) ont été modifiée(s)\033[0m')
    return ligne_ajoutee, ligne_modifie
        
    
    
        
