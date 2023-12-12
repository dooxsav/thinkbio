# services/DB_operation_sevices
#
# Ce service est responsable des opérations sur les tables ISFACT et DIVALTO
#
#
#
#
#
#
#

from app import db
from app.models import Geography, Client_ISAFACT, CLI_ISFACT, SITE_ISAFACT, RIB_ISAFACT, SITE_GEOCODAGE
from app.services import exporter_cli_isfact_excel
from flask import jsonify
from datetime import datetime
from tqdm import tqdm
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_
import os
import signal
import psutil


def KillAllTable():
    try:
        print('\033[91m *** PURGE DES BASES DE DONNEES ***\033[0m"')
        db.reflect()

        # Sauvegarder les données de la table que vous souhaitez conserver
        # Supposons que la table à conserver s'appelle 'table_to_keep'
        table_to_keep_data = SITE_GEOCODAGE.query.all()

        # Supprimer toutes les tables sauf celle que vous souhaitez conserver
        db.drop_all()
        print(" *** Toutes les tables ont été supprimées avec succès sauf la table '{}' ***".format(SITE_GEOCODAGE.__tablename__))

        # Recréer les tables
        db.create_all()
        print(" *** La base de données a été reconstruite avec succès. ***")

        # Restaurer les données dans la table conservée
        for row in table_to_keep_data:
            db.session.add(row)
        db.session.commit()
        print(" *** Données restaurées dans la table '{}' avec succès. ***".format(SITE_GEOCODAGE.__tablename__))
        
        return "Job Done"

    except Exception as e:
        return f"Une erreur s'est produite : {e}", 400
    
    
def lire_donnees_CLI_ISAFACT():
    clients = CLI_ISFACT.query.all()  # Récupérer tous les clients depuis la base de données
    clients_json = [client.to_dict() for client in clients]  # Convertir les objets clients en dictionnaires

    return jsonify(clients_json)  # Retourner les données au format JSON

def lire_donnes_SITE_ISFACT():
    sites = SITE_ISAFACT.query.all()  # Récupérer tous les clients depuis la base de données
    sites_json = [site.to_dict() for site in sites]  # Convertir les objets clients en dictionnaires

    return jsonify(sites_json)  # Retourner les données au format JSON

def lire_donnes_RIB_ISFACT ():
    RIBs = RIB_ISAFACT.query.all()  # Récupérer tous les RIBs depuis la base de données
    RIBs_list = [rib.to_dict() for rib in RIBs]  # Convertir les objets RIBs en dictionnaires

    return jsonify(RIBs_list)  # Retourner les données au format JSON



