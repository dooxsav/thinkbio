# model/categorie_client

from app import db

class T119_CATEG_CLIENT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DOSSIER = db.Column(db.String(30), default= 'BIONEST')
    CATCLICOD = db.Column(db.String(30))
    LIBELLE_TABLE_CATEGORIECLIENT = db.Column(db.String(30))
    EQUIV_ISAFACT = db.Column(db.String(30))
    INDICATEURSIBOUTONFACTURE = db.Column(db.Integer, default= 2)
    INDICATEURSIBOUTONBL = db.Column(db.Integer, default= 1)
    INDICATEURSIBOUTONACCOMPTE = db.Column(db.Integer, default= 1)
    INDICATEURSIBOUTONREGLEMENT = db.Column(db.String(30))
    BOUTONPARDEFAUT = db.Column(db.Integer, default= 1)
    INDICTARIF = db.Column(db.Integer, default= 1)
    CODEOPERATION = db.Column(db.String(30), default = "C")
    REGLIMMFL = db.Column(db.Integer, default= 2)
    
    def to_string(self):
        return {
            'id': self.id,
            'DOSSIER': self.DOSSIER,
            'CATCLICOD': self.CATCLICOD,
            'LIBELLE_TABLE_CATEGORIECLIENT': self.LIBELLE_TABLE_CATEGORIECLIENT,
            'EQUIV_ISAFACT': self.EQUIV_ISAFACT,
            'INDICATEURSIBOUTONFACTURE': self.INDICATEURSIBOUTONFACTURE,
            'INDICATEURSIBOUTONBL': self.INDICATEURSIBOUTONBL,
            'INDICATEURSIBOUTONACCOMPTE': self.INDICATEURSIBOUTONACCOMPTE,
            'INDICATEURSIBOUTONREGLEMENT': self.INDICATEURSIBOUTONREGLEMENT,
            'BOUTONPARDEFAUT': self.BOUTONPARDEFAUT,
            'INDICTARIF': self.INDICTARIF,
            'CODEOPERATION': self.CODEOPERATION,
            'REGLIMMFL': self.REGLIMMFL
        }
        


    
    


    
