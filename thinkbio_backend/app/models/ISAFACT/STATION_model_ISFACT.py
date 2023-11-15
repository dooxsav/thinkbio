# models/ISFACT/SITE_model_ISFACT.py
#
# Modèle de SITE, ce modèle est un modèle de la base client épuréee
#
#
from app import db

class SITE_ISAFACT(db.Models): 
    id = db.Column(db.Integer, primary_key=True)
    CodeClient = db.Column(db.String(7))
    CodeClientDivalto = db.Column(db.String(10))
    FamilleTIERS = db.Column(db.String(30))
    AdresseSite = db.Column(db.String(30))
    VilleSite = db.Column(db.String(30))
    CPSite = db.Column(db.String(5))
