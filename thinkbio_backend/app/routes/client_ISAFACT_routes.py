# routes/client_ISAFACT.py

from flask import Blueprint, request, jsonify
from app.controllers import importISAFACTDataFromExcel,lireDonnesClientISAFACT, extraire_CLI_from_DATA_brut_ISFACT, lire_BD_CLI_ISFACT, lire_Table_RIB_ISAFACT, lire_Table_RIB_ISAFACT, dosomeMagical

Client_ISAFACT_bp = Blueprint('Client_ISAFACT', __name__)

@Client_ISAFACT_bp.route('/clientISAFACT/test', methods=['GET'])
def HelloClientISAFACT():
    return 'Hello, from ClientISAFACT'

@Client_ISAFACT_bp.route('/clientISAFACT/populateDB', methods = ['POST'])
def GetISAFACTDataFromExcelFile():
    # attribution du fichier
    file = request.files.get('file') # le fichier devra s'appeler file !
    
    # Vérification présence d'un fichier
    if not (file and file.filename and file.filename.endswith('.xlsx')):
        return jsonify({"error": "Fichier incorrect dans la requête"}), 400 # Bad Request
    
    result = importISAFACTDataFromExcel(file)
    
    return result

@Client_ISAFACT_bp.route('/clientISAFACT/lireclients', methods=['GET'])
def lireclientBDDISFACT():
    return lireDonnesClientISAFACT()

@Client_ISAFACT_bp.route('/clientISAFACT/MaJCLIISFACT', methods=['GET'])
def MaJ_CLI_CLIISAFACT():
    return extraire_CLI_from_DATA_brut_ISFACT()

@Client_ISAFACT_bp.route('/clientISAFACT/lire_CLI_by_ISFACT', methods=['GET'])
def lire_CLI_ISFACT():
    return lire_BD_CLI_ISFACT()

@Client_ISAFACT_bp.route('/clientISAFACT/lire_SITE_by_ISFACT', methods=['GET'])
def lire_SITE_ISFACT():
    return lire_Table_RIB_ISAFACT()

@Client_ISAFACT_bp.route('/clientISAFACT/lire_RIB_by_ISFACT', methods=['GET'])
def lire_RIB_ISAFACT():
    return lire_Table_RIB_ISAFACT()

@Client_ISAFACT_bp.route('/clientISAFACT/DoSomeMagical', methods=['POST'])
def MagicalRoad():
        # attribution du fichier
    file = request.files.get('file') # le fichier devra s'appeler file !
    
    # Vérification présence d'un fichier
    if not (file and file.filename and file.filename.endswith('.xlsx')):
        return jsonify({"error": "Fichier incorrect dans la requête"}), 400 # Bad Request
    
    result = dosomeMagical(file)
    
    return result
