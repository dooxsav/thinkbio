# routes/client_DIVALTO_routes.py
#
#
#
#

from flask import Blueprint, jsonify

Client_DIVALTO_bp = Blueprint('Client_DIVALTO', __name__)

@Client_DIVALTO_bp.route('/clientDIVALTO/testroutesdivalto', methods=['GET'])
def HelloDivalto():
    result = 'Routes DIVALTO fonctionnels'
    return jsonify({'message': result})

