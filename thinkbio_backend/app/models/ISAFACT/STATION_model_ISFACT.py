# models/ISFACT/SITE_model_ISFACT.py
#
# Modèle de SITE, ce modèle est un modèle de la base client épuréee
#
#
from app import db

class SITE_ISAFACT(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    Site_id = db.Column(db.String(20))
    Client_id = db.Column(db.String(20))
    CodeClient = db.Column(db.String(7))
    RefExterneISAFACT = db.Column(db.String(7))
    FamilleTIERS = db.Column(db.String(30))
    AdresseSite = db.Column(db.String(30))
    VilleSite = db.Column(db.String(30))
    CPSite = db.Column(db.String(5))
    CreatedAt = db.Column(db.DateTime())
    UpdatedAt = db.Column(db.DateTime())
    CreatedBy = db.Column(db.String(30))
    LastUpdatedBy = db.Column(db.String(30))
    
    def to_dict(self):
        return {
            'Site_id' : self.Site_id,
            'Client_id' : self.Client_id,
            'CodeClient' :self.CodeClient,
            'RefExterneISAFACT': self.RefExterneISAFACT,
            'FamilleTIERS' : self.FamilleTIERS,
            'AdresseSite' : self.AdresseSite,
            'VilleSite' : self.VilleSite,
            'CPSite' : self.CPSite,
            'CreatedAt' : self.CreatedAt,
            'UpdatedAt' : self.UpdatedAt,
            'CreatedBy' : self.CreatedBy,
            'LastUpdatedBy': self.LastUpdatedBy
        }
    
