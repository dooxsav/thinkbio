# routes/__init__.py
#
# La responsabilité du fichier route est de récupérer les informations de routage et de faire les traitements initiaux
#
# Si des importations ou des configurations sont nécessaires pour tous les fichiers dans le dossier routes,
# vous pouvez les placer ici.

from .hello_routes import hello_bp
from .GRC_routes import GRC_bp
from .client_routes import Client_bp
from .geography_routes import Geography_bp
from .client_ISAFACT_routes import Client_ISAFACT_bp