# services/DB_GEOCODING_sevices
#
# Ce service est responsable des opérations de géocoding
#
#
#
#
#
#
#
from flask import jsonify
import time
from sqlalchemy.orm.exc import NoResultFound
from tqdm import tqdm
import requests
from app import db
from app.models import SITE_ISAFACT, SITE_GEOCODAGE, CLIENT_CONTRAT_ISAFACT

def geocodage_site(site):
    url = "https://api-adresse.data.gouv.fr/search/?q=" + site
    
    try:
        # Effectuer la requête GET
        response = requests.get(url)
        response.raise_for_status()  # Vérifier les erreurs HTTP
        
        # Vérifier si la requête a réussi (code 200)
        if response.status_code == 200:
            # Récupérer les données de la réponse
            data = response.json()  # Si la réponse est en JSON
            
            if data and "features" in data:
                if data["features"]:
                    for feature in data["features"]:
                        if "geometry" in feature and "coordinates" in feature["geometry"]:
                            coordinates = feature["geometry"]["coordinates"]
                            if len(coordinates) >= 2:
                                latitude = float(coordinates[1])  # Latitude est à l'index 1
                                longitude = float(coordinates[0])  # Longitude est à l'index 0
                                
                                if latitude is not None and longitude is not None:
                                    return {"latitude": latitude, "longitude": longitude}
                                else:
                                    print("Les coordonnées sont incomplètes")
                                    return None
                            else:
                                print("Les coordonnées sont incomplètes")
                                return None
                        else:
                            print("Les données de géométrie sont absentes ou incorrectes")
                            return None
                else:
                    print(f'No Data found for {site}')
                    return None
            else:
                print("Aucune donnée ou format de réponse incorrect")
                return None
        else:
            print(f"La requête a échoué avec le code : {response.status_code}")
            return None  # Requête échouée, coordonnées non disponibles
            
    except requests.RequestException as e:
        print(f"Une erreur de requête s'est produite : {e}")
        return None

def Ecrire_base_GEOCODAGE():
    print(' * GEOCODAGE DES SITES...')
    ligne_ajoutees = 0

    sites = SITE_ISAFACT.query.all()
    nbre_site = len(sites)

    for site in sites:
        try:
            site_geocode_entry = SITE_GEOCODAGE.query.filter_by(Site_id=site.Site_id).one()
        except NoResultFound:
            location_site = SITE_ISAFACT.query.filter_by(Site_id=site.Site_id).first()
            if location_site:
                location = geocodage_site(location_site.CPSite)
                if location is not None:  # Vérification de la géolocalisation non nulle
                    latitude = location.get("latitude")
                    longitude = location.get("longitude")
                    try:
                        new_entry_geocodage = SITE_GEOCODAGE(
                            Site_id=site.Site_id,
                            Client_id=site.Client_id,
                            CodeClient=site.CodeClient,
                            latitude=latitude,
                            longitude=longitude,
                        )
                        db.session.add(new_entry_geocodage)
                        db.session.commit()
                        ligne_ajoutees += 1
                        print(f" * Recherche de localisation en cours pour : {location_site.CPSite} {location_site.VilleSite} => longitude: {longitude}, latitude : {latitude} ({ligne_ajoutees}/{nbre_site})", end="\r")
                    except Exception as exception:
                        print(f"*** Problème lors du géocodage de {location_site.CPSite} {location_site.VilleSite}: {exception}")
                else:
                    # Gérer le cas où la géolocalisation n'est pas possible
                    print(f"*** La géolocalisation pour {location_site.CPSite} {location_site.VilleSite} n'a pas été trouvée.")
            else:
                # Gérer le cas où l'emplacement du site n'est pas trouvé dans la base de données
                print(f"*** Emplacement non trouvé pour le site ID {site.Site_id}.")

def lire_base_site_geocodage():
    sites = SITE_GEOCODAGE.query.all()
    sites_json = [site.to_dict() for site in sites]
    return jsonify(sites_json)

def lire_base_site_geocodage_avec_contrats():
    # Récupération des sites de SITE_GEOCODAGE
    sites = SITE_GEOCODAGE.query.all()

    # Liste pour stocker les données finales
    sites_with_contrats = []

    # Récupération des informations pour chaque site
    for site in sites:
        # Récupération des informations du site
        site_info = site.to_dict()

        # Récupération des informations de contrat correspondant au CodeClient du site
        contrat_info = CLIENT_CONTRAT_ISAFACT.query.filter_by(CodeClient=site.CodeClient).first()

        # Création d'un dictionnaire combinant les informations du site et du contrat
        combined_info = {
            'Site_Info': site_info,
            'Contrat_Info': {
                'CodeTypeCONTRAT': contrat_info.CodeTypeCONTRAT if contrat_info else None,
                'CodeCONTRAT': contrat_info.CodeCONTRAT if contrat_info else None,
                'FAMILLE_CONTRAT_DIVALTO': contrat_info.FAMILLE_CONTRAT_DIVALTO if contrat_info else None,
                'CODE_CONTRAT_DIVALTO': contrat_info.CODE_CONTRAT_DIVALTO if contrat_info else None,
                'MODE_RGLT': contrat_info.MODE_RGLT if contrat_info else None
            }
        }

        # Ajout du dictionnaire combiné à la liste des sites avec contrats
        sites_with_contrats.append(combined_info)

    return jsonify(sites_with_contrats)
    
    

    
    