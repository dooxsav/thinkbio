from app import db

class CONTRAT_MODEL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DOSSIER = db.Column(db.String(50))
    EQUIV_ISAFACT = db.Column(db.String(50))
    CODECONTRAT = db.Column(db.String(50))
    NUMERONOTE = db.Column(db.String(50))
    LIBELLE_CONTRAT_MODELE = db.Column(db.String(100))
    CODEOPERATION = db.Column(db.String(50))
    REFERENCE = db.Column(db.Integer)
    INDICEARTICLE = db.Column(db.String(50))
    SREFERENCE1 = db.Column(db.String(50))
    SREFERENCE2 = db.Column(db.String(50))
    CODETARIF = db.Column(db.Integer)
    CODETARIFTTC = db.Column(db.String(50))
    FACTUREMANUELLE = db.Column(db.Integer)
    AXE1 = db.Column(db.String(50))
    AXE2 = db.Column(db.String(50))
    AXE3 = db.Column(db.String(50))
    AXE4 = db.Column(db.String(50))
    MODECALCULMONTANT = db.Column(db.Integer)
    MONTANT = db.Column(db.Integer)
    TXTPREENREG = db.Column(db.String(50))
    TEXTETYP = db.Column(db.String(50))
    TYPECALENDRIERFACTURATION = db.Column(db.Integer)
    TAUXSURPRIXVENTE = db.Column(db.Integer)
    TAUX1SURPRIXVENTE = db.Column(db.String(50))
    INDICATEURSIREGROUPEMENT = db.Column(db.String(50))
    FACTURATIONCONDITIONNELLE = db.Column(db.Integer)
    TAFAMINTER = db.Column(db.Integer)
    TAFAMXINTER = db.Column(db.Integer)
    PROMOTACODINTER = db.Column(db.Integer)
    TACODINTER = db.Column(db.String(50))
    REFAMXINTER = db.Column(db.String(50))
    REFAMINTER = db.Column(db.Integer)
    PROMOREMCODINTER = db.Column(db.String(50))
    REMCODINTER = db.Column(db.Integer)
    REMINTER1 = db.Column(db.Integer)
    REMINTER2 = db.Column(db.Integer)
    REMINTER3 = db.Column(db.Integer)
    REMTYPINTER1 = db.Column(db.Integer)
    REMTYPINTER2 = db.Column(db.Integer)
    REMTYPINTER3 = db.Column(db.Integer)
    CODEINTERVENTION = db.Column(db.Integer)
    FAMODTYP = db.Column(db.Integer)
    CODECOMPTEUR = db.Column(db.Integer)
    CPTACTUFL = db.Column(db.Integer)
    MOINCLUFLG = db.Column(db.Integer)
    PCEINCLUFLG = db.Column(db.Integer)
    DEPINCLUFLG = db.Column(db.Integer)
    FADETAILTYP = db.Column(db.Integer)
    
    def to_dict(self):
        return{
            'id': self.id,
            'DOSSIER': self.DOSSIER,
            'EQUIV_ISAFACT': self.EQUIV_ISAFACT,
            'CODECONTRAT': self.CODECONTRAT,
            'NUMERONOTE': self.NUMERONOTE,
            'LIBELLE_CONTRAT_MODELE': self.LIBELLE_CONTRAT_MODELE,
            'CODEOPERATION': self.CODEOPERATION,
            'REFERENCE': self.REFERENCE,
            'INDICEARTICLE': self.INDICEARTICLE,
            'SREFERENCE1': self.SREFERENCE1,
            'SREFERENCE2': self.SREFERENCE2,
            'CODETARIF': self.CODETARIF,
            'CODETARIFTTC': self.CODETARIFTTC,
            'FACTUREMANUELLE': self.FACTUREMANUELLE,
            'AXE1': self.AXE1,
            'AXE2': self.AXE2,
            'AXE3': self.AXE3,
            'AXE4': self.AXE4,
            'MODECALCULMONTANT': self.MODECALCULMONTANT,
            'MONTANT': self.MONTANT,
            'TXTPREENREG': self.TXTPREENREG,
            'TEXTETYP': self.TEXTETYP,
            'TYPECALENDRIERFACTURATION': self.TYPECALENDRIERFACTURATION,
            'TAUXSURPRIXVENTE': self.TAUXSURPRIXVENTE,
            'TAUX1SURPRIXVENTE': self.TAUX1SURPRIXVENTE,
            'INDICATEURSIREGROUPEMENT': self.INDICATEURSIREGROUPEMENT,
            'FACTURATIONCONDITIONNELLE': self.FACTURATIONCONDITIONNELLE,
            'TAFAMINTER': self.TAFAMINTER,
            'TAFAMXINTER': self.TAFAMXINTER,
            'PROMOTACODINTER': self.PROMOTACODINTER,
            'TACODINTER': self.TACODINTER,
            'REFAMXINTER': self.REFAMXINTER,
            'REFAMINTER': self.REFAMINTER,
            'PROMOREMCODINTER': self.PROMOREMCODINTER,
            'REMCODINTER': self.REMCODINTER,
            'REMINTER1': self.REMINTER1,
            'REMINTER2': self.REMINTER2,
            'REMINTER3': self.REMINTER3,
            'REMTYPINTER1': self.REMTYPINTER1,
            'REMTYPINTER2': self.REMTYPINTER2,
            'REMTYPINTER3': self.REMTYPINTER3,
            'CODEINTERVENTION': self.CODEINTERVENTION,
            'FAMODTYP': self.FAMODTYP,
            'CODECOMPTEUR': self.CODECOMPTEUR,
            'CPTACTUFL': self.CPTACTUFL,
            'MOINCLUFLG': self.MOINCLUFLG,
            'PCEINCLUFLG': self.PCEINCLUFLG,
            'DEPINCLUFLG': self.DEPINCLUFLG,
            'FADETAILTYP': self.FADETAILTYP  
        }