from app import db

class SITUATION_ISAFACT(db.Model):
    __tablename__ = 'SITUATIONS'

    id = db.Column(db.Integer, primary_key=True)
    date_document = db.Column(db.Date)
    numero_document = db.Column(db.String(20))
    nom = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    CodeClient = db.Column(db.String(20))
    libelle_famille_tiers = db.Column(db.String(100))
    code_postal = db.Column(db.String(10))
    nom_representant = db.Column(db.String(100))
    code_article = db.Column(db.String(20))
    designation_courte_article = db.Column(db.String(100))
    code_lot_articles = db.Column(db.String(20))
    code_lot_facture = db.Column(db.String(20))
    libelle_lot_facture = db.Column(db.String(100))
    code_famille_article = db.Column(db.String(20))
    libelle_famille_article = db.Column(db.String(100))
    compte_de_vente = db.Column(db.String(20))
    quantite_unit = db.Column(db.Float)
    montant_HT = db.Column(db.Float)
    volume = db.Column(db.Integer)
    code_divers = db.Column(db.String(10))
    date_livraison_document = db.Column(db.Date)
    
    def __repr__(self):
        return f"<Document {self.numero_document}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'date_document': self.date_document.strftime('%d/%m/%Y') if self.date_document else None,
            'numero_document': self.numero_document,
            'nom': self.nom,
            'prenom': self.prenom,
            'CodeClient': self.code,
            'libelle_famille_tiers': self.libelle_famille_tiers,
            'code_postal': self.code_postal,
            'nom_representant': self.nom_representant,
            'code_article': self.code_article,
            'designation_courte_article': self.designation_courte_article,
            'code_lot_articles': self.code_lot_articles,
            'code_lot_facture': self.code_lot_facture,
            'libelle_lot_facture': self.libelle_lot_facture,
            'code_famille_article': self.code_famille_article,
            'libelle_famille_article': self.libelle_famille_article,
            'compte_de_vente': self.compte_de_vente,
            'quantite_unit': self.quantite_unit,
            'montant_HT': self.montant_HT,
            'volume': self.volume,
            'code_divers': self.code_divers,
            'date_livraison_document': self.date_livraison_document.strftime('%d/%m/%Y') if self.date_livraison_document else None
        }
