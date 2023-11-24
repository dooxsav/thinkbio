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

import time
from sqlalchemy.orm.exc import NoResultFound
from tqdm import tqdm
import requests
from app import db
from app.models import SITE_ISAFACT, SITE_GEOCODAGE

def geocodage_site(site):
    url = "https://api-adresse.data.gouv.fr/search/?q=" + site
    
    # Effectuer la requête GET
    response = requests.get(url)
    
    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        # Récupérer les données de la réponse
        data = response.json()  # Si la réponse est en JSON
        
        if data and "features" in data:
            for feature in data["features"]:
                if "geometry" in feature and "coordinates" in feature["geometry"]:
                    coordinates = feature["geometry"]["coordinates"]
                    if len(coordinates) >= 2:
                        latitude = float(coordinates[1])  # Latitude est à l'index 1
                        longitude = float(coordinates[0])  # Longitude est à l'index 0
                        print("latitude : " + str(latitude), "longitude : " +  str(longitude))
                        if latitude is not None and longitude is not None:
                            return {"latitude": latitude, "longitude": longitude}
                    else:
                        print("Les coordonnées sont incomplètes")
                        return None
                else:
                    print("Les données de géométrie sont absentes ou incorrectes")
                    return None
        else:
            print("Aucune donnée ou format de réponse incorrect")
            return None
    else:
        print(f"La requête a échoué avec le code : {response.status_code}")
        return None  # Requête échouée, coordonnées non disponibles

def Ecrire_base_GEOCODAGE():
    print('GEOCODAGE DES SITES...')
    ligne_ajoutees = 0 
    sites = SITE_ISAFACT.query.all()
    nbre_site = len(sites)
    
    for site in tqdm(sites, total=nbre_site, desc="Geocodage en cours"):
        try:
            site_geocode_entry = SITE_GEOCODAGE.query.filter_by(Site_id=site.Site_id).one()
        except NoResultFound:
            location_site = SITE_ISAFACT.query.filter_by(Site_id=site.Site_id).first()
            if location_site:
                print("location recherché : " + location_site.CPSite + " " + location_site.VilleSite)
                location = geocodage_site(location_site.CPSite)
                if location:
                    # Accéder aux valeurs de latitude et longitude du dictionnaire location
                    latitude = location["latitude"]
                    longitude = location["longitude"]

                    new_entry_geocodage = SITE_GEOCODAGE(
                        Site_id=site.Site_id,
                        Client_id=site.Client_id,
                        CodeClient=site.CodeClient,
                        latitude=latitude,
                        longitude=longitude,
                    )
                    db.session.add(new_entry_geocodage)
                    ligne_ajoutees += 1
                    time.sleep(1)
    db.session.commit()

    
    