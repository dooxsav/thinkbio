# services/DB_operation_sevices
#
# Ce service est responsable des opérations sur les tables ISFACT et DIVALTO
#
#
#
#
#
#
#

from app import db
from app.models import Geography, Client_ISAFACT, Client_DIVALTO

def MaJ_Table_DIVALTO_Par_ISAFACT():
    return 'Mise à jour !'