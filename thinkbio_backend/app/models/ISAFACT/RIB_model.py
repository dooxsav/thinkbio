# models/ISFACT/CLI_model_ISFACT.py
#
# Modèle de CLIENT, ce modèle est un modèle de la base client épuréee
#
#

from app import db

class RIB_ISAFACT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Client_id = db.Column(db.String(20))
    CodeClient = db.Column(db.String(7))
    FamilleTIERS = db.Column(db.String(30))
    IBANPAYS = db.Column(db.String(2))
    IBANCLE = db.Column(db.String(2))
    IBANCOMPTE = db.Column(db.String(30))
    RIBBIC = db.Column(db.String(20))
    RIBDO = db.Column(db.String(50))
    
    def to_dict(self):
        return {
            'id': self.id,
            'Client_id': self.Client_id,
            'CodeClient': self.CodeClient,
            'FamilleTIERS': self.FamilleTIERS,
            'IBANPAYS': self.IBANPAYS,
            'IBANCLE': self.IBANCLE,
            'IBANCOMPTE': self.IBANCOMPTE,
            'RIBBIC': self.RIBBIC,
            'RIBDO': self.RIBDO
        }
