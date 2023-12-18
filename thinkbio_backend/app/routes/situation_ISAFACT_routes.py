from flask import Blueprint, jsonify, request
from app.controllers import lire_historique_client_par_CodeClient

# Création du Blueprint 'OperationDB_bp'
Situation_bp = Blueprint('Situation_bp', __name__)

@Situation_bp.route('/situation/', methods=['GET'])
def situation_by_client():
    codeclient = request.args.get('codeclient')
    # Utilisation du paramètre codeclient dans la logique de votre fonction
    result = lire_historique_client_par_CodeClient(codeclient)
    return result