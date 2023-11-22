# services/DB_site.py
#

from app import db
from app.models import Client_ISAFACT, CLI_ISFACT, SITE_ISAFACT
from tqdm import tqdm
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound

def Transfert_donnes_CLIENT_ISAFACT_CLI():
    print('Ecriture de la base CLI...')
    Donnes_depuis_CLIENT_ISAFACT = Client_ISAFACT.query.all()
    lignes_ajoutées = 0
    lignes_modifiées = 0
    
    for client in tqdm(Donnes_depuis_CLIENT_ISAFACT, desc='Processing CLI from ISAFACT', unit="CLI/s"):
        # Utilisation de sorted au lieu de sort pour obtenir une nouvelle liste triée
        num_tel = sorted([client.TelFACT1, client.TelFACT2, client.TelFACT3], reverse=True)
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
                createdAt=datetime.now(),
                createdBy='CREATOR',
                updatedAt=datetime.now(),
                lastUpdatedBy='CREATOR'
            )
            db.session.add(new_CLI_entry)
            lignes_ajoutées += 1

    db.session.commit()
    return lignes_ajoutées, lignes_modifiées

def suppression_doublon_by_TEL1():
    doublon_supprime = 0
    SITE_Maj = 0
    doublons_supprimes = 0  # Déclarer ici pour éviter l'erreur UnboundLocalError
    clients_tel1 = (
        db.session.query(CLI_ISFACT.Tel1)
        .group_by(CLI_ISFACT.Tel1)
        .having(db.func.count(CLI_ISFACT.Tel1) > 1)
        .all()
    )
    # Parcourir les numéros de téléphone avec doublons
    for tel1, in tqdm(clients_tel1, desc="Removing Tel1 duplicates", unit="Tel1"):
        try:
            # Récupérer tous les enregistrements avec le numéro de téléphone donné
            doublon_entries = CLI_ISFACT.query.filter_by(Tel1=tel1).all()
            
            # Ecrire dans la base SITE la référence du 1er enregistrement
            CodeClient_source = doublon_entries[0].CodeClient
            
            for entry in doublon_entries:
                mise_a_jour_site = SITE_ISAFACT.query.filter_by(CodeClient=entry.CodeClient).first()
                mise_a_jour_site.CodeClient = CodeClient_source
                SITE_Maj += 1 
                
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

    return doublons_supprimes, SITE_Maj