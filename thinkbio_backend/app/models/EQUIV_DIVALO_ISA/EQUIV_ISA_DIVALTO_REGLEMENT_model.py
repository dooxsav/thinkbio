# models/equiv_divalto_isa
#

from app import db
from datetime import datetime

class EQUIV_MODE_RGLT_ISA_DIV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code_ISA = db.Column(db.String(10))
    code_Divalto = db.Column(db.String(10))
    libelle_code_rglt = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'code_ISA': self.code_ISA,
            'code_Divalto': self.code_Divalto,
            'libelle_code_rglt': self.libelle_code_rglt,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

        