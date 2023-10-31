from app import db

commercial_secteur = db.Table('commercial_secteur',
    db.Column('commercial_id', db.Integer, db.ForeignKey('commercial.id')),
    db.Column('secteur_id', db.Integer, db.ForeignKey('secteur.id'))
)