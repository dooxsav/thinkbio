# Routes/clients

from flask import Blueprint, jsonify, request
from app.controllers import populate_DB_Client, lireBaseCLient

Client_bp = Blueprint('clients', __name__)

@Client_bp.route('/client')
def test():
    return jsonify({"message": "Job Done"})

@Client_bp.route('/client/populateDB', methods=['POST'])
def PopulateDB():
    
    # attribution du fichier
    file = request.files.get('file') # le fichier devra s'appeler file !
    
    # Vérification présence d'un fichier
    if not (file and file.filename and file.filename.endswith('.csv')):
        return jsonify({"error": "Fichier incorrect dans la requête"}), 400 # Bad Request
    result = populate_DB_Client(file)
    
    return result, 200

@Client_bp.route('/client/lireclients', methods=['GET'])
def lireDonnesClient():
    result = lireBaseCLient()
    return result