from flask import Blueprint
from app.controllers import lire_donnes_table_geolocation, lire_donnes_contrat_et_site

Geolocation_bp = Blueprint('Geolocation', __name__)

@Geolocation_bp.route('/geolocation/allsite', methods=['GET'])
def lire_table_geolocation_site():
    return lire_donnes_table_geolocation()

@Geolocation_bp.route('/geolocation/sitecontrats', methods=['GET'])
def lire_contrat_geocodage():
    return lire_donnes_contrat_et_site()