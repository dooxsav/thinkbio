# controller/Client_ISAFACT_controller.py
import os
from datetime import datetime
from app.services import numerotation_contrat, Ecrire_MAJ_Clients_ISFACT, lire_donnees_ISAFACT, MaJ_Table_CLI_BY_ISAFACT, lire_donnees_CLI_ISAFACT, lire_donnes_SITE_ISFACT, lire_donnes_RIB_ISFACT, Transfert_donnes_CLIENT_ISAFACT_SITES, numerotation_sites, Transfert_donnes_CLIENT_ISAFACT_CLI, suppression_doublon_by_TEL1, suppression_doublon_by_TEL2, suppression_doublon_by_EMAIL, correspondance_clientID_siteID, numerotation_client, exporter_cli_isfact_excel, Ecrire_Table_RIB_from_ISAFACT, Ecrire_base_GEOCODAGE, suppression_doublon_by_TEL1_ET_TEL2, KillAllTable, CodeStatisitique_CLI, ecrire_table_base_client_contrat_isafact, initialisation_mode_paiement, initialisation_T119, initialisation_Article_facturation_contrat,    initialisation_mode_paiement, initialisation_T111, initialisation_typemodel, initialisation_model_contrat, initialisation_table_materiel, ecrire_BD_RESSOURCE_MATERIEL_DIVALTO, intialisation_BD_SITUATION_ISFACT

def dosomeMagical(file):
    # Etape 1 - Récupérer les informations dans le fichier Excel et peupler la base CLIENT_ISAFACT
    lignes_ajoutees, ligne_modifies = importISAFACTDataFromExcel(file)
    
    # Etape 2 - Créer un table SITE qui est l'image de la table CLIENT_ISAFACT avec des informations en moins
    ligne_table_SITE_ajoutes, ligne_table_SITE_modifiees = Transfert_donnes_CLIENT_ISAFACT_SITES()
    nombre_site_numeroté = numerotation_sites()
    
    # Etape 3 - Créer un table CLI qui est l'image de la table CLIENT_ISFACT avec des informations spécifique aux client
    ligne_table_CLI_ajoutes, ligne_table_CLI_modifiees = Transfert_donnes_CLIENT_ISAFACT_CLI()
    doublons_supprimes_EMAIL, SITE_Maj = suppression_doublon_by_EMAIL()
    doublons_supprimes_Tel1, SITE_Maj = suppression_doublon_by_TEL1()
    doublons_supprimes_Tel2, SITE_Maj = suppression_doublon_by_TEL2()
    doublons_supprimes_Tel1_TEL2, SITE_Maj = suppression_doublon_by_TEL1_ET_TEL2()
    nombre_client_numeroté = numerotation_client()
    nombre_client_axe = CodeStatisitique_CLI()
    # Etape 4 - Faire la correspondance entre CLI et SITE
    nbre_correspondance = correspondance_clientID_siteID()

    # Etape 5 - Ecrire la base RIB
    ligne_ajoutées_RIB, ligne_modifie_RIB = Ecrire_Table_RIB_from_ISAFACT()
    
    # Etape - Ecrire la base contrat
    lignes_ajoutees_contrat, lignes_modifiee_contrat = ecrire_table_base_client_contrat_isafact()
    nombre_contrat_numerote = numerotation_contrat()
    
    # Etape - Ecrire dans la base MATERIELS
    ligne_ajoute, ligne_modifie = ecrire_BD_RESSOURCE_MATERIEL_DIVALTO()
    # Etape 7 - Géocodage
    exporter_cli_isfact_excel()
    
    # Etape 6 - Export des informations sous excel
    Ecrire_base_GEOCODAGE()
    
    return 'Job Done'
    
def preparation_import():
    # Destruction des tables
    KillAllTable()
    # Reconstruction des données en dur
    print('\033[33m ** Synchronisation des modèles: **\033[0m ')
    intialisation_BD_SITUATION_ISFACT()
    initialisation_table_materiel()
    initialisation_model_contrat()
    initialisation_mode_paiement()
    initialisation_T119()
    initialisation_Article_facturation_contrat()
    initialisation_mode_paiement()
    initialisation_T111()
    initialisation_typemodel()
    return None

def importISAFACTDataFromExcel(file):
    # Enregistrer le fichier source
    # Gestion des chemins des fichiers :
    preparation_import()
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Récupérer le répertoire du fichier actuel (GRC_controller.py)
    path_to_input = os.path.join(current_directory, '..', '..', 'ressources', 'input', 'ISAFACT')  # Chemin vers le répertoire "ressources/input"
    
    # Gestion du nommage : ssssssss
    datefichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Formater la date
    nom_fichier = f"ISAFACT_{datefichier}.xlsx"  # Créer un nom de fichier pour sauvegarder le fichier PDF
    file_path = os.path.join(path_to_input, nom_fichier)  # Chemin complet du fichier à enregistrer
    
    # Sauvegarder le fichier avec un nom spécifique dans le dossier spécifié
    file.save(file_path)
    
    # Traitement du fichier excel
    lignes_ajoutees, ligne_modifies = Ecrire_MAJ_Clients_ISFACT(file_path)
    
    return lignes_ajoutees, ligne_modifies

def extraire_CLI_from_DATA_brut_ISFACT():
    result = MaJ_Table_CLI_BY_ISAFACT()
    return result

def lire_BD_CLI_ISFACT():
    result = lire_donnees_CLI_ISAFACT()
    return result

def lire_BD_SITE_ISAFACT():
    result = lire_donnes_SITE_ISFACT()
    return result

def lireDonnesClientISAFACT():
    return lire_donnees_ISAFACT()

def lire_Table_RIB_ISAFACT():
    return lire_donnes_RIB_ISFACT()