def MaJ_Table_CLI_BY_ISAFACT():

    lignes_ajoutees = 0
    lignes_modifiees = 0
    ligne_supprimé = 0
    Compteur_Client = 0
    
    clientsRAW = Client_ISAFACT.query.all()

    # Créer une barre de progression pour itérer sur les clients
    for client in tqdm(clientsRAW, desc="Processing clients", unit="client"):
        TelRAW = [client.TelFACT1, client.TelFACT2, client.TelFACT3]
        TelRAW.sort(reverse=True)

        try:
            # MaJ
            cli_isafact_entry = CLI_ISFACT.query.filter_by(CodeClient=client.CodeClient).one()
            cli_isafact_entry.FamilleTIERS = client.FamilleTIERS
            cli_isafact_entry.NomFACT = client.NomFACT
            cli_isafact_entry.PrenomFACT = client.PrenomFACT
            cli_isafact_entry.AdresseFACT = client.AdresseFACT
            cli_isafact_entry.CPFACT = client.CPFACT
            cli_isafact_entry.VilleFACT = client.VilleFACT
            cli_isafact_entry.PaysFACT = client.PaysFACT
            cli_isafact_entry.EmailTIERS = client.EmailTIERS
            cli_isafact_entry.Tel1 = TelRAW[0]
            cli_isafact_entry.Tel2 = TelRAW[1]
            cli_isafact_entry.updatedAt = datetime.now()
            cli_isafact_entry.lastUpdatedBy = 'USER'
            lignes_modifiees += 1
        except NoResultFound:
            # Création
            new_entry = CLI_ISFACT(
                CodeClient=client.CodeClient,
                Client_id=f'C{Compteur_Client:010d}',
                FamilleTIERS=client.FamilleTIERS,
                NomFACT=client.NomFACT,
                PrenomFACT=client.PrenomFACT,
                AdresseFACT=client.AdresseFACT,
                CPFACT=client.CPFACT,
                VilleFACT=client.VilleFACT,
                PaysFACT=client.PaysFACT,
                EmailTIERS=client.EmailTIERS,
                Tel1=TelRAW[0],
                Tel2=TelRAW[1],
                Tel3=None,
                createdAt=datetime.now(),
                createdBy='USER',
                updatedAt=datetime.now(),
                lastUpdatedBy='USER'
            )
            db.session.add(new_entry)
            lignes_ajoutees += 1
            Compteur_Client+=1
            
    db.session.commit()
    ligne_supprimé = supprimer_doublons_tel1() 
    ligne_supprimé = supprimer_doublons_tel2() 
    ligne_supprimé += supprimer_doublons_courriel()
    # ligne_supprimé += supprimer_doublons_IBAN() --A faire !
    mettre_a_jour_compteur_cli()
    MaJ_table_STATION_BY_ISAFACT()
    exporter_cli_isfact_excel()

    # Afficher le nombre de lignes ajoutées et modifiées
    return jsonify({
        "message": f"Migration effectuée avec succès. {lignes_ajoutees} lignes ont été ajoutées, {lignes_modifiees} lignes ont été mises à jour. {ligne_supprimé} ont été supprimés"
    })

def MaJ_table_STATION_BY_ISAFACT():
    # Initialisation des compteurs
    lignes_ajoutees = 0
    lignes_modifiees = 0
    ligne_supprimee = 0
    Compteur_Client = 0

    # récupération des données dans la base brut. Les données sont filtrées par la famille pour n'impacter que les particuliers
    clientsRAW = Client_ISAFACT.query.filter_by(FamilleTIERS='PARTICULIER pour le SAV').all()
    
    # Créer une barre de progression pour itérer sur les clients
    for station in tqdm(clientsRAW, desc="Processing STATION", unit="client"):

        try:
            # MaJ des données dans SITE_ISAFACT
            site_entry = SITE_ISAFACT.query.filter_by(CodeClient=station.CodeClient).one()
            site_entry.AdresseSite = station.AdresseSITE
            site_entry.VilleSite = station.VilleSITE
            site_entry.CPSite = station.CPSITE
            site_entry.UpdatedAt = datetime.now()
            site_entry.LastUpdatedBy = 'USER'

            lignes_modifiees += 1
        except NoResultFound:
            # Création d'une nouvelle entrée dans SITE_ISAFACT
            new_entry = SITE_ISAFACT(
                CodeClient=station.CodeClient,
                FamilleTIERS=station.FamilleTIERS,
                AdresseSite=station.AdresseSITE,
                VilleSite=station.VilleSITE,
                CPSite=station.CPSITE,
                CreatedAt=datetime.now(),
                CreatedBy='USER',
                UpdatedAt=datetime.now(),
                LastUpdatedBy='USER',
            )
            db.session.add(new_entry)
            lignes_ajoutees += 1
            Compteur_Client += 1
     
    db.session.commit()
    
    # Attribution du numéro de site
    print('Attribution du numéro de site...')
    attribuer_numero_site()
    
    # Correlation numéro site, numéro client
    print('Correspondance entre les sites et la clients...')
    correspondance_non_trouve = attribuer_correspondance_site_client()
    
    print('Attribution des RIB/client')
    RIB = MaJ_Table_RIB_BY_ISFACT()
    
    # Afficher le nombre de lignes ajoutées et modifiées
    return jsonify({
        "message": f"Migration effectuée avec succès. {lignes_ajoutees} ligne(s) ont été ajoutées, {lignes_modifiees} ligne(s) ont été mise(s) à jour. {ligne_supprimee} ont été supprimée(s). {correspondance_non_trouve} stations sont non attribuées. Sur table RIB : {RIB}"
    })
   
