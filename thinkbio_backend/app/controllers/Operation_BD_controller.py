# controllers/operation_DB.py
#
# Ce controller s'occupe de gérer les opérations sur les bases de données
#
#

from app.services import MaJ_Table_DIVALTO_Par_ISAFACT

def HelloOperationDB():
    return MaJ_Table_DIVALTO_Par_ISAFACT()

def MaJDIVALTO_table():
    return 'MaJDIVALTO_table'

def EtatdesDifferenceDIVALTOISFACT():
    return 'EtatdesDifferenceDIVALTOISFACT'