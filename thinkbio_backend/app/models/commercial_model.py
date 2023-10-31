from app import db

class Commercial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    email = db.Column(db.String(50))
    
    # Relation entre commerciaux et secteurs géographiques
    secteurs = db.relationship('Secteur', secondary='commercial_secteur', backref='commerciaux', lazy='dynamic')
    
    def __repr__(self):
        return f"Commercial {self.nom} {self.prenom}"
