# service/DB_service
import csv
import re

from flask import jsonify
from app.models import Client, Geography	
from app import db
from tqdm import tqdm
from sqlalchemy.exc import IntegrityError

import pandas as pd


## ------------------------------------------------------------------------------------------------------------------------------------------------ ##
## ------------------------------------------------------------** Methods **----------------------------------------------------------------------- ##
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##

def testServiceDB():
    return "DBService Work !"

def remove_special_characters(text):
    if text is None:  # Vérifier si la valeur est nulle
        return "NC"
    return re.sub(r'[^A-Za-z0-9\s]', '', text)

def check_email(email):
    if not email or email.isspace():  # Vérifie si l'e-mail est vide ou ne contient que des espaces
        return "email non communiqué"

    # Si l'e-mail contient un espace ou un caractère '/', on le divise en plusieurs adresses
    emails = re.split(r'\s+|/', email)
    
    valid_emails = []
    for mail in emails:
        # Vérification du modèle d'e-mail
        if re.match(r'^\S+@\S+\.\S+$', mail.strip()):
            valid_emails.append(mail.strip())
    
    if valid_emails:
        return ', '.join(valid_emails)  # Retourne les adresses valides séparées par une virgule
    else:
        return "email non communiqué"

## ------------------------------------------------------------------------------------------------------------------------------------------------ ##
## ---------------------------------------------------------** Table Client **--------------------------------------------------------------------- ##
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##

def lire_base_de_donnes_client():

    clients = Client.query.all()
            # Convertir les données en format JSON
    data_json = [
        {
            'id': entry.id,
            'code': entry.code,
            'email': entry.courriel,
            'nom': entry.nom,
            'prenom': entry.prenom
        }
        for entry in clients
        ]

    return jsonify(data_json)
 
def lire_ecrire_mettre_a_jour_fichier_csv(file):
    with open(file, 'r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv, delimiter=';')
        next(lecteur_csv)  # Ignorer l'en-tête

        lignes_ajoutees = 0
        lignes_modifiees = 0

        for ligne in tqdm(lecteur_csv, desc="Importation en cours", unit=" lignes"):
            if len(ligne) >= 4:
                code = ligne[0].strip()
                email = check_email(ligne[1].lower())
                nom = remove_special_characters(ligne[2].strip())
                prenom = remove_special_characters(ligne[3].strip())

                # Vérification et nettoyage du champ "Code"
                code = code if code and len(code) >= 7 else ""  # Vérifie si le code est valide

                client_existant = Client.query.filter_by(code=code).first()

                if client_existant:
                    # Mettre à jour les valeurs existantes
                    client_existant.courriel = email
                    client_existant.nom = nom
                    client_existant.prenom = prenom
                    lignes_modifiees += 1
                else:
                    # Créer une nouvelle entrée
                    nouveau_client = Client(
                        code=code,
                        courriel=email,
                        nom=nom,
                        prenom=prenom
                    )
                    db.session.add(nouveau_client)
                    lignes_ajoutees += 1

        db.session.commit()

    return jsonify({"message": f"Fichier CSV importé avec succès dans la base de données. {lignes_ajoutees} lignes ont été ajoutées, {lignes_modifiees} lignes ont été mises à jour."})

## ------------------------------------------------------------------------------------------------------------------------------------------------ ##
## -------------------------------------------------------** Table GEOGRAPHY **-------------------------------------------------------------------- ##
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##

def lire_ercrire_mettre_a_jour_table_geography(file_path):
    try:
        # Ouvre le fichier Excel
        df = pd.read_excel(file_path)
        lignes_ajoutees = 0
        lignes_modifiees = 0
        
        # Itération sur le DF (DataFrame)
        for index, row in df.iterrows():
            numero_departement = row['numero_departement']
            nom_departement = row['nom_departement']
            region_departement = row['region_departement']
            pays = row['pays']

            # Vérifie s'il existe déjà une entrée pour ce numéro de département
            existing_departement = Geography.query.filter_by(numero_departement=numero_departement).first()

            if existing_departement:
                # Mettre à jour les valeurs de l'entrée existante
                existing_departement.nom_departement = nom_departement
                existing_departement.region_departement = region_departement
                existing_departement.pays = pays
                lignes_modifiees += 1
            else:
                # Création d'une nouvelle instance de la classe Departement
                new_departement = Geography(numero_departement=numero_departement, nom_departement=nom_departement, region_departement=region_departement, pays=pays)
                db.session.add(new_departement)
                lignes_ajoutees += 1

        # Enregistrer les modifications dans la base de données
        db.session.commit()

        return jsonify({
            "message": f"Fichier CSV importé avec succès dans la base de données. {lignes_ajoutees} lignes ont été ajoutées, {lignes_modifiees} lignes ont été mises à jour."
        })
    except Exception as e:
        return jsonify({"error": f"Une erreur s'est produite : {str(e)}"}), 405
    
def lire_donnees_BD_geography():
    departement = Geography.query.all()

    # Convertir les données en format JSON
    data_json = [
        {
            'numero_departement': str(entry.numero_departement),
            "nom_departement": entry.nom_departement,
            "region_departement": entry.region_departement
        }
        for entry in departement
    ]

    return jsonify(data_json)

