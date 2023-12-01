from app import db

class Contrat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DOSSIER = db.Column(db.Integer)
    FAMILLECONTRAT = db.Column(db.String)
    NUMERONOTE = db.Column(db.String)
    LIBELLE_TABLE_FAMILLECONTRAT = db.Column(db.String)
    CONTRATTYP = db.Column(db.Integer)
    DATEFINVALID = db.Column(db.DateTime)
    STRUCTUREREFERENCECONTRAT = db.Column(db.String)
    CRMUPDATEDH = db.Column(db.DateTime)
    
    def __repr__(self):
        return f"<Contrat(DOSSIER={self.DOSSIER}, FAMILLECONTRAT={self.FAMILLECONTRAT}, NUMERONOTE={self.NUMERONOTE}, CONTRATTYP={self.CONTRATTYP})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'DOSSIER': self.DOSSIER,
            'FAMILLECONTRAT': self.FAMILLECONTRAT,
            'NUMERONOTE': self.NUMERONOTE,
            'LIBELLE_TABLE_FAMILLECONTRAT': self.LIBELLE_TABLE_FAMILLECONTRAT,
            'CONTRATTYP': self.CONTRATTYP,
            'DATEFINVALID': self.DATEFINVALID.strftime("%Y-%m-%d") if self.DATEFINVALID else None,
            'STRUCTUREREFERENCECONTRAT': self.STRUCTUREREFERENCECONTRAT,
            'CRMUPDATEDH': self.CRMUPDATEDH.strftime("%Y-%m-%d %H:%M:%S") if self.CRMUPDATEDH else None

            }
