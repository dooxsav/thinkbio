# service/DB_service
import csv
import re

from flask import jsonify	
from app import db
from app.models import Client, Geography, Client_ISAFACT
from app.utils import sanitarise_donnes_niveau1, convert_specific_to_date, clean_phone_number, extract_email
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
        # Lire le fichier Excel dans un DataFrame
        dataFrame = pd.read_excel(file_path)
        longueur_dataFrame_avant_suppression = len(dataFrame) # longueur initiale du DF
        total_rows = len(dataFrame)
        lignes_ajoutees = 0
        ligne_modifies = 0
        date_now = str(datetime.now())
    # Itération sur le DF
    
        # Utilisation de tqdm pour obtenir une barre de progression
        with tqdm(total=total_rows, desc="Importation en cours", unit=" lignes") as pbar:
            
            # Avant de commencer l'itération sur le DataFrame, supprimez les doublons basés sur la colonne 'CodeClient'
            dataFrame.drop_duplicates(subset='CodeClient', keep='first', inplace=True)
            longueur_dataFrame_apres_suppression = len(dataFrame)
            nombre_doublons_supprimes = longueur_dataFrame_avant_suppression - longueur_dataFrame_apres_suppression
            
            # Itération sur le DataFrame
            for index, row in dataFrame.iterrows():
                CodeClient = row['CodeClient']
                FamilleTIERS = row['FamilleTIERS']
                NomFACT = sanitarise_donnes_niveau1(row['NomFACT'])
                PrenomFACT = sanitarise_donnes_niveau1(row['PrenomFACT'])
                AdresseFACT = sanitarise_donnes_niveau1(row['AdresseFACT'])
                CPFACT = row['CPFACT']
                VilleFACT = row['VilleFACT']
                PaysFACT = row['PaysFACT']
                EmailTIERS = extract_email(row['EmailTIERS'])
                NomLOC = sanitarise_donnes_niveau1(row['NomLOC'])
                PrenomLOC = sanitarise_donnes_niveau1(row['PrenomLOC'])
                AdresseSITE = sanitarise_donnes_niveau1(row['AdresseSITE'])
                CPSITE = row['CPSITE']
                VilleSITE = row['VilleSITE']
                PaysSITE = row['PaysSITE']
                Livrer_adresse_facturation = row['Livrer_adresse_facturation']
                CodeTVA = row['CodeTVA']
                TVA = row['LibelleTVA']
                CodeTypeCONTRAT = row['CodeTypeCONTRAT']
                CodeCONTRAT = row['CodeCONTRAT']
                CategTARIF = row['CategTARIF']
                Mode_rglt = row['Mode_rglt']
                Delai_rglt = row['Delai_rglt']
                StatusTiers = row['StatusTiers']
                NivRelanceTiers = row['NivRelanceTiers']
                Nom_representant = row['Nom_representant']
                RIB_Domic = row['RIB_Domic']
                RIB_Etabl = row['RIB_Etabl']
                RIB_IBAN = row['RIB_IBAN']
                RIB_Cle = row['RIB_Cle']
                RIB_CodeBIC = row['RIB_CodeBIC']
                NEGOCE = (row['NEGOCE'])
                TP_nom = (row['TP_nom'])
                # Gestion des tels
                TP_tel = clean_phone_number(row['TP_tel'])
                TelSITE1 = clean_phone_number(row['TelSITE1'])
                TelSITE2 = clean_phone_number(row['TelSITE2'])
                TelSITE3 = clean_phone_number(row['TelSITE3'])
                TelFACT1 = clean_phone_number(row['TelFACT1'])
                TelFACT2 = clean_phone_number(row['TelFACT2'])
                TelFACT3 = clean_phone_number(row['TelFACT3'])
                # Convertir les dates au format correct
                Date_creation_tiers = datetime.strptime(str(row['Date_creation_tiers']), '%d/%m/%Y').date() if pd.notna(row['Date_creation_tiers']) else None
                DateProchaineIntervention = datetime.strptime(str(row['DateProchaineIntervention']), '%d/%m/%Y').date() if pd.notna(row['DateProchaineIntervention']) else None
                DateMEPContrat = datetime.strptime(str(row['DateMEPContrat']), '%d/%m/%Y').date() if pd.notna(row['DateMEPContrat']) else None
                Date_derniere_facture = convert_specific_to_date(row['DateMEPContrat'])
                
                # Controle présence de l'enregistrement, si présent => UPDATE sinon CREATE
        
                existing_record = Client_ISAFACT.query.filter_by(CodeClient=CodeClient).first()

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
                    existing_record.TelSITE2 = TelSITE2
                    existing_record.TelSITE3 = TelSITE3
                    existing_record.Livrer_adresse_facturation = Livrer_adresse_facturation
                    existing_record.CodeTVA = CodeTVA
                    existing_record.TVA = TVA
                    existing_record.CodeTypeCONTRAT = CodeTypeCONTRAT
                    existing_record.CodeCONTRAT = CodeCONTRAT
                    existing_record.CategTARIF = CategTARIF
                    existing_record.Mode_rglt = Mode_rglt
                    existing_record.Delai_rglt = Delai_rglt
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
                    existing_record.Date_creation_tiers = Date_creation_tiers
                    existing_record.DateProchaineIntervention = DateProchaineIntervention
                    existing_record.DateMEPContrat = DateMEPContrat
                    existing_record.Date_derniere_facture = Date_derniere_facture
                    existing_record.UpdatedAt = datetime.now()  # Mettez à jour le champ UpdatedAt
                    existing_record.LastUpdatedBy = 'ADMIN2'
                    ligne_modifies += 1
                    # Sauvegarde des modifications dans la base de données
                    db.session.commit()
                    # Mise à jour de la barre de progression
                    pbar.update(1)
                else:
                # Si l'enregistrement n'existe pas, créez un nouvel enregistrement
                    new_client = Client_ISAFACT(
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
                        CodeTypeCONTRAT = CodeTypeCONTRAT,
                        CodeCONTRAT=CodeCONTRAT,
                        CategTARIF=CategTARIF,
                        Mode_rglt=Mode_rglt,
                        Delai_rglt=Delai_rglt,
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
                        Date_creation_tiers=Date_creation_tiers,
                        DateProchaineIntervention=DateProchaineIntervention,
                        DateMEPContrat=DateMEPContrat,
                        Date_derniere_facture=Date_derniere_facture,
                        CreatedAt= datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S.%f'),
                        UpdatedAt= datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S.%f'),
                        CreatedBy='ADMIN',
                        LastUpdatedBy='ADMIN'
                    )
                    
                    db.session.add(new_client)
                    lignes_ajoutees += 1
                    # Ajout du nouvel enregistrement dans la base de données
                    db.session.commit()
                    # Mise à jour de la barre de progression
                    pbar.update(1)
                
        return jsonify({
            "message": f"Fichier .xlsx importé avec succès dans la base de données. {lignes_ajoutees} lignes ont été ajoutées, {ligne_modifies} lignes ont été mises à jour. {nombre_doublons_supprimes} doublons ont été supprimée pendant l'import"
        })
 
    
    except Exception as e:
        return jsonify({"error": f"Une erreur s'est produite : {str(e)}, ceci dit {lignes_ajoutees} ont été ajoutées et {ligne_modifies} ont été modifiées"}), 405
    
def lire_donnees_ISAFACT():
    clients = Client_ISAFACT.query.all()  # Récupérer tous les clients depuis la base de données
    clients_json = [client.to_dict() for client in clients]  # Convertir les objets clients en dictionnaires

    return jsonify(clients_json)  # Retourner les données au format JSON
      

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


