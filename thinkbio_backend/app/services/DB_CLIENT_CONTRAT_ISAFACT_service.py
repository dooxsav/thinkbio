from app import db
from app.models import CLIENT_CONTRAT_ISAFACT, Client_ISAFACT, SITE_ISAFACT, T111_FAMILLE_CONTRAT_DIVALTO, CONTRAT_MODEL, CLI_ISFACT, ARTICLE_FACTURATION_CONTRAT, SITUATION_ISAFACT
import os
from tqdm import tqdm 
import json
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import func
from datetime import datetime

def lire_table_base_client_contrat_isafact():
        # Cette fonction récupère tous les enregistrements de la table CLIENT_CONTRAT_ISAFACT
    records = CLIENT_CONTRAT_ISAFACT.query.all()
    return [record.to_dict() for record in records]  # Convertir les objets en dictionnaires

def nbre_enregistrement_table_client_contrat():
    nbre_contrat = len(CLIENT_CONTRAT_ISAFACT.query.all())
    return nbre_contrat

def ecrire_table_base_client_contrat_isafact():
    lignes_ajoutees = 0
    lignes_modifiees = 0

    clients = Client_ISAFACT.query.all()
    total_clients = len(clients)

    for client in tqdm(clients, desc=" * Processing client/contrats", unit='client/s', total=total_clients):
        contrat_exist = None
        famille_contrat_divalto = None
        code_contrat_divalto = None
        mode_rglt = None
        libellé_contrat = ""

        # Vérification si le CodeContrat du client commence par "OUI"
        if client.CodeTypeCONTRAT and client.CodeTypeCONTRAT.startswith("OUI"):
            try:
                contrat_exist = CLIENT_CONTRAT_ISAFACT.query.filter_by(CodeClient=client.CodeClient).first()
            except NoResultFound:
                print("\033[91m **** ERREUR! Aucune correspondance trouvée pour le CONTRAT de: {}\033[0m".format(client.CodeClient))

            try:
                famille_contrat_divalto = T111_FAMILLE_CONTRAT_DIVALTO.query.filter_by(EQUIV_ISFACT_CodeTypeCONTRAT=client.CodeTypeCONTRAT).one().FAMILLECONTRAT
            except NoResultFound:
                print("\033[91m **** ERREUR! Aucune correspondance trouvée pour FAMILLE CONTRAT: {}\033[0m".format(client.CodeClient))
            
            try:
                result_contrat = CONTRAT_MODEL.query.filter_by(EQUIV_ISAFACT=client.CodeCONTRAT).first()
                if result_contrat:
                    code_contrat_divalto = result_contrat.CODECONTRAT
                    if code_contrat_divalto:
                        article_facturation = ARTICLE_FACTURATION_CONTRAT.query.filter_by(CODECONTRAT=code_contrat_divalto).first()
                        if article_facturation:
                            montant_ht_contrat = article_facturation.MONTANT_HT
                            if montant_ht_contrat is None:
                                print(f'\033[91m **** ATTENTION : pas de montant HT pour {client.CodeClient} ****\033[0m')
                        else:
                            print(f'\033[91m **** ATTENTION : aucun enregistrement d\'article de facturation trouvé pour {client.CodeClient} ****\033[0m')
                    libellé_contrat = result_contrat.LIBELLE_CONTRAT_MODELE
            except NoResultFound:
                print("\033[91m **** ERREUR! Aucune correspondance trouvée pour le CODE CONTRAT: {}\033[0m".format(client.CodeClient))
            
            # *** MODE de REGLEMENT ***
            try: 
                site_isafact = SITE_ISAFACT.query.filter_by(CodeClient=client.CodeClient).first()
                if site_isafact:
                    result_client_id = site_isafact.Client_id
                    if result_client_id:
                        cli_isafact = CLI_ISFACT.query.filter_by(Client_id=result_client_id).first()
                        if cli_isafact:
                            mode_rglt = cli_isafact.Mode_RGLT
                        else:
                            print("\033[91m **** ERREUR! Pas de MODE de REGLEMENT pour le client_id: {}\033[0m".format(result_client_id))
                    else:
                        print("\033[91m **** ERREUR! Aucun résultat trouvé pour le Client_id pour le CodeClient: {}\033[0m".format(client.CodeClient))
                else:
                    print("\033[91m **** ERREUR! Aucun enregistrement trouvé pour le CodeClient: {}\033[0m".format(client.CodeClient))

            except NoResultFound:
                print("\033[91m **** ERREUR! Pas de MODE de REGLEMENT pour le CodeClient: {}\033[0m".format(client.CodeClient))
                
            try:
                result_client_isafact = Client_ISAFACT.query.filter_by(CodeClient=client.CodeClient).first()
                if result_client_isafact:
                    if client.CodeTypeCONTRAT == "OUI.S":
                        libellé_contrat += f' Contrat SEMICO de {result_client_isafact.NomFACT}'
                    else:
                        if result_client_isafact.NomFACT:  # Vérifiez si NomFACT n'est pas None
                            libellé_contrat += f' pour Mr. ou Mne {result_client_isafact.NomFACT}'
                        else:
                            print("\033[91m **** ATTENTION! NomFACT est vide pour le contrat de: {}\033[0m".format(client.CodeClient))
                else:
                    print("\033[91m **** ATTENTION! Aucun résultat trouvé pour le contrat de: {}\033[0m".format(client.CodeClient))
            except NoResultFound:
                print("\033[91m **** ERREUR! Pas de Nom pour le contrat de: {}\033[0m".format(client.CodeClient))
            
            # Gestion des dates de MEP des contrats
            if not client.DateMEPContrat or client.DateMEPContrat == "":    
                # Filtre inital sur client.CodeClient
                results = SITUATION_ISAFACT.query.filter_by(CodeClient=client.CodeClient)
                if client.CodeTypeCONTRAT == "OUI.E": 
                    # Filtre supplémentaire sur le code d'article commençant par 'ENTRETIEN'
                    results = results.filter(SITUATION_ISAFACT.code_article.like('ENTRETIEN%'))
                elif client.CodeTypeCONTRAT == "OUI.T":
                    results = results.filter(SITUATION_ISAFACT.code_article.like('TRANQLOYERANNUE'))
                elif client.CodeTypeCONTRAT == "OUI.S":
                    results = results.filter(SITUATION_ISAFACT.code_article.like('ENTRETIEN.SC'))
                    # Trouver la valeur la plus ancienne dans la colonne date_document
                oldest_date = results.order_by(SITUATION_ISAFACT.date_document).first()
                if oldest_date:
                    oldest_date = oldest_date.date_document.strftime('%d/%m/%Y')
                else:
                    print(f'\033[1;33m INFORMATION : pas de code article ENTRETIEN pour {client.CodeClient} \033[0m')
            else:
                # Conversion de la chaîne en objet de date
                date_obj = datetime.strptime(client.DateMEPContrat, '%Y-%m-%d')
                oldest_date = date_obj.strftime('%d/%m/%Y')
                
                                   
            if contrat_exist and famille_contrat_divalto:
                # Si un enregistrement existe, mettre à jour les attributs
                contrat_exist.CodeClient = client.CodeClient
                contrat_exist.AdresseSite = client.AdresseSITE
                contrat_exist.VilleSite = client.VilleSITE
                contrat_exist.CPSite = client.CPSITE
                contrat_exist.CodeTypeCONTRAT = client.CodeTypeCONTRAT
                contrat_exist.CodeCONTRAT = client.CodeCONTRAT
                contrat_exist.FAMILLE_CONTRAT_DIVALTO = famille_contrat_divalto
                contrat_exist.CODE_CONTRAT_DIVALTO = code_contrat_divalto
                contrat_exist.MODE_RGLT = mode_rglt
                contrat_exist.LIBELLE_CONTRATCEA = libellé_contrat
                contrat_exist.MONTANT_HT = montant_ht_contrat
                contrat_exist.DateMEPContrat = oldest_date
                lignes_modifiees += 1
            else:
                # Si aucun enregistrement n'existe, ajouter un nouvel enregistrement
                site_isafact = SITE_ISAFACT.query.filter_by(CodeClient=client.CodeClient).first()

                if site_isafact:
                    CodeClient_DIVALTO = site_isafact.Client_id
                    CodeSite_DIVALTO = site_isafact.Site_id
                else:
                    # Affichage d'un message d'erreur en rouge dans la console
                    print("\033[91m **** ERREUR! Aucune correspondance trouvée pour CodeClient: {}\033[0m".format(client.CodeClient))
                    CodeClient_DIVALTO = None
                    CodeSite_DIVALTO = None

                nouveau_contrat = CLIENT_CONTRAT_ISAFACT(
                    CodeClient=client.CodeClient,
                    CodeClient_DIVALTO=CodeClient_DIVALTO,
                    CodeSite_DIVALTO=CodeSite_DIVALTO,
                    AdresseSite=client.AdresseSITE,
                    VilleSite=client.VilleSITE,
                    CPSite=client.CPSITE,
                    CodeTypeCONTRAT=client.CodeTypeCONTRAT,
                    CodeCONTRAT=client.CodeCONTRAT,
                    FAMILLE_CONTRAT_DIVALTO=famille_contrat_divalto,
                    CODE_CONTRAT_DIVALTO=code_contrat_divalto,
                    MODE_RGLT=mode_rglt,
                    LIBELLE_CONTRATCEA = libellé_contrat,
                    MONTANT_HT = montant_ht_contrat,
                    DateMEPContrat=oldest_date
                )
                db.session.add(nouveau_contrat)
                lignes_ajoutees += 1

    db.session.commit()

    return lignes_ajoutees, lignes_modifiees

def numerotation_contrat():
    print(' *** Numérotation des contrats...')
    compteur_contrat = 10000000
    
    contrats = CLIENT_CONTRAT_ISAFACT.query.all()
    nbre_contrat = len(contrats)
    
    for contrat in tqdm(contrats, desc=' * Numérotation des contrats', total=nbre_contrat):
        contrat.NUMERO_CONTRAT = compteur_contrat
        compteur_contrat += 1
    
    db.session.commit()
    
    
    print(' *** Numérotation des contrats terminée')