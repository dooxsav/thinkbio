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
from app.models import Geography, Client_ISAFACT, Client_DIVALTO

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