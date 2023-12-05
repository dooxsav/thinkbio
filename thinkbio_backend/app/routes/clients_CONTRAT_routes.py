# Routes/clients_contrats

from flask import Blueprint, jsonify, request
from app.controllers import populate_DB_Client, lireBaseCLient, lireBaseCLientContrat

ClientContrat_bp = Blueprint('clientscontrat', __name__)

@ClientContrat_bp.route('/clientcontrat')
def test():
    return jsonify({"message": "Job Done"})

@ClientContrat_bp.route('/clientcontrat/lireall', methods=['GET'])
def lire_contrats():
    return lireBaseCLientContrat()