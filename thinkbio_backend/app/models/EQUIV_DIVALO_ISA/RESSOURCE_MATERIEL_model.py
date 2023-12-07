from app import db

class RESSOURCE_MATERIEL_DIVALTO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DOSSIER = db.Column(db.String(50), default='BIONEST')
    CODEMATERIEL = db.Column(db.String(50))
    ETABLISSEMENT = db.Column(db.String(50), default='001')
    CODEGENRE = db.Column(db.String(50))
    CODETYPERESSOURCEMATERIEL = db.Column(db.String(50))
    DESIGNATIONMATERIEL = db.Column(db.String(100))
    CODELOCALISATION = db.Column(db.String(50)) # code SITE DIVALTO
    MARQUE = db.Column(db.String(50))
    TIERSINDIVIDU = db.Column(db.String(50)) # Code CLIENT DIVALTO
    NUMEROSERIEBIEN = db.Column(db.String(50)) # code ISAFACT
    CODE_CONTRAT_DIVALTO = db.Column(db.String(50))
    
    def to_dict(self):
        return {
            'id': self.id,
            'DOSSIER': self.DOSSIER,
            'CODEMATERIEL': self.CODEMATERIEL,
            'ETABLISSEMENT': self.ETABLISSEMENT,
            'CODEGENRE': self.CODEGENRE,
            'CODETYPERESSOURCEMATERIEL': self.CODETYPERESSOURCEMATERIEL,
            'DESIGNATIONMATERIEL': self.DESIGNATIONMATERIEL,
            'CODELOCALISATION' : self.CODELOCALISATION,
            'MARQUE': self.MARQUE,
            'TIERSINDIVIDU': self.TIERSINDIVIDU,
            'NUMEROSERIEBIEN': self.NUMEROSERIEBIEN,
            'CODE_CONTRAT_DIVALTO': self.CODE_CONTRAT_DIVALTO
        }


    
