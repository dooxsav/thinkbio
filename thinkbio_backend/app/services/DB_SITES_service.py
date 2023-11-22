# services/DB_site.py
#

from app import db
from app.models import Client_ISAFACT, CLI_ISFACT, SITE_ISAFACT
from tqdm import tqdm
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound

def Transfert_donnes_CLIENT_ISAFACT_SITES():
    # Récupération des informations depuis table ISFACT
    # La table ISFACT reflète TOUS les sites.
    print('Ecriture de la base SITE...')
    Donnes_depuis_CLIENT_ISAFACT = Client_ISAFACT.query.all()
    lignes_ajouté = 0
    ligne_modifie = 0
    total_site = len(Donnes_depuis_CLIENT_ISAFACT)

    for site in tqdm(Donnes_depuis_CLIENT_ISAFACT, total=total_site, desc='Processing SITES from Table ISAFACT', unit="site/s"):
        # Recherche d'un correspondance. Si la correspondance est trouvée => UPDATE sinon CREATE
        try:
            entrée_site = SITE_ISAFACT.query.filter_by(CodeClient = site.CodeClient).one()
            entrée_site.FamilleTIERS = site.FamilleTIERS
            entrée_site.AdresseSite = site.AdresseSITE
            entrée_site.VilleSite = site.VilleSITE
            entrée_site.CPSite = site.CPSITE
            entrée_site.CreatedAt = site.CreatedAt
            entrée_site.LastUpdatedBy = datetime.now()
            entrée_site.LastUpdatedBy = 'ADMIN'
            ligne_modifie += 1
        # Ecriture du site dans la table
        except NoResultFound:
            new_entry_site = SITE_ISAFACT(
                CodeClient = site.CodeClient,
                FamilleTIERS = site.FamilleTIERS,
                AdresseSite = site.AdresseSITE,
                VilleSite = site.VilleSITE,
                CPSite = site.CPSITE,
                CreatedAt = datetime.now(),
                UpdatedAt = datetime.now(),
                CreatedBy = 'CREATOR',
                LastUpdatedBy = 'CREATOR'
            )
            db.session.add(new_entry_site)
            lignes_ajouté += 1
            
    db.session.commit()
    return lignes_ajouté, ligne_modifie

def numerotation_sites():
    # Cette fonction numérote les site avec 10 chiffres NON significatif
    print('Numérotation des sites....')
    Données_site = SITE_ISAFACT.query.all()
    longueur_table = len(Données_site)
    compteur_site = 0
    for site in tqdm(Données_site, desc="Numerating site", unit="site/s", total=longueur_table):
        site.Site_id = f'S{compteur_site:010d}'
        compteur_site += 1  # Incrémente compteur_site pour chaque site
    db.session.commit()
    return compteur_site