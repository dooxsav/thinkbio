# services/DB_site.py
#

from app import db
from app.models import Client_ISAFACT, CLI_ISFACT, SITE_ISAFACT, EQUIV_MODE_RGLT_ISA_DIV
from tqdm import tqdm
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
import re

def Transfert_donnes_CLIENT_ISAFACT_CLI():
    print(' * Ecriture de la base CLI...')
    Donnes_depuis_CLIENT_ISAFACT = Client_ISAFACT.query.all()
    lignes_ajoutées = 0
    lignes_modifiées = 0

    for client in tqdm(Donnes_depuis_CLIENT_ISAFACT, desc='Processing CLI from ISAFACT', unit="CLI/s"):
        # Utilisation de sorted au lieu de sort pour obtenir une nouvelle liste triée
        num_tel = sorted([client.TelFACT1, client.TelFACT2, client.TelFACT3], reverse=True)

        # Initialisation de Mode_rglt_Code pour éviter une erreur de variable non définie
        Mode_rglt_Code = None

        # Correspondances des moyens de paiement
        equiv_mde_reglement = EQUIV_MODE_RGLT_ISA_DIV.query.filter_by(code_ISA=client.Code_Rglt).first()
        Mode_rglt_Code = equiv_mde_reglement.code_Divalto if equiv_mde_reglement else "N/C"

        # Ecriture dans la BD
        try:
            entrée_CLI = CLI_ISFACT.query.filter_by(CodeClient=client.CodeClient).one()
            # Les virgules en trop après chaque assignation ont été retirées
            entrée_CLI.CodeClient = client.CodeClient
            entrée_CLI.FamilleTIERS = client.FamilleTIERS
            entrée_CLI.NomFACT = client.NomFACT
            entrée_CLI.PrenomFACT = client.PrenomFACT
            entrée_CLI.AdresseFACT = client.AdresseFACT
            entrée_CLI.CPFACT = client.CPFACT
            entrée_CLI.VilleFACT = client.VilleFACT
            entrée_CLI.PaysFACT = client.PaysFACT
            entrée_CLI.EmailTIERS = client.EmailTIERS
            entrée_CLI.Tel1 = num_tel[0]
            entrée_CLI.Tel2 = num_tel[1]
            entrée_CLI.Tel3 = num_tel[2]
            entrée_CLI.Mode_RGLT = str(Mode_rglt_Code)
            entrée_CLI.updatedAt = datetime.now()
            entrée_CLI.lastUpdatedBy = 'ADMIN'
            lignes_modifiées += 1
        except NoResultFound:
            new_CLI_entry = CLI_ISFACT(
                CodeClient=client.CodeClient,
                FamilleTIERS=client.FamilleTIERS,
                NomFACT=client.NomFACT,
                PrenomFACT=client.PrenomFACT,
                AdresseFACT=client.AdresseFACT,
                CPFACT=client.CPFACT,
                VilleFACT=client.VilleFACT,
                PaysFACT=client.PaysFACT,
                EmailTIERS=client.EmailTIERS,
                Tel1=num_tel[0],
                Tel2=num_tel[1],
                Tel3=num_tel[2],
                Mode_RGLT= str(Mode_rglt_Code),  # S'assurer que Mode_rglt_Code est défini
                createdAt=datetime.now(),
                createdBy='CREATOR',
                updatedAt=datetime.now(),
                lastUpdatedBy='CREATOR'
            )
            db.session.add(new_CLI_entry)
            lignes_ajoutées += 1

    db.session.commit()
    return lignes_ajoutées, lignes_modifiées

def numerotation_client():
    # Cette fonction numérote les site avec 10 chiffres NON significatif
    print(' * Numérating clients....')
    Données_client = CLI_ISFACT.query.all()
    longueur_table = len(Données_client)
    compteur_site = 0
    for client in tqdm(Données_client, desc=" * Numerating client", unit="site/s", total=longueur_table):
        client.Client_id = f'C{compteur_site:010d}'
        compteur_site += 1  # Incrémente compteur_site pour chaque site
    db.session.commit()
    return compteur_site

