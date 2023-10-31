# service/DB_service
import csv
from app.models import Client
from tqdm import tqdm

def testFonctionnel():
    return "titi"

def lire_ecrire_fichier_csv(file):
    with open(file, 'r') as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv)
        total_lignes = sum(1 for line in lecteur_csv)
        
        fichier_csv.seek(0)
        lecteur_csv = csv.DictReader(fichier_csv)

        for ligne in tqdm(lecteur_csv, total=total_lignes, desc="Importation en cours", unit=" lignes"):
            try:
                nouveau_client = Client(
                    code=ligne.get("Code"),
                    courriel=ligne.get("EMail"),
                    nom=ligne.get("Nom"),
                    prenom=ligne.get("Prenom")
                )
                nouveau_client.save_to_db()
            except KeyError as e:
                print(f"Clé manquante dans le fichier CSV : {e}")

    return "Fichier CSV importé avec succès dans la base de données"