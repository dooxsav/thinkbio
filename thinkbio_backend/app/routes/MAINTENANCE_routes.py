from flask import Blueprint
from app.controllers import *

# Création du Blueprint 'MaintenanceDB_bp'
MaintenanceDB_bp = Blueprint('MaintenanceDB_bp', __name__)

# Définition des routes pour ce BP :
@MaintenanceDB_bp.route('/MaintenanceDB/hello', methods=['GET'])
def hello():
    return 'test'

@MaintenanceDB_bp.route('/MaintenanceDB/etatBD', methods=['GET'])
def CountRecordInTable():
    return lire_nbre_enregistrement_par_table()