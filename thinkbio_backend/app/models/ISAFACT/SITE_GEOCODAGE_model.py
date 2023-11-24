from app import db
from datetime import datetime

class SITE_GEOCODAGE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Site_id = db.Column(db.String(20))
    Client_id = db.Column(db.String(20))
    CodeClient = db.Column(db.String(7))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    

    def to_dict(self):
        return {
            'id': self.id,
            'Site_id': self.Site_id,
            'Client_id': self.Client_id,
            'CodeClient': self.CodeClient,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

