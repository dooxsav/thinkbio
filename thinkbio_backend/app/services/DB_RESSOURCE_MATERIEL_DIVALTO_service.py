from app import db
from app.models import RESSOURCE_MATERIEL_DIVALTO

def lire_BD_RESSOURCE_MATERIEL_DIVALTO():
    materiels = RESSOURCE_MATERIEL_DIVALTO.query.all()
    return [materiel.to_dict() for materiel in materiels]  # Convertir les objets en dictionnaires

def ecrire_BD_RESSOURCE_MATERIEL_DIVALTO():
    
    return 'toto'