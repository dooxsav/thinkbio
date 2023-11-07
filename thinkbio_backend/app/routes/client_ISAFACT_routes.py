# routes/client_ISAFACT.py

from flask import Blueprint

Client_ISAFACT_bp = Blueprint('Client_ISAFACT', __name__)

@Client_ISAFACT_bp.route('/clientISAFACT/test', methods=['GET'])
def HelloClientISAFACT():
    return 'Hello, from ClientISAFACT'
