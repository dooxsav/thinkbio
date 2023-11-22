import re
import pandas as pd
from datetime import datetime
from unidecode import unidecode


def sanitarise_donnes_niveau1(chaine):
    traitement = retirer_blancs(chaine)
    traitement = retirer_caracteres_speciaux(traitement)
    traitement = mettre_en_majuscules(traitement)
    return traitement

def mettre_en_majuscules(chaine):
    chaine_traitee = chaine.upper()
    return chaine_traitee
    
def retirer_caracteres_speciaux(chaine):
    # Retirer les accents
    chaine_sans_accents = unidecode(chaine)
    # Remplacer les caractères séparatifs par des espaces
    chaine_traitee = re.sub(r'[-_]', ' ', chaine_sans_accents)
    # Remplacer les espaces multiples par un seul espace
    chaine_traitee = re.sub(r'\s+', ' ', chaine_traitee)
    # Supprimer les espaces au début et à la fin de la chaîne
    chaine_traitee = chaine_traitee.strip()
    return chaine_traitee

def retirer_blancs(chaine):
    chaine_traitee = str(chaine).strip()
    return chaine_traitee

def convert_specific_to_date(date_str):
    if pd.notna(date_str) and date_str != '00:00:00':
        return datetime.strptime(str(date_str), '%d/%m/%Y').date()
    else:
        return None
    
def clean_phone_number(phone):
    # Convertir le numéro de téléphone en chaîne
    phone_str = str(phone)

    # Ajouter un '0' en première position si la chaîne termine par ".0"
    if phone_str.endswith('.0'):
        cleaned_number = '0' + phone_str[:-2]  # Supprimer '.0' à la fin
    else:
        # Supprimer les caractères non numériques et les espaces
        cleaned_number = ''.join(filter(lambda x: x.isdigit() or x.isspace(), phone_str))

    # S'assurer que la longueur totale est de 10 caractères
    if not len(cleaned_number) == 10:
        return cleaned_number.replace(" ", "")  # Retirer les espaces entre les caractères
    else:
        return cleaned_number  # Retourner None si la longueur n'est pas correcte

def extract_email(text):
    # Convertir la valeur en chaîne de caractères
    text_str = str(text)
    
    # Si la valeur est vide, retourner None
    if not text_str:
        return None
    
    # Utilisation d'une expression régulière pour extraire une adresse e-mail
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(email_pattern, text_str)
    
    # Si des correspondances sont trouvées, retourner la première adresse e-mail trouvée
    if matches:
        return matches[0]
    else:
        return None
