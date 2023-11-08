import re

def sanitarise_donnes_niveau1(chaine):
    traitement = retirer_blancs(chaine)
    traitement = retirer_caracteres_speciaux(traitement)
    return traitement

def retirer_caracteres_speciaux(chaine):
    # Utilisation d'une expression régulière pour garder uniquement les lettres, les chiffres et les espaces
    chaine_traitee = re.sub(r'[^\w\s]', '', chaine)
    return chaine_traitee

def retirer_blancs(chaine):
    chaine_traitee = str(chaine).strip()
    return chaine_traitee