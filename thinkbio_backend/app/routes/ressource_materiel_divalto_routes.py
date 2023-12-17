from flask import Blueprint
from app.controllers import lire_donnes_ressources_materiel

# Création du Blueprint 'OperationDB_bp'
RessourcesMaterielDivalto_bp = Blueprint('RessourcesMaterielDivalto_bp', __name__)

@RessourcesMaterielDivalto_bp.route('/RessourcesMaterielDivalto/allmateriels', methods=['GET'])
def lire_ressource_materiel_divalto():
    return lire_donnes_ressources_materiel()