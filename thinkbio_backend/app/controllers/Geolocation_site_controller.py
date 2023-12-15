from app.services import *

def lire_donnes_table_geolocation():
    result = lire_base_site_geocodage()
    return result

def lire_donnes_contrat_et_site():
    result = lire_base_site_geocodage_avec_contrats()
    return result