def MaJ_Table_RIB_BY_ISFACT():
    ligne_ajoute = 0
    ligne_modifie = 0
    
    clients = CLI_ISFACT.query.all()
    
    for client in tqdm(clients, desc="Correspondance client/IBAN", unit="client"):
        
        codeClient = client.CodeClient
        existence_RIB = Client_ISAFACT.query.filter(Client_ISAFACT.RIB_IBAN != '', Client_ISAFACT.CodeClient == codeClient).first()
        
        if existence_RIB:
            try:
                # Mise à jour
                RIB_entry = RIB_ISAFACT.query.filter_by(CodeClient=codeClient).first()
                if RIB_entry:
                    RIB_entry.IBANPAYS = existence_RIB.RIB_IBAN[:2]
                    RIB_entry.IBANCLE = existence_RIB.RIB_Cle
                    RIB_entry.IBANCOMPTE = existence_RIB.RIB_IBAN[4:4+23]
                    RIB_entry.RIBBIC = existence_RIB.RIB_CodeBIC
                    RIB_entry.RIBDO = existence_RIB.RIB_Domic

                    ligne_modifie += 1
                else:
                    raise NoResultFound  # Lever l'exception pour créer une nouvelle entrée
                
            except NoResultFound:
                # Nouvelle entrée
                new_entry = RIB_ISAFACT(
                    Client_id=client.Client_id,
                    CodeClient=client.CodeClient,
                    FamilleTIERS=client.FamilleTIERS,
                    IBANPAYS=existence_RIB.RIB_IBAN[:2],
                    IBANCLE=existence_RIB.RIB_Cle,
                    IBANCOMPTE=existence_RIB.RIB_IBAN[4:4+23],
                    RIBBIC=existence_RIB.RIB_CodeBIC,
                    RIBDO=existence_RIB.RIB_Domic
                )
                db.session.add(new_entry)
                ligne_ajoute += 1
    
    db.session.commit()
    
    return {'message': f'Données importées avec succès. {ligne_ajoute} ligne(s) ont été ajoutée(s), {ligne_modifie} ligne(s) ont été modifiée(s)'}

    
def attribuer_correspondance_site_client():
    sites = SITE_ISAFACT.query.all()
    no_match = 0
    for site in tqdm(sites, desc="Correspondance sites/clients", unit="enregistrements"):
        equiv_cli = CLI_ISFACT.query.filter_by(CodeClient=site.CodeClient).first()
        
        if equiv_cli:
            # Correspondance directe
            site.Client_id = equiv_cli.Client_id
        else:
            client_BD_ISAFACT = Client_ISAFACT.query.filter_by(CodeClient=site.CodeClient).first()

            client_BD_CLI = CLI_ISFACT.query.filter_by(Tel1=client_BD_ISAFACT.TelFACT2).first() or \
                                CLI_ISFACT.query.filter_by(Tel2=client_BD_ISAFACT.TelFACT2).first() or None
            if client_BD_CLI and not client_BD_CLI.Client_id:    
                client_BD_CLI = CLI_ISFACT.query.filter_by(Tel1=client_BD_ISAFACT.TelFACT1).first() or \
                                    CLI_ISFACT.query.filter_by(Tel2=client_BD_ISAFACT.TelFACT1)
                if client_BD_CLI and not client_BD_CLI.Client_id:
                    client_BD_CLI = CLI_ISFACT.query.filter_by(Tel1=client_BD_ISAFACT.TelFACT3).first() or \
                                        CLI_ISFACT.query.filter_by(Tel2=client_BD_ISAFACT.TelFACT3).first() or None 
     
                    if client_BD_CLI and not client_BD_CLI.Client_id:
                        client_BD_CLI = CLI_ISFACT.query.filter_by(EmailTIERS=client_BD_ISAFACT.EmailTIERS).first()


            if client_BD_CLI:
                site.Client_id = client_BD_CLI.Client_id
            else:
                no_match += 1
                print('No Match found for ' + site.CodeClient)


        db.session.add(site)
    print(str(no_match) + " station sans affectation")
    db.session.commit()

    return None



