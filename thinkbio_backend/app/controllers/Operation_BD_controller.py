# controllers/operation_DB.py
#
# Ce controller s'occupe de gérer les opérations sur les bases de données
#
#

from app.services import KillAllTable

def HelloOperationDB():
    return "Hello!", 200

def MaJDIVALTO_table():
    return 'MaJDIVALTO_table'

def EtatdesDifferenceDIVALTOISFACT():
    return 'EtatdesDifferenceDIVALTOISFACT'

def KillSwitch():
    return KillAllTable()
    