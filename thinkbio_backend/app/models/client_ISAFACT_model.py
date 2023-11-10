# models/client_isafact_model.py

from app import db

class Client_ISAFACT(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    CodeClient = db.Column(db.String(7))
    FamilleTIERS = db.Column(db.String(30))
    NomFACT = db.Column(db.String(30))
    PrenomFACT = db.Column(db.String(30))
    AdresseFACT = db.Column(db.String(100))
    CPFACT = db.Column(db.String(8))
    VilleFACT = db.Column(db.String(30))
    PaysFACT = db.Column(db.String(30))
    EmailTIERS = db.Column(db.String(90))
    TelFACT1 = db.Column(db.String(17))
    TelFACT2 = db.Column(db.String(17))
    TelFACT3 = db.Column(db.String(17))
    NomLOC = db.Column(db.String(30))  # Correction ici
    PrenomLOC = db.Column(db.String(30))
    AdresseSITE = db.Column(db.String(100))
    CPSITE = db.Column(db.String(8))
    VilleSITE = db.Column(db.String(30))
    PaysSITE = db.Column(db.String(30))
    TelSITE1 = db.Column(db.String(17))
    TelSITE2 = db.Column(db.String(17))
    TelSITE3 = db.Column(db.String(17))
    Livrer_adresse_facturation = db.Column(db.String(4))  # Correction ici
    CodeTVA = db.Column(db.String(4))
    TVA = db.Column(db.String(30))
    CodeTypeCONTRAT = db.Column(db.String(5))
    CodeCONTRAT = db.Column(db.String(5))
    CategTARIF = db.Column(db.String(30))
    Mode_rglt = db.Column(db.String(30))  # Correction ici
    Delai_rglt = db.Column(db.String(30))  # Correction ici
    Date_creation_tiers = db.Column(db.String(30))
    StatusTiers = db.Column(db.String(30))
    NivRelanceTiers = db.Column(db.String(30))
    Nom_representant = db.Column(db.String(30))
    RIB_Domic = db.Column(db.String(100))
    RIB_Etabl = db.Column(db.String(5))
    RIB_IBAN = db.Column(db.String(34))
    RIB_Cle = db.Column(db.String(2))
    RIB_CodeBIC = db.Column(db.String(30))
    NEGOCE = db.Column(db.String(30))
    TP_nom = db.Column(db.String(30))
    TP_tel = db.Column(db.String(30))
    DateProchaineIntervention = db.Column(db.String(30))  # Correction ici
    DateMEPContrat = db.Column(db.String(30))
    Date_derniere_facture = db.Column(db.Date())
    CreatedAt = db.Column(db.DateTime())
    UpdatedAt = db.Column(db.DateTime())
    CreatedBy = db.Column(db.String(30))
    LastUpdatedBy = db.Column(db.String(30))
    
# __repr__: Cette méthode spéciale permet de définir une représentation en chaîne de caractères de l'objet. Dans cet exemple, il affiche l'identifiant de l'objet Client_ISFACT suivi du nom et prénom de la personne.
    def __repr__(self):
        return f"<Client_ISFACT {self.id}: {self.CodeClient} {self.NomFACT} {self.PrenomFACT} {self.CreatedBy}>"

# to_dict(): Cette méthode convertit l'objet Client_ISFACT en un dictionnaire. Elle facilite la conversion de l'objet en un format plus facilement sérialisable, par exemple, pour le convertir en JSON.
    def to_dict(self):
        return {
            'id': self.id,
            'CodeClient': self.CodeClient,
            'FamilleTIERS': self.FamilleTIERS,
            'NomFACT': self.NomFACT,
            'PrenomFACT': self.PrenomFACT,
            'AdresseFACT': self.AdresseFACT,
            'CPFACT': self.CPFACT,
            'VilleFACT': self.VilleFACT,
            'PaysFACT': self.PaysFACT,
            'EmailTIERS': self.EmailTIERS,
            'TelFACT1': self.TelFACT1,
            'TelFACT2': self.TelFACT2,
            'TelFACT3': self.TelFACT3,
            'NomLOC': self.NomLOC,
            'PrenomLOC': self.PrenomLOC,
            'AdresseSITE': self.AdresseSITE,
            'CPSITE': self.CPSITE,
            'VilleSITE': self.VilleSITE,
            'PaysSITE': self.PaysSITE,
            'TelSITE1': self.TelSITE1,
            'TelSITE2': self.TelSITE2,
            'TelSITE3': self.TelSITE3,
            'Livrer_adresse_facturation': self.Livrer_adresse_facturation,
            'CodeTVA': self.CodeTVA,
            'TVA': self.TVA,
            'CodeTypeCONTRAT' : self.CodeTypeCONTRAT,
            'CodeCONTRAT': self.CodeCONTRAT,
            'CategTARIF': self.CategTARIF,
            'Mode_rglt': self.Mode_rglt,
            'Delai_rglt': self.Delai_rglt,
            'Date_creation_tiers': self.Date_creation_tiers,
            'StatusTiers': self.StatusTiers,
            'NivRelanceTiers': self.NivRelanceTiers,
            'Nom_representant': self.Nom_representant,
            'RIB_Domic': self.RIB_Domic,
            'RIB_Etabl': self.RIB_Etabl,
            'RIB_IBAN': self.RIB_IBAN,
            'RIB_Cle': self.RIB_Cle,
            'RIB_CodeBIC': self.RIB_CodeBIC,
            'NEGOCE': self.NEGOCE,
            'TP_nom': self.TP_nom,
            'TP_tel': self.TP_tel,
            'DateProchaineIntervention': self.DateProchaineIntervention,
            'DateMEPContrat': self.DateMEPContrat,
            'Date_derniere_facture': self.Date_derniere_facture,
            'CreatedAt': self.CreatedAt,
            'UpdatedAt': self.UpdatedAt,
            'CreatedBy': self.CreatedBy,
            'LastUpdatedBy': self.LastUpdatedBy
        }

# from_dict(): Cette méthode statique crée une instance de Client_ISFACT à partir d'un dictionnaire. Elle permet de reconstruire un objet Client_ISFACT à partir d'un dictionnaire, ce qui peut être utile lors de la réception de données, par exemple d'un formulaire ou d'une requête JSON.
    @staticmethod
    def from_dict(data):
        return Client_ISAFACT(
            id=data.get('id'),
            CodeClient=data.get('CodeClient'),
            FamilleTIERS=data.get('FamilleTIERS'),
            NomFACT=data.get('NomFACT'),
            PrenomFACT=data.get('PrenomFACT'),
            AdresseFACT=data.get('AdresseFACT'),
            CPFACT=data.get('CPFACT'),
            VilleFACT=data.get('VilleFACT'),
            PaysFACT=data.get('PaysFACT'),
            EmailTIERS=data.get('EmailTIERS'),
            TelFACT1=data.get('TelFACT1'),
            TelFACT2=data.get('TelFACT2'),
            TelFACT3=data.get('TelFACT3'),
            NomLOC=data.get('NomLOC'),
            PrenomLOC=data.get('PrenomLOC'),
            AdresseSITE=data.get('AdresseSITE'),
            CPSITE=data.get('CPSITE'),
            VilleSITE=data.get('VilleSITE'),
            PaysSITE=data.get('PaysSITE'),
            TelSITE1=data.get('TelSITE1'),
            TelSITE2=data.get('TelSITE2'),
            TelSITE3=data.get('TelSITE3'),
            Livrer_adresse_facturation=data.get('Livrer_adresse_facturation'),
            CodeTVA=data.get('CodeTVA'),
            TVA=data.get('TVA'),
            CodeTypeCONTRAT= data.get('CodeTypeCONTRAT'),
            CodeCONTRAT=data.get('CodeCONTRAT'),
            CategTARIF=data.get('CategTARIF'),
            Mode_rglt=data.get('Mode_rglt'),
            Delai_rglt=data.get('Delai_rglt'),
            Date_creation_tiers=data.get('Date_creation_tiers'),
            StatusTiers=data.get('StatusTiers'),
            NivRelanceTiers=data.get('NivRelanceTiers'),
            Nom_representant=data.get('Nom_representant'),
            RIB_Domic=data.get('RIB_Domic'),
            RIB_Etabl=data.get('RIB_Etabl'),
            RIB_IBAN=data.get('RIB_IBAN'),
            RIB_Cle=data.get('RIB_Cle'),
            RIB_CodeBIC=data.get('RIB_CodeBIC'),
            NEGOCE=data.get('NEGOCE'),
            TP_nom=data.get('TP_nom'),
            TP_tel=data.get('TP_tel'),
            DateProchaineIntervention=data.get('DateProchaineIntervention'),
            DateMEPContrat=data.get('DateMEPContrat'),
            Date_derniere_facture= data.Date_derniere_facture,
            CreatedAt=data.get('CreatedAt'),
            UpdatedAt=data.get('UpdatedAt'),
            CreatedBy=data.get('CreatedBy'),
            LastUpdatedBy=data.get('LastUpdatedBy')
        )
        