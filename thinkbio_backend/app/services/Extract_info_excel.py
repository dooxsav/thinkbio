import pandas as pd
import os 
from app.models import CLI_ISFACT, SITE_ISAFACT, RIB_ISAFACT
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from tqdm import tqdm

import os
from datetime import datetime
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def exporter_cli_isfact_excel():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path_to_output = os.path.join(current_directory, '..', '..', 'ressources', 'output', 'CLI_ISAFACT')

    date_fichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"ISAFACT_{date_fichier}.xlsx"
    file_path = os.path.join(path_to_output, nom_fichier)

    # Gestion des cli
    cli_isfact_data = CLI_ISFACT.query.all()

    df_cli = pd.DataFrame([
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

    # Exporter le DataFrame df_cli vers un fichier Excel
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df_cli.to_excel(writer, sheet_name='CLI_ISAFACT', index=False)

        # Extraction table SITE
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

        df_site.to_excel(writer, sheet_name='SITE_ISAFACT', index=False)

        # Extraction table RIB_ISAFACT
        rib_isfact_data = RIB_ISAFACT.query.all()

        df_rib = pd.DataFrame([
            {
                'Client_id': entry.Client_id,
                'CodeClient': entry.CodeClient,
                'FamilleTIERS': entry.FamilleTIERS,
                'IBANPAYS': entry.IBANPAYS,
                'IBANCLE': entry.IBANCLE,
                'IBANCOMPTE': entry.IBANCOMPTE,
                'RIBBIC': entry.RIBBIC,
                'RIBDO': entry.RIBDO
            }
            for entry in rib_isfact_data
        ])

        df_rib.to_excel(writer, sheet_name='RIB_ISAFACT', index=False)
