import pandas as pd
import os 
from app.models import CLI_ISFACT
from datetime import datetime

def exporter_cli_isfact_excel():
    # Gestion des chemins des fichiers :
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path_to_output = os.path.join(current_directory, '..', '..', 'ressources', 'output', 'CLI_ISAFACT')

    # Gestion du nommage :
    date_fichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"ISAFACT_{date_fichier}.xlsx"
    file_path = os.path.join(path_to_output, nom_fichier)

    # Récupérer toutes les données de la table CLI_ISFACT
    cli_isfact_data = CLI_ISFACT.query.all()

    # Créer un DataFrame pandas avec les données
    df = pd.DataFrame([
        {
            'CodeClient': entry.CodeClient,
            'Client_id': entry.Client_id,
            'FamilleTIERS': entry.FamilleTIERS,
            'NomFACT': entry.NomFACT,
            'PrenomFACT': entry.PrenomFACT,
            'AdresseFACT': entry.AdresseFACT,
            'CPFACT': entry.CPFACT,
            'VilleFACT': entry.VilleFACT,
            'PaysFACT': entry.PaysFACT,
            'EmailTIERS': entry.EmailTIERS,
            'Tel1': entry.Tel1,
            'Tel2': entry.Tel2,
            'Tel3': entry.Tel3,
            'createdAt': entry.createdAt,
            'createdBy': entry.createdBy,
            'updatedAt': entry.updatedAt,
            'lastUpdatedBy': entry.lastUpdatedBy
        }
        for entry in cli_isfact_data
    ])

    # Assurer que le dossier de sortie existe
    os.makedirs(path_to_output, exist_ok=True)

    # Exporter le DataFrame vers un fichier Excel
    df.to_excel(file_path, index=False, engine='openpyxl')