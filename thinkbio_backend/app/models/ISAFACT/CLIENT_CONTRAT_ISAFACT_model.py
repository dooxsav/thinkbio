from app import db
from datetime import datetime

class CLIENT_CONTRAT_ISAFACT(db.Model):
    __tablename__ = 'CLIENT_CONTRAT_ISAFACT'

    id = db.Column(db.Integer, primary_key=True)
    CodeClient = db.Column(db.String(7))
    AdresseSite = db.Column(db.String(30))
    VilleSite = db.Column(db.String(30))
    CPSite = db.Column(db.String(5))
    CodeTypeCONTRAT = db.Column(db.String(5))
    CodeCONTRAT = db.Column(db.String(5))
    DateMEPContrat = db.Column(db.String(30))
    CodeClient_DIVALTO = db.Column(db.String(30))
    CodeSite_DIVALTO = db.Column(db.String(30))
    FAMILLE_CONTRAT_DIVALTO = db.Column(db.String)
    CODE_CONTRAT_DIVALTO = db.Column(db.String)
    MODE_RGLT = db.Column(db.String)
    LIBELLE_CONTRATCEA = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"CLIENT_CONTRAT_ISAFACT(id={self.id}, CodeClient='{self.CodeClient}', AdresseSite='{self.AdresseSite}', VilleSite='{self.VilleSite}', CPSite='{self.CPSite}', CodeTypeCONTRAT='{self.CodeTypeCONTRAT}', CodeCONTRAT='{self.CodeCONTRAT}', DateMEPContrat='{self.DateMEPContrat}', created_at='{self.created_at}', updated_at='{self.updated_at}')"
    
    def to_dict(self):
        return {
            'id': self.id,
            'CodeClient': self.CodeClient,
            'AdresseSite': self.AdresseSite,
            'VilleSite': self.VilleSite,
            'CPSite': self.CPSite,
            'CodeTypeCONTRAT': self.CodeTypeCONTRAT,
            'CodeCONTRAT': self.CodeCONTRAT,
            'DateMEPContrat': self.DateMEPContrat,
            'CodeClient_DIVALTO': self.CodeClient_DIVALTO,
            'CodeSite_DIVALTO': self.CodeSite_DIVALTO,
            'FAMILLE_CONTRAT_DIVALTO': self.FAMILLE_CONTRAT_DIVALTO,
            'CODE_CONTRAT_DIVALTO': self.CODE_CONTRAT_DIVALTO,
            'MODE_RGLT': self.MODE_RGLT,
            'LIBELLE_CONTRATCEA' : self.LIBELLE_CONTRATCEA,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        
    
    
    
    
    
    