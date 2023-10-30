# GRC_Route.py
from flask import Blueprint, jsonify, request
from app.controllers import toto

GRC_bp = Blueprint('GRC', __name__)

@GRC_bp.route("/GRC")
def GRC_test():
    return jsonify({"message": "GRC route is OK"}), 200

@GRC_bp.route("/GRC/test")
def GRC_test_route():
    return jsonify({"message": "GRC test route is OK"}), 200

@GRC_bp.route('/GRC/extraire_information_PDF', methods=['POST'])
def GRC_extraire_information():
    if request.method == 'POST':
        # attribution du fichier
        file = request.files.get('file') # le fichier devra s'appeler file !
        # Vérification présence d'un fichier
        if not (file and file.filename and file.filename.endswith('.pdf')):
            return jsonify({"error": "Fichier incorrect dans la requête"}), 400 # Bad Request
        
        
        return toto(), 200
    else:
        return jsonify({"error": "Méthode non autorisée"}), 405 # Not Allowed
    return toto()