# // a faire
def CodeStatisitique_CLI():
    # Mise en place des axes statistiques sur les CLI
    # Cette fonction numérote les sites avec 10 chiffres NON significatifs
    print(' * Establishing Statistics Axes for clients....')
    Donnees_client = CLI_ISFACT.query.all()
    longueur_table = len(Donnees_client)
    compteur_client = 0

    for client in tqdm(Donnees_client, desc=" * Attributing statistic Axes", total=longueur_table):
        if re.search(r'\b' + re.escape("SARL") + r'\b', client.NomFACT):
            client.Axe_stat_1 = "MOPRIVEE"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
        elif re.search(r'\b' + re.escape("SAS") + r'\b', client.NomFACT):
            client.Axe_stat_1 = "MOPRIVEE"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
        elif re.search(r'\b' + re.escape("SASU") + r'\b', client.NomFACT):
            client.Axe_stat_1 = "MOPRIVEE"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
        elif re.search(r'\b' + re.escape("EARL") + r'\b', client.NomFACT):
            client.Axe_stat_1 = "MOPRIVEE"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
        elif re.search(r'\b' + re.escape("SCEA") + r'\b', client.NomFACT):
            client.Axe_stat_1 = "MOPRIVEE"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
        elif re.search(r'\b' + re.escape("CHATEAU") + r'\b', client.NomFACT):
            client.Axe_stat_1 = "MOPRIVEE"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
        elif client.FamilleTIERS == 'PARTICULIER pour le SAV':
            if client.NomFACT.startswith("SCI"):
                client.Axe_stat_1 = "SCI"
                client.Axe_stat_2 = ""
                client.Axe_stat_3 = ""
            elif client.NomFACT.startswith("MAIRIE"):
                client.Axe_stat_1 = "MOPUBLIQ"
                client.Axe_stat_2 = ""
                client.Axe_stat_3 = ""
            elif client.NomFACT.startswith("COMMUN"):
                client.Axe_stat_1 = "MOPUBLIQ"
                client.Axe_stat_2 = ""
                client.Axe_stat_3 = ""
            else:
                client.Axe_stat_1 = "PARTICUL"
                client.Axe_stat_2 = ""
                client.Axe_stat_3 = ""
        elif client.FamilleTIERS == 'NEGOCE':
            client.Axe_stat_1 = "REVENDEU"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
        elif client.FamilleTIERS == 'CONCESSIONAIRE':
            client.Axe_stat_1 = "REVENDEU"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
        elif client.FamilleTIERS == 'ENTREPRISES DE POSE':
            client.Axe_stat_1 = "INSTALLA"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
        else:
            client.Axe_stat_1 = "AUTRES"
            client.Axe_stat_2 = ""
            client.Axe_stat_3 = ""
            
    compteur_client += 1
    db.session.commit()
    return compteur_client

def suppression_doublon_by_TEL1_ET_TEL2():
    doublons_supprimes = 0
    SITE_Maj = 0
    
    # Récupérer les doublons pour Tel1 et Tel2 ensemble
    clients_tel1_tel2 = (
        db.session.query(CLI_ISFACT.Tel1, CLI_ISFACT.Tel2)
        .filter(CLI_ISFACT.FamilleTIERS == 'PARTICULIER pour le SAV')
        .filter(CLI_ISFACT.Tel1 != '')  # Exclure les enregistrements avec Tel1 vide
        .filter(CLI_ISFACT.Tel2 != '')  # Exclure les enregistrements avec Tel2 vide
        .group_by(CLI_ISFACT.Tel1, CLI_ISFACT.Tel2)
        .having(db.func.count().label('count') > 1)
        .all()
    )

    # Parcourir les doublons de Tel1 et Tel2 regroupés
    for tel1, tel2 in tqdm(clients_tel1_tel2, desc=" * Removing Tel1 and Tel2 duplicates", unit="Tel1 & Tel2"):
        try:
            # Récupérer tous les enregistrements avec les numéros de téléphone donnés
            doublon_entries = CLI_ISFACT.query.filter_by(Tel1=tel1, Tel2=tel2).all()
            
            # Ecrire dans la base SITE la référence du 1er enregistrement
            CodeClient_source = doublon_entries[0].CodeClient
            
            for entry in doublon_entries:
                mise_a_jour_site = SITE_ISAFACT.query.filter_by(CodeClient=entry.CodeClient).first()
                if mise_a_jour_site:
                    mise_a_jour_site.RefExterneISAFACT = CodeClient_source
                    SITE_Maj += 1 
                else:
                    print(' * Pas de code client ' + entry.CodeClient)
                
            if all(entry.FamilleTIERS == 'PARTICULIER pour le SAV' for entry in doublon_entries):
                premier_enregistrement = doublon_entries[0]

                for doublon in doublon_entries[1:]:
                    db.session.delete(doublon)
                    doublons_supprimes += 1

                db.session.commit()

        except NoResultFound:
            pass
    
    print(" *** " + str(doublons_supprimes) + ' doublons ont été supprimés')
    return doublons_supprimes, SITE_Maj     

