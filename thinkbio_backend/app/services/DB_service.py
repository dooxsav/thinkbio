# service/DB_service
import csv
import re

from flask import jsonify
from app.models import Client, Geography, Client_ISFACT	
from app import db
from tqdm import tqdm
from sqlalchemy.exc import IntegrityError

import pandas as pd
from datetime import datetime

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
    
def enregistrerFichier():
    return None

## ------------------------------------------------------------------------------------------------------------------------------------------------ ##
## -------------------------------------------------------** Table CLIENT ISFACT **-------------------------------------------------------------------- ##
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##

def Ecrire_MAJ_Clients_ISFACT(file_path):
    # Initialisation
    try:
        dataFrame = pd.read_excel(file_path)
        lignes_ajoutees = 0
        ligne_modifies = 0
    
    # Itération sur le DF
    
        for index, row in dataFrame.iterrows():
            CodeClient = row['CodeClient']
            FamilleTIERS = row['FamilleTIERS']
            NomFACT = row['NomFACT']
            PrenomFACT = row['PrenomFACT']
            AdresseFACT = row['AdresseFACT']
            CPFACT = row['CPFACT']
            VilleFACT = row['VilleFACT']
            PaysFACT = row['PaysFACT']
            EmailTIERS = row['EmailTIERS']
            TelFACT1 = row['TelFACT1']
            TelFACT2 = row['TelFACT2']
            TelFACT3 = row['TelFACT3']
            NomLOC = row['NomLOC']
            PrenomLOC = row['PrenomLOC']
            AdresseSITE = row['AdresseSITE']
            CPSITE = row['CPSITE']
            VilleSITE = row['VilleSITE']
            PaysSITE = row['PaysSITE']
            TelSITE1 = row['TelSITE1']
            TelSITE2 = row['TelSITE2']
            TelSITE3 = row['TelSITE3']
            Livrer_adresse_facturation = row['Livrer_adresse_facturation    ']
            CodeTVA = row['CodeTVA']
            TVA = row['LibelleTVA']
            CodeCONTRAT = row['CodeCONTRAT']
            CategTARIF = row['CategTARIF']
            Mode_rglt = row['Mode_rglt']
            Delai_rglt = row['Delai_rglt']
            Date_creation_tiers = row['Date_creation_tiers']
            StatusTiers = row['StatusTiers']
            NivRelanceTiers = row['NivRelanceTiers']
            Nom_representant = row['Nom_representant']
            RIB_Domic = row['RIB_Domic']
            RIB_Etabl = row['RIB_Etabl']
            RIB_IBAN = row['RIB_IBAN']
            RIB_Cle = row['RIB_Cle']
            RIB_CodeBIC = row['RIB_CodeBIC']
            NEGOCE = row['NEGOCE']
            TP_nom = row['TP_nom']
            TP_tel = row['TP_tel']
            DateProchaineIntervention = row['DateProchaineIntervention']
            DateMEPContrat  = row['DateMEPContrat']

            
    # Controle présence de l'enregistrement, si présent => UPDATE sinon CREATE
    
        existing_record = Client_ISFACT.query.filter_by(CodeClient=CodeClient).first()
        
        if existing_record:
        # Si l'enregistrement existe déjà, mettez à jour ses valeurs
            existing_record.FamilleTIERS = FamilleTIERS
            existing_record.NomFACT = NomFACT
            existing_record.PrenomFACT = PrenomFACT
            existing_record.AdresseFACT = AdresseFACT
            existing_record.CPFACT = CPFACT
            existing_record.VilleFACT = VilleFACT
            existing_record.PaysFACT = PaysFACT
            existing_record.EmailTIERS = EmailTIERS
            existing_record.TelFACT1 = TelFACT1
            existing_record.TelFACT2 = TelFACT2
            existing_record.TelFACT3 = TelFACT3
            existing_record.NomLOC = NomLOC
            existing_record.PrenomLOC = PrenomLOC
            existing_record.AdresseSITE = AdresseSITE
            existing_record.CPSITE = CPSITE
            existing_record.VilleSITE = VilleSITE
            existing_record.PaysSITE = PaysSITE
            existing_record.TelSITE1 = TelSITE1
            existing_record.TelSITE1 = TelSITE2
            existing_record.TelSITE1 = TelSITE3
            existing_record.Livrer_adresse_facturation = Livrer_adresse_facturation
            existing_record.CodeTVA = CodeTVA
            existing_record.TVA = TVA
            existing_record.CodeCONTRAT = CodeCONTRAT
            existing_record.CategTARIF = CategTARIF
            existing_record.Mode_rglt = Mode_rglt
            existing_record.Delai_rglt = Delai_rglt
            existing_record.Date_creation_tiers = Date_creation_tiers
            existing_record.StatusTiers = StatusTiers
            existing_record.NivRelanceTiers = NivRelanceTiers
            existing_record.Nom_representant = Nom_representant
            existing_record.RIB_Domic = RIB_Domic
            existing_record.RIB_Etabl = RIB_Etabl
            existing_record.RIB_IBAN = RIB_IBAN
            existing_record.RIB_Cle  = RIB_Cle 
            existing_record.RIB_CodeBIC = RIB_CodeBIC
            existing_record.NEGOCE = NEGOCE
            existing_record.TP_nom = TP_nom
            existing_record.TP_tel = TP_tel
            existing_record.DateProchaineIntervention = DateProchaineIntervention
            existing_record.DateMEPContrat = DateMEPContrat
            existing_record.UpdatedAt = datetime.now()
            existing_record.LastUpdatedBy = 'ADMIN2'
            ligne_modifies += 1
            # Sauvegarde des modifications dans la base de données
            db.session.commit()
        else:
        # Si l'enregistrement n'existe pas, créez un nouvel enregistrement
            new_client = Client_ISFACT(
                CodeClient=CodeClient,
                FamilleTIERS=FamilleTIERS,
                NomFACT=NomFACT,
                PrenomFACT=PrenomFACT,
                AdresseFACT=AdresseFACT,
                CPFACT=CPFACT,
                VilleFACT=VilleFACT,
                PaysFACT=PaysFACT,
                EmailTIERS=EmailTIERS,
                TelFACT1=TelFACT1,
                TelFACT2=TelFACT2,
                TelFACT3=TelFACT3,
                NomLOC=NomLOC,
                PrenomLOC=PrenomLOC,
                AdresseSITE=AdresseSITE,
                CPSITE=CPSITE,
                VilleSITE=VilleSITE,
                PaysSITE=PaysSITE,
                TelSITE1=TelSITE1,
                TelSITE2=TelSITE2,
                TelSITE3=TelSITE3,
                Livrer_adresse_facturation=Livrer_adresse_facturation,
                CodeTVA=CodeTVA,
                TVA=TVA,
                CodeCONTRAT=CodeCONTRAT,
                CategTARIF=CategTARIF,
                Mode_rglt=Mode_rglt,
                Delai_rglt=Delai_rglt,
                Date_creation_tiers=Date_creation_tiers,
                StatusTiers=StatusTiers,
                NivRelanceTiers=NivRelanceTiers,
                Nom_representant=Nom_representant,
                RIB_Domic=RIB_Domic,
                RIB_Etabl=RIB_Etabl,
                RIB_IBAN=RIB_IBAN,
                RIB_Cle=RIB_Cle,
                RIB_CodeBIC=RIB_CodeBIC,
                NEGOCE=NEGOCE,
                TP_nom=TP_nom,
                TP_tel=TP_tel,
                DateProchaineIntervention=DateProchaineIntervention,
                DateMEPContrat=DateMEPContrat,
                CreatedAt= datetime.now(),
                UpdatedAt= datetime.now(),
                CreatedBy='ADMIN',
                LastUpdatedBy='ADMIN'
            )
            
            db.session.add(new_client)
            lignes_ajoutees += 1
            # Ajout du nouvel enregistrement dans la base de données
            db.session.commit()
        
        return f"Nombre de lignes ajoutées : {lignes_ajoutees}, Nombre de lignes modifiées : {ligne_modifies}"
 
    
    except Exception as e:
        return jsonify({"error": f"Une erreur s'est produite : {str(e)}"}), 405
    
        
    
    return 'toto'

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


