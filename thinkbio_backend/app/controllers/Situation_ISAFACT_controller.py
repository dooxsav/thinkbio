from app import db
from app.services import lire_BD_SITUATION_ISAFACT_ByCodeClient

def lire_historique_client_par_CodeClient(codeclient):
    return lire_BD_SITUATION_ISAFACT_ByCodeClient(codeclient)