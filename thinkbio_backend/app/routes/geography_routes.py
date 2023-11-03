# routes/geography_routes.py

from flask import Blueprint, request, jsonify
from app.controllers import HelloGeography, PopulateDB_geography

Geography_bp = Blueprint('Geography', __name__)

@Geography_bp.route('/geography/testroutes', methods = ['GET'])
def TestRoute():
    return 'Router Route work!'

@Geography_bp.route('/geography/populateDB', methods = ['POST'])
def populateDB():
    # Attribution du fichier
    file = request.files.get('file') # Nom du fichier
    
    # Vérification présence d'un fichier
    if not (file and file.filename and file.filename.endswith('.xlsx')):
        return jsonify({"error": "Fichier incorrect dans la requête"}), 400 # Bad Request
    
    result = PopulateDB_geography(file)
    
    return result