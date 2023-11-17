import pandas as pd
import os 
from app.models import CLI_ISFACT, SITE_ISAFACT
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from tqdm import tqdm

def exporter_cli_isfact_excel():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path_to_output = os.path.join(current_directory, '..', '..', 'ressources', 'output', 'CLI_ISAFACT')

    date_fichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"ISAFACT_{date_fichier}.xlsx"
    file_path = os.path.join(path_to_output, nom_fichier)

    cli_isfact_data = CLI_ISFACT.query.all()

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
    
    # Exporter le DataFrame df vers un fichier Excel
    df.to_excel(file_path, index=False, engine='openpyxl')

    wb = load_workbook(file_path)

    table_name = CLI_ISFACT.__tablename__
    sheet = wb.active
    sheet.title = table_name

    site_isfact_data = SITE_ISAFACT.query.all()

    df_site = pd.DataFrame([
        {
            'Site_id': entry.Site_id,
            'Client_id': entry.Client_id,
            'CodeClient': entry.CodeClient,
            'FamilleTIERS': entry.FamilleTIERS,
            'AdresseSite': entry.AdresseSite,
            'VilleSite': entry.VilleSite,
            'CPSite': entry.CPSite,
            'CreatedAt': entry.CreatedAt,
            'UpdatedAt': entry.UpdatedAt,
            'CreatedBy': entry.CreatedBy,
            'LastUpdatedBy': entry.LastUpdatedBy
        }
        for entry in site_isfact_data
    ])

    ws_site = wb.create_sheet(title="SITE_ISAFACT")

    # Utilisation de tqdm pour la barre de progression
    for r in tqdm(dataframe_to_rows(df_site, index=False, header=True), desc="Exportation des données", unit="ligne"):
        ws_site.append(r)

    wb.save(file_path)