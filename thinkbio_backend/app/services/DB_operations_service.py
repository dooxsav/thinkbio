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
from app.models import Geography, Client_ISAFACT, Client_DIVALTO, CLI_ISFACT
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
            
    db.session.commit()
    ligne_supprimé = supprimer_doublons_tel1()
    exporter_cli_isfact_excel()

    # Afficher le nombre de lignes ajoutées et modifiées
    return jsonify({
        "message": f"Migration effectuée avec succès. {lignes_ajoutees} lignes ont été ajoutées, {lignes_modifiees} lignes ont été mises à jour. {ligne_supprimé} ont été supprimés"
    })

def supprimer_doublons_tel1():
    doublons_supprimes = 0

    clients_tel1 = (
        db.session.query(CLI_ISFACT.Tel1)
        .group_by(CLI_ISFACT.Tel1)
        .having(db.func.count(CLI_ISFACT.Tel1) > 1)
        .all()
    )

    for tel1, in tqdm(clients_tel1, desc="Processing Tel1 duplicates", unit="Tel1"):
        try:
            doublon_entries = CLI_ISFACT.query.filter_by(Tel1=tel1).all()

            # Conserver le premier enregistrement, supprimer les doublons
            premier_enregistrement = doublon_entries[0]

            for doublon in doublon_entries[1:]:
                db.session.delete(doublon)
                doublons_supprimes += 1

            db.session.commit()

        except NoResultFound:
            pass  # Aucun enregistrement avec Tel1 trouvé, ignorer

    return doublons_supprimes