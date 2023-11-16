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
from app.models import Geography, Client_ISAFACT, Client_DIVALTO, CLI_ISFACT, SITE_ISAFACT
from app.services import exporter_cli_isfact_excel
from flask import jsonify
from datetime import datetime
from tqdm import tqdm
from sqlalchemy.orm.exc import NoResultFound

def Etat_des_lieux_difference_ISAFACT_DIVALTO():
    # récupération de tous les n° de client ISAFACT
    clients_isafact = Client_ISAFACT.query.all()
    nbre_client_isafact = len(clients_isafact)
    
    return nbre_client_isafact


def MaJ_Table_DIVALTO_Par_ISAFACT():
    # récupération de tous les n° de client ISAFACT
    clients_isafact = Client_ISAFACT.query.all()
    
    for client_ISAFACT in clients_isafact:
        # recherche des enregistrement correspondant dans la table DIVALTO
        client_divalto = Client_DIVALTO.query.filter_by(TIERSEXTERNE=client_ISAFACT)
    
    return 'Mise à jour !'


def lire_donnees_CLI_ISAFACT():
    clients = CLI_ISFACT.query.all()  # Récupérer tous les clients depuis la base de données
    clients_json = [client.to_dict() for client in clients]  # Convertir les objets clients en dictionnaires

    return jsonify(clients_json)  # Retourner les données au format JSON

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
            cli_isafact_entry.Tel2 = TelRAW[-1]
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
                Tel2=TelRAW[-1],
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
    ligne_supprimé += supprimer_doublons_courriel()
    exporter_cli_isfact_excel()
    mettre_a_jour_compteur_cli()

    # Afficher le nombre de lignes ajoutées et modifiées
    return jsonify({
        "message": f"Migration effectuée avec succès. {lignes_ajoutees} lignes ont été ajoutées, {lignes_modifiees} lignes ont été mises à jour. {ligne_supprimé} ont été supprimés"
    })


def MaJ_table_STATION_BY_ISAFACT():
    # Initialisation des compteurs
    lignes_ajoutees = 0
    lignes_modifiees = 0
    ligne_supprimé = 0
    Compteur_Station = 0
    
    # récupération des données dans la base brut. Les données sont filtrées par la famille pour n'impacter que les particuliers
    clientsRAW = Client_ISAFACT.query.filter_by(FamilleTIERS='PARTICULIER pour le SAV')
    
    # Créer une barre de progression pour itérer sur les clients
    for station in tqdm(clientsRAW, desc="Processing STATION", unit="client"):
        try:
            # MaJ des données
            cli_isafact_entry = SITE_ISAFACT.query.filter_by(CodeClient=station.CodeClient).one()
            cli_isafact_entry.AdresseSite = station.AdresseSite
            cli_isafact_entry.VilleSite = station.VilleSite
            cli_isafact_entry.CPSite = station.CPSite
            cli_isafact_entry.updatedAt = datetime.now(),
            cli_isafact_entry.lastUpdatedBy = 'USER'

            lignes_modifiees += 1
        except NoResultFound:
            # Création de l'entrée dans la table 
            new_entry = SITE_ISAFACT(
                CodeClient = station.CodeClient,
                FamilleTIERS = station.FamilleTIERS,
                AdresseSite = station.AdresseSite,
                VilleSite = station.VilleSite,
                CPSite = station.CPSite,
                createdAt = datetime.now(),
                createdBy ='USER',
                updatedAt = datetime.now(),
                lastUpdatedBy ='USER'
            )
            db.session.add(new_entry)
            lignes_ajoutees += 1
            Compteur_Client+=1
    
        db.session.commit()
    
    # Attribution du numéro de site
    attribuer_numero_site()
    
    # Correlation numéro site, numéro client
    
    # Afficher le nombre de lignes ajoutées et modifiées
    return jsonify({
        "message": f"Migration effectuée avec succès. {lignes_ajoutees} lignes ont été ajoutées, {lignes_modifiees} lignes ont été mises à jour. {ligne_supprimé} ont été supprimés"
    })
    

    


def attribuer_correspondance_site_client():
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
        site.Site_id = f'{compteur_site:01d}'
        compteur_site +=1
        
    db.session.commit()