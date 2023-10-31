from app import db

class Secteur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    # Autres attributs des secteurs géographiques
