# models/ISFACT/CLI_model_ISFACT.py
#
# Modèle de CLIENT, ce modèle est un modèle de la base client épuréee
#
#

from app import db

class CLI_ISFACT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Client_id = db.Column(db.String(20))
    CodeClient = db.Column(db.String(7))
    FamilleTIERS = db.Column(db.String(30))
    NomFACT = db.Column(db.String(30))
    PrenomFACT = db.Column(db.String(30))
    AdresseFACT = db.Column(db.String(100))
    CPFACT = db.Column(db.String(8))
    VilleFACT = db.Column(db.String(30))
    PaysFACT = db.Column(db.String(30))
    EmailTIERS = db.Column(db.String(90))
    Tel1 = db.Column(db.String(17))
    Tel2 = db.Column(db.String(17))
    Tel3 = db.Column(db.String(17))
    Mode_RGLT = db.Column(db.String(17))
    Axe_stat_1 = db.Column(db.String(17))
    Axe_stat_2 = db.Column(db.String(17))
    Axe_stat_3 = db.Column(db.String(17))
    createdAt = db.Column(db.DateTime())
    createdBy = db.Column(db.String(17))
    updatedAt = db.Column(db.DateTime())
    lastUpdatedBy = db.Column(db.String(17))
    
    def to_dict(self):
        return {
            'id': self.id,
            'Client_id': self.Client_id,
            'CodeClient': self.CodeClient,
            'FamilleTIERS': self.FamilleTIERS,
            'NomFACT': self.NomFACT,
            'PrenomFACT': self.PrenomFACT,
            'AdresseFACT': self.AdresseFACT,
            'CPFACT': self.CPFACT,
            'VilleFACT': self.VilleFACT,
            'PaysFACT': self.PaysFACT,
            'EmailTIERS': self.EmailTIERS,
            'Tel1': self.Tel1,
            'Tel2': self.Tel2,
            'Tel3': self.Tel3,
            'Mode_RGLT' : self.Mode_RGLT,
            'Axe_stat_1': self.Axe_stat_1,
            'Axe_stat_2': self.Axe_stat_2,
            'Axe_stat_3': self.Axe_stat_3,
            'createdAt': self.createdAt,
            'createdBy': self.createdBy,
            'updatedAt': self.updatedAt,
            'lastUpdatedBy': self.lastUpdatedBy,
        }