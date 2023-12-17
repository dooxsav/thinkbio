from app import db
from app.services import lire_BD_RESSOURCE_MATERIEL_DIVALTO

def lire_donnes_ressources_materiel():
    result = lire_BD_RESSOURCE_MATERIEL_DIVALTO()
    return result
    