def supprimer_doublons_tel1():
    doublons_supprimes = 0
    # Récupérer les numéros de téléphone avec des doublons
    clients_tel1 = (
        db.session.query(CLI_ISFACT.Tel1)
        .group_by(CLI_ISFACT.Tel1)
        .having(db.func.count(CLI_ISFACT.Tel1) > 1)
        .all()
    )

    # Parcourir les numéros de téléphone avec doublons
    for tel1, in tqdm(clients_tel1, desc="Processing Tel1 duplicates", unit="Tel1"):
        try:
            # Récupérer tous les enregistrements avec le numéro de téléphone donné
            doublon_entries = CLI_ISFACT.query.filter_by(Tel1=tel1).all()

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

    return doublons_supprimes

def supprimer_doublons_tel2():
    doublons_supprimes = 0
    # Récupérer les numéros de téléphone avec des doublons
    clients_tel2 = (
        db.session.query(CLI_ISFACT.Tel2)
        .group_by(CLI_ISFACT.Tel2)
        .having(db.func.count(CLI_ISFACT.Tel2) > 1)
        .all()
    )

    # Parcourir les numéros de téléphone avec doublons
    for tel2, in tqdm(clients_tel2, desc="Processing Tel2 duplicates", unit="Tel"):
        try:
            # Récupérer tous les enregistrements avec le numéro de téléphone donné
            doublon_entries = CLI_ISFACT.query.filter_by(Tel1=tel2).all()

            # Vérifier la condition pour supprimer les doublons
            if doublon_entries and all(entry.FamilleTIERS == 'PARTICULIER pour le SAV' for entry in doublon_entries):
                # Conserver le premier enregistrement, supprimer les doublons
                premier_enregistrement = doublon_entries[0]

                for doublon in doublon_entries[1:]:
                    db.session.delete(doublon)
                    doublons_supprimes += 1

                db.session.commit()

        except NoResultFound:
            pass  # Aucun enregistrement avec Tel2 trouvé, ignorer

    return doublons_supprimes

def supprimer_doublons_courriel():
    doublons_supprimes = 0
    # Récupérer les numéros de téléphone avec des doublons
    clients_courriel = (
        db.session.query(CLI_ISFACT.EmailTIERS)
        .group_by(CLI_ISFACT.EmailTIERS)
        .having(db.func.count(CLI_ISFACT.EmailTIERS) > 1)
        .all()
    )

    # Parcourir les numéros de téléphone avec doublons
    for EmailTIERS, in tqdm(clients_courriel, desc="Processing EmailTIERS duplicates", unit="Tel1"):
        try:
            # Récupérer tous les enregistrements avec le numéro de téléphone donné
            doublon_entries = CLI_ISFACT.query.filter_by(EmailTIERS=EmailTIERS).all()

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

    return doublons_supprimes


def mettre_a_jour_compteur_cli():
    compteur_client = 1
    clients = db.session.query(CLI_ISFACT).all()

    # Utilisation de tqdm pour la barre de progression
    for client in tqdm(clients, desc="Numérotation des clients", unit="client"):
        client.Client_id = f'C{compteur_client:010d}'
        compteur_client += 1
    
    db.session.commit()

def attribuer_numero_site():
    compteur_site = 0
    sites = db.session.query(SITE_ISAFACT).all()
    
    # Utilisation de TQDM pour la barre de progression
    for site in tqdm(sites, desc="Numérotation des sites", unit="site"):
        site.Site_id = f'S{compteur_site:010d}'
        compteur_site +=1
        
    db.session.commit()
    
