from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50))
    courriel = db.Column(db.String(100))
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))

    def __init__(self, code, courriel, nom, prenom):
        self.code = code
        self.courriel = courriel
        self.nom = nom
        self.prenom = prenom

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
