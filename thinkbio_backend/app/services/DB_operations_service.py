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
from flask import jsonify
from datetime import datetime
from tqdm import tqdm

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
    clientsRAW = Client_ISAFACT.query.all()
    
    for client in clientsRAW:
        TelRAW = [clientsRAW['TelFACT1'], clientsRAW['TelFACT2'], clientsRAW['TelFACT3']]
        TelRAW.sort()
    
    
    db.session.commit()

    # Afficher le nombre de lignes ajoutées et modifiées
    return jsonify({
        "message": f"Fichier importé avec succès dans la base de données. {lignes_ajoutees} lignes ont été ajoutées, {lignes_modifiees} lignes ont été mises à jour."
    })
    

        