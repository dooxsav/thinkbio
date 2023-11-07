# routes/client_ISAFACT.py

from flask import Blueprint, request, jsonify
from app.controllers import importISAFACTDataFromExcel

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
    
    return importISAFACTDataFromExcel(), 200
