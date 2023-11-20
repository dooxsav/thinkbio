from flask import Blueprint
from app.controllers import HelloOperationDB, KillSwitch

# Création du Blueprint 'OperationDB_bp'
OperationDB_bp = Blueprint('OperationDB_bp', __name__)

# Définition des routes pour ce BP :
@OperationDB_bp.route('/OperationDB/hello', methods=['GET'])
def hello():
    return 'test'

@OperationDB_bp.route('/OperationDB/MaJdivaltotable', methods=['GET'])
def MAJ_TableDivalto_données_ISFACT():
    return None

@OperationDB_bp.route('/OperationDB/etatdesdifference', methods=['GET'])
def EtatDesDifferenceISAFACTDIVALTO():
    return None

@OperationDB_bp.route('/OperationDB/killswitch', methods = ['GET'])
def KillSwitch_route():
    # kill toutes la base de données
    return KillSwitch()