from flask import Blueprint
from app.controllers import lire_donnes_table_geolocation

Geolocation_bp = Blueprint('Geolocation', __name__)

@Geolocation_bp.route('/geolocation/allsite', methods=['GET'])
def lire_table_geolocation_site():
    return lire_donnes_table_geolocation()