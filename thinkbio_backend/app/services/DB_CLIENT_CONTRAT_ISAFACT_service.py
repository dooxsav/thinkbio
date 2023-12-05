from app import db
from app.models import CLIENT_CONTRAT_ISAFACT, Client_ISAFACT, SITE_ISAFACT
import os
from tqdm import tqdm 
import json

def lire_table_base_client_contrat_isafact():
        # Cette fonction récupère tous les enregistrements de la table CLIENT_CONTRAT_ISAFACT
    records = CLIENT_CONTRAT_ISAFACT.query.all()
    return [record.to_dict() for record in records]  # Convertir les objets en dictionnaires

def ecrire_table_base_client_contrat_isafact():
    lignes_ajoutees = 0
    lignes_modifiees = 0

    clients = Client_ISAFACT.query.all()
    total_clients = len(clients)

    for client in tqdm(clients, desc=" * Processing client/contrats", unit='client/s', total=total_clients):
        # Vérification si le CodeContrat du client commence par "OUI"
        if client.CodeTypeCONTRAT is not None and client.CodeTypeCONTRAT.startswith("OUI"):
            # Vérification de l'existence d'un enregistrement pour ce client dans CLIENT_CONTRAT_ISAFACT
            contrat_exist = CLIENT_CONTRAT_ISAFACT.query.filter_by(CodeClient=client.CodeClient).first()

            if contrat_exist:
                # Si un enregistrement existe, mettre à jour les attributs
                contrat_exist.CodeClient = client.CodeClient
                contrat_exist.AdresseSite = client.AdresseSITE
                contrat_exist.VilleSite = client.VilleSITE
                contrat_exist.CPSite = client.CPSITE
                contrat_exist.CodeTypeCONTRAT = client.CodeTypeCONTRAT
                contrat_exist.CodeCONTRAT = client.CodeCONTRAT
                contrat_exist.DateMEPContrat = client.DateMEPContrat
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
                    DateMEPContrat=client.DateMEPContrat)
                db.session.add(nouveau_contrat)
                lignes_ajoutees += 1

    db.session.commit()

    return lignes_ajoutees, lignes_modifiees
    