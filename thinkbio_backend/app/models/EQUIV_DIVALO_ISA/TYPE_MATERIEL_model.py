from app import db


class TYPE_MATERIEL(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    DOSSIER = db.Column(db.String)
    CODEGENRE = db.Column(db.String)
    CODETYPERESSOURCEMATERIEL = db.Column(db.String)
    NUMERONOTE = db.Column(db.Integer)
    PRESENCEJOINT = db.Column(db.Integer)
    INDICEDOCUMENTREFERENCE = db.Column(db.Integer)
    DATEFINVALID = db.Column(db.String, nullable=True)
    LIBELLE_TYPE = db.Column(db.Integer)
    INDICATEURSIMOBILE = db.Column(db.Integer, nullable=True, default=2)
    QUESTION = db.Column(db.Integer)
    NATIMMO = db.Column(db.Integer)
    UTILISATEURMANAGER = db.Column(db.String)
    TYPECRMFL = db.Column(db.Integer)
    CRMUPDATEDH = db.Column(db.String)

    def __repr__(self):
        return f"<VotreModele(id={self.id}, DOSSIER='{self.DOSSIER}', CODEGENRE='{self.CODEGENRE}', ...)>"  
    
    def to_dict(self):
        return {
            'id': self.id,
            'DOSSIER': self.DOSSIER,
            'CODEGENRE': self.CODEGENRE,
            'CODETYPERESSOURCEMATERIEL': self.CODETYPERESSOURCEMATERIEL,
            'NUMERONOTE': self.NUMERONOTE,
            'PRESENCEJOINT': self.PRESENCEJOINT,
            'INDICEDOCUMENTREFERENCE': self.INDICEDOCUMENTREFERENCE,
            'DATEFINVALID': self.DATEFINVALID,
            'LIBELLE_TYPE': self.LIBELLE_TYPE,
            'INDICATEURSIMOBILE': self.INDICATEURSIMOBILE,
            'QUESTION': self.QUESTION,
            'NATIMMO': self.NATIMMO,
            'UTILISATEURMANAGER': self.UTILISATEURMANAGER,
            'TYPECRMFL': self.TYPECRMFL,
            'CRMUPDATEDH': self.CRMUPDATEDH
        }