def suppression_doublon_by_TEL1():
    doublon_supprime = 0
    SITE_Maj = 0
    doublons_supprimes = 0  # Déclarer ici pour éviter l'erreur UnboundLocalError
    clients_tel1 = (
        db.session.query(CLI_ISFACT.Tel1)
        .filter(CLI_ISFACT.FamilleTIERS == 'PARTICULIER pour le SAV')  # Filtrer par FamilleTIERS
        .filter(CLI_ISFACT.Tel1 != '')  # Exclure les enregistrements avec Tel1 vide
        .group_by(CLI_ISFACT.Tel1)
        .having(db.func.count(CLI_ISFACT.Tel1) > 1)
        .all()
    )
    # Parcourir les numéros de téléphone avec doublons
    for tel1, in tqdm(clients_tel1, desc=" * Removing Tel1 duplicates", unit="Tel1"):
        try:
            # Récupérer tous les enregistrements avec le numéro de téléphone donné
            doublon_entries = CLI_ISFACT.query.filter_by(Tel1=tel1).all()
            
            # Ecrire dans la base SITE la référence du 1er enregistrement
            CodeClient_source = doublon_entries[0].CodeClient
            
            for entry in doublon_entries:
                mise_a_jour_site = SITE_ISAFACT.query.filter_by(CodeClient=entry.CodeClient).first()
                if mise_a_jour_site:
                        mise_a_jour_site.RefExterneISAFACT = CodeClient_source
                        SITE_Maj += 1 
                else:
                        # Gérer le cas où aucune correspondance pour CodeClient n'est trouvée dans SITE_ISAFACT
                        # Peut-être imprimer un message d'erreur ou d'avertissement
                        print(" *** " + 'Pas de code client ' + entry.CodeClient)
                pass
                
            # Vérifier la condition pour supprimer les doublons
            if all(entry.FamilleTIERS == 'PARTICULIER pour le SAV' for entry in doublon_entries):
                # Conserver le premier enregistrement, supprimer les doublons
                premier_enregistrement = doublon_entries[0]

                for doublon in doublon_entries[1:]:
                    db.session.delete(doublon)
                    doublons_supprimes += 1

                db.session.commit()

        except NoResultFound:
            pass  # Aucun enregistrement avec Tel1 trouvé, ignorer
        
    print( " *** " +  str(doublons_supprimes) + ' doublons ont été supprimés')
    return doublons_supprimes, SITE_Maj

