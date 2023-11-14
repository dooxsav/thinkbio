# routes/client_DIVALTO_routes.py
#
# Gestion des routes liées à DIVALTO
#
#

from flask import Blueprint, jsonify, request
from datetime import datetime
import os
from app.controllers import importDIVALTODataFromExcel, lireBDDDIVALTO

Client_DIVALTO_bp = Blueprint('Client_DIVALTO', __name__)

@Client_DIVALTO_bp.route('/clientDIVALTO/testroutesdivalto', methods=['GET'])
def HelloDivalto():
    result = 'Routes DIVALTO fonctionnels'
    return jsonify({'message': result})

@Client_DIVALTO_bp.route('/clientDIVALTO/populateDB', methods = ['POST'])
def PopulateDBDIVALTOfromExcelFile():
    # attribution du fichier
    file = request.files.get('file') # le fichier devra s'appeler file !
    
    # Vérification présence d'un fichier
    if not (file and file.filename and file.filename.endswith('.xlsx')):
        return jsonify({"error": "Fichier incorrect dans la requête"}), 400 # Bad Request
    
    result = importDIVALTODataFromExcel(file)
    
    return result

@Client_DIVALTO_bp.route('/clientDIVALTO/lireclients', methods=['GET'])
def lireClientDIVALTo():
    result = lireBDDDIVALTO()
    return result