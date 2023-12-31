# services/__init__.py

from .Extract_info_from_pdf import (
    extract_text_from_pdf,
    search_patterns,
    create_excel_file
)
from .Extract_info_excel import exporter_cli_isfact_excel
from .DB_service import (
    Lire_BD_DIVALTO,
    Ecrire_MAJ_Clients_DIVALTO,
    lire_donnees_ISAFACT,
    Ecrire_MAJ_Clients_ISFACT,
    testServiceDB,
    lire_ecrire_mettre_a_jour_fichier_csv,
    lire_base_de_donnes_client,
    lire_ercrire_mettre_a_jour_table_geography,
    lire_donnees_BD_geography
)
from .DB_operations_service import (
    MaJ_Table_CLI_BY_ISAFACT,
    lire_donnees_CLI_ISAFACT,
    lire_donnes_SITE_ISFACT,
    KillAllTable,
    lire_donnes_RIB_ISFACT
)
from .DB_SITES_service import (
    Transfert_donnes_CLIENT_ISAFACT_SITES,
    numerotation_sites,
    correspondance_clientID_siteID
)
from .DB_CLI_services import (
    Transfert_donnes_CLIENT_ISAFACT_CLI,
    suppression_doublon_by_TEL1,
    suppression_doublon_by_TEL2,
    suppression_doublon_by_EMAIL,
    suppression_doublon_by_TEL1_ET_TEL2,
    numerotation_client,
    CodeStatisitique_CLI
)
from .DB_RIB_service import Ecrire_Table_RIB_from_ISAFACT
from .DB_GEOCODING_service import (
    Ecrire_base_GEOCODAGE,
    lire_base_site_geocodage,
    lire_base_site_geocodage_avec_contrats
)

from .DB_matériels_service import initialisation_table_materiel, lire_BD_materiel
from .DB_MODE_RGLT_service import initialisation_mode_paiement
from .DB_T119_CATEG_CLIENT_service import initialisation_T119
from .DB_T111_FAMILLE_CONTRAT_service import initialisation_T111
from .DB_ARTICLE_FACTURATION_CONTRAT_service import initialisation_Article_facturation_contrat
from .DB_CONTRAT_MODEL_service import initialisation_model_contrat
from .DB_TYPE_MODEL_service import initialisation_typemodel
from .DB_CLIENT_CONTRAT_ISAFACT_service import ecrire_table_base_client_contrat_isafact, lire_table_base_client_contrat_isafact, numerotation_contrat, lire_table_base_client_contrat_isafact
from .DB_RESSOURCE_MATERIEL_DIVALTO_service import ecrire_BD_RESSOURCE_MATERIEL_DIVALTO, lire_BD_RESSOURCE_MATERIEL_DIVALTO
from .DB_SITUATION_ISAFACT_service import lire_BD_SITUATION_ISFACT, intialisation_BD_SITUATION_ISFACT, lire_BD_SITUATION_ISAFACT_ByCodeClient
from .MAINTENANCE_DB_service import count_records_in_tables