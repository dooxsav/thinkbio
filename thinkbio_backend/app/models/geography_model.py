# geography.py

from app import db

class Geography(db.Model):
    numero_departement = db.Column(db.Integer, primary_key=True)
    pays = db.Column(db.String(50))
    region_departement = db.Column(db.String(50))
    nom_departement = db.Column(db.String(100))
    
    def __init__(self, numero_departement, pays, region_departement, nom_departement):
        self.pays = pays
        self.numero_departement = numero_departement
        self.region_departement = region_departement
        self.nom_departement = nom_departement

        
