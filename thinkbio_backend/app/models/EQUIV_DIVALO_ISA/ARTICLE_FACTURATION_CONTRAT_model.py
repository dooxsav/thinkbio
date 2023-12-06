from app import db

class ARTICLE_FACTURATION_CONTRAT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DOSSIER = db.Column(db.String(30), default= 'BIONEST')
    CODECONTRAT = db.Column(db.String(30))
    MONTANT_HT = db.Column(db.Float)
    EQUIV_ISAFACT = db.Column(db.String(30))
    LIGNE = db.Column(db.Integer, default= 1)
    REFERENCE = db.Column(db.Integer)
    DESIGNATION = db.Column(db.String(30))
    POURCENT = db.Column(db.Integer, default= 100)
    
    def to_dict(self):
        return {
            'id': self.id,
            'DOSSIER': self.DOSSIER,
            'CODECONTRAT': self.CODECONTRAT,
            'MONTANT_HT' : self.MONTANT_HT,
            'EQUIV_ISAFACT': self.EQUIV_ISAFACT,
            'LIGNE': self.LIGNE,
            'REFERENCE': self.REFERENCE,
            'DESIGNATION': self.DESIGNATION,
            'POURCENT': self.POURCENT,
        }
