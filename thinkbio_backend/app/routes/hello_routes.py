# hello_routes.py

from flask import Blueprint

# Création du Blueprint 'hello_bp'
hello_bp = Blueprint('hello', __name__)

# Définition des routes pour ce BP :
@hello_bp.route('/hello')
def hello():
    return "Hello, toto"