def suppression_doublon_by_TEL2():
    doublon_supprime = 0
    SITE_Maj = 0
    doublons_supprimes = 0  # Déclarer ici pour éviter l'erreur UnboundLocalError
    clients_tel2 = (
        db.session.query(CLI_ISFACT.Tel2)
        .filter(CLI_ISFACT.FamilleTIERS == 'PARTICULIER pour le SAV')  # Filtrer par FamilleTIERS
        .filter(CLI_ISFACT.Tel2 != '')  # Exclure les enregistrements avec Tel1 vide
        .group_by(CLI_ISFACT.Tel2)
        .having(db.func.count(CLI_ISFACT.Tel2) > 1)
        .all()
    )
    # Parcourir les numéros de téléphone avec doublons
    for tel2, in tqdm(clients_tel2, desc=" * Removing Tel2 duplicates", unit="Tel2"):
        try:
            # Récupérer tous les enregistrements avec le numéro de téléphone donné
            doublon_entries = CLI_ISFACT.query.filter_by(Tel2=tel2).all()
            
            # Ecrire dans la base SITE la référence du 1er enregistrement
            CodeClient_source = doublon_entries[0].CodeClient
            
            for entry in doublon_entries:
                mise_a_jour_site = SITE_ISAFACT.query.filter_by(CodeClient=entry.CodeClient).first()
                if mise_a_jour_site:
                        mise_a_jour_site.RefExterneISAFACT = CodeClient_source
                        SITE_Maj += 1 
                else:
                        # Gérer le cas où aucune correspondance pour CodeClient n'est trouvée dans SITE_ISAFACT
                        # Peut-être imprimer un message d'erreur ou d'avertissement
                        print(" *** " + 'Pas de code client ' + entry.CodeClient)
                pass
                
            # Vérifier la condition pour supprimer les doublons
            if all(entry.FamilleTIERS == 'PARTICULIER pour le SAV' for entry in doublon_entries):
                # Conserver le premier enregistrement, supprimer les doublons
                premier_enregistrement = doublon_entries[0]

                for doublon in doublon_entries[1:]:
                    db.session.delete(doublon)
                    doublons_supprimes += 1

                db.session.commit()

        except NoResultFound:
            pass  # Aucun enregistrement avec Tel1 trouvé, ignorer
    print(" *** " + str(doublons_supprimes) + ' doublons ont été supprimés')
    return doublons_supprimes, SITE_Maj

def suppression_doublon_by_EMAIL():
    doublon_supprime = 0
    SITE_Maj = 0
    doublons_supprimes = 0  # Déclarer ici pour éviter l'erreur UnboundLocalError
    clients_EMAIL = (
        db.session.query(CLI_ISFACT.EmailTIERS)
        .filter(CLI_ISFACT.FamilleTIERS == 'PARTICULIER pour le SAV')  # Filtrer par FamilleTIERS
        .filter(CLI_ISFACT.EmailTIERS != '')  # Exclure les enregistrements avec Tel1 vide
        .group_by(CLI_ISFACT.EmailTIERS)
        .having(db.func.count(CLI_ISFACT.EmailTIERS) > 1)
        .all()
    )
    # Parcourir les numéros de téléphone avec doublons
    for EmailTIERS, in tqdm(clients_EMAIL, desc=" * Removing Email duplicates", unit="Email"):
        try:
            # Récupérer tous les enregistrements avec le numéro de téléphone donné
            doublon_entries = CLI_ISFACT.query.filter_by(EmailTIERS=EmailTIERS).all()
            
            # Ecrire dans la base SITE la référence du 1er enregistrement
            CodeClient_source = doublon_entries[0].CodeClient
            
            for entry in doublon_entries:
                mise_a_jour_site = SITE_ISAFACT.query.filter_by(CodeClient=entry.CodeClient).first()
                if mise_a_jour_site:
                        mise_a_jour_site.RefExterneISAFACT = CodeClient_source
                        SITE_Maj += 1 
                else:
                        # Gérer le cas où aucune correspondance pour CodeClient n'est trouvée dans SITE_ISAFACT
                        # Peut-être imprimer un message d'erreur ou d'avertissement
                        print(" *** " + 'Pas de code client ' + entry.CodeClient)
                pass
                
            # Vérifier la condition pour supprimer les doublons
            if all(entry.FamilleTIERS == 'PARTICULIER pour le SAV' for entry in doublon_entries):
                # Conserver le premier enregistrement, supprimer les doublons
                premier_enregistrement = doublon_entries[0]

                for doublon in doublon_entries[1:]:
                    db.session.delete(doublon)
                    doublons_supprimes += 1

                db.session.commit()

        except NoResultFound:
            pass  # Aucun enregistrement avec Tel1 trouvé, ignorer
    print( " *** " + str(doublons_supprimes) + ' doublons ont été supprimés')
    return doublons_supprimes, SITE_Maj