from app import db

class MATERIEL_ISAFACT(db.Model):
    #__tablename__ = 'Matériels'

    id = db.Column(db.Integer, primary_key=True)
    NO_SERIE_BIONEST = db.Column(db.String(50))
    MODELE_SYSTEME = db.Column(db.String(50))
    MATERIAUX = db.Column(db.String(50))
    FABRIQUANT_CUVE = db.Column(db.String(50))
    GENRE = db.Column(db.String(50))
    TYPE = db.Column(db.String(50))
    CodeClient = db.Column(db.String(50))
    
    def __repr__(self):
        return f"<VotreModele id={self.id}, NO_SERIE_BIONEST={self.NO_SERIE_BIONEST}, MODELE_SYSTEME={self.MODELE_SYSTEME}, MATERIAUX={self.MATERIAUX}, FABRIQUANT_CUVE={self.FABRIQUANT_CUVE}, GENRE={self.GENRE}, TYPE={self.TYPE}, CodeClient={self.CodeClient}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'NO_SERIE_BIONEST': self.NO_SERIE_BIONEST,
            'MODELE_SYSTEME': self.MODELE_SYSTEME,
            'MATERIAUX': self.MATERIAUX,
            'FABRIQUANT_CUVE': self.FABRIQUANT_CUVE,
            'GENRE': self.GENRE,
            'TYPE': self.TYPE,
            'CodeClient': self.CodeClient
        }