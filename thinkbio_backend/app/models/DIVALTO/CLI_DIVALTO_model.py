# models/DIVALTO/CLI_DIVALTO_model.py
# Table DIVALTO

from app import db

class Client_DIVALTO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DOSSIER=db.Column(db.String(10), nullable=True) 
    TIERS=db.Column(db.String(10), nullable=True) 
    CONF=db.Column(db.String(10), nullable=True) 
    VISA=db.Column(db.Integer(), nullable=True)
    NOMABREGE=db.Column(db.String(100), nullable=True) 
    NOM_CLIENT=db.Column(db.String(100), nullable=True) 
    ADRCPL1=db.Column(db.String(100), nullable=True) 
    ADRCPL2=db.Column(db.String(100), nullable=True) 
    RUE=db.Column(db.String(100), nullable=True) 
    LOCALITE=db.Column(db.String(100), nullable=True) 
    VILLE=db.Column(db.String(100), nullable=True) 
    PAYS=db.Column(db.String(100), nullable=True) 
    CODEPOSTAL=db.Column(db.String(10), nullable=True) 
    ZIPCOD=db.Column(db.String(100), nullable=True) 
    REGIONADMINISTRATIVE=db.Column(db.String(100), nullable=True) 
    CODEINSEE=db.Column(db.String(100), nullable=True) 
    LATITUDE=db.Column(db.String(100), nullable=True) 
    LONGITUDE=db.Column(db.String(100), nullable=True) 
    TEL=db.Column(db.String(20), nullable=True) 
    FAX=db.Column(db.String(20), nullable=True) 
    ADRESSEWEB=db.Column(db.String(100), nullable=True) 
    EMAIL=db.Column(db.String(100), nullable=True) 
    NAF=db.Column(db.String(100), nullable=True) 
    TITRE=db.Column(db.String(100), nullable=True) 
    MODEREGL=db.Column(db.String(100), nullable=True) 
    DEVISE=db.Column(db.String(100), nullable=True) 
    LANGUE=db.Column(db.String(100), nullable=True) 
    COMPTE=db.Column(db.String(100), nullable=True) 
    COMPTEMASQUE=db.Column(db.String(100), nullable=True) 
    CRITERESELECTION=db.Column(db.String(100), nullable=True) 
    SIRET=db.Column(db.String(100), nullable=True) 
    ETABLISSEMENT=db.Column(db.String(100), nullable=True) 
    DATEFINVALID=db.Column(db.Date(), nullable=True) 
    NUMERONOTE=db.Column(db.String(100), nullable=True) 
    JOINT=db.Column(db.String(100), nullable=True) 
    IDCONNECT=db.Column(db.String(100), nullable=True) 
    CALENDRIER=db.Column(db.String(100), nullable=True) 
    GLN=db.Column(db.String(100), nullable=True) 
    TELCLE=db.Column(db.String(100), nullable=True) 
    ICPFL=db.Column(db.String(100), nullable=True) 
    CATEGORIEPIECE=db.Column(db.String(100), nullable=True) 
    TAGS=db.Column(db.String(100), nullable=True) 
    CODETARIF=db.Column(db.String(100), nullable=True) 
    CODEREMISE=db.Column(db.String(100), nullable=True) 
    CODETARIFPROMOTION=db.Column(db.String(100), nullable=True) 
    CODEREMISEPROMOTION=db.Column(db.String(100), nullable=True) 
    FAMILLETARIFCLIENT=db.Column(db.String(100), nullable=True) 
    FAMILLETARIFEXCEPTIONCLIENT=db.Column(db.String(100), nullable=True) 
    CLASSEREMISECLIENT=db.Column(db.String(100), nullable=True) 
    CLASSEREMISEEXCEPTIONCLIENT=db.Column(db.String(100), nullable=True) 
    REMISE1=db.Column(db.String(100), nullable=True) 
    REMISE2=db.Column(db.String(100), nullable=True) 
    REMISE3=db.Column(db.String(100), nullable=True) 
    TYPEREMISE1=db.Column(db.Integer(), nullable=True) 
    TYPEREMISE2=db.Column(db.Integer(), nullable=True) 
    TYPEREMISE3=db.Column(db.Integer(), nullable=True) 
    DATEDEROPERATION=db.Column(db.DateTime(), nullable=True)
    NBEX1=db.Column(db.String(100), nullable=True) 
    NBEX2=db.Column(db.String(100), nullable=True) 
    NBEX3=db.Column(db.String(100), nullable=True) 
    NBEX4=db.Column(db.String(100), nullable=True) 
    EDITTYP1=db.Column(db.Integer(), nullable=True) 
    EDITTYP2=db.Column(db.Integer(), nullable=True) 
    EDITTYP3=db.Column(db.Integer(), nullable=True) 
    EDITTYP4=db.Column(db.Integer(), nullable=True) 
    ETANO1=db.Column(db.String(100), nullable=True) 
    ETANO2=db.Column(db.String(100), nullable=True) 
    ETANO3=db.Column(db.String(100), nullable=True) 
    ETANO4=db.Column(db.String(100), nullable=True) 
    AXEMASQUE=db.Column(db.String(100), nullable=True) 
    AXENO=db.Column(db.Integer(), nullable=True) 
    STLGTGAMCOD=db.Column(db.Integer(), nullable=True) 
    WMAUDITFL=db.Column(db.Integer(), nullable=True) 
    WMDOCEMP=db.Column(db.String(100), nullable=True) 
    WMRESAIMPFL=db.Column(db.String(100), nullable=True) 
    PLANTRANSPORT=db.Column(db.String(100), nullable=True) 
    TXTPREENREG1=db.Column(db.String(100), nullable=True) 
    TXTPREENREG2=db.Column(db.String(100), nullable=True) 
    TXTPREENREG3=db.Column(db.String(100), nullable=True) 
    TXTPREENREG4=db.Column(db.String(100), nullable=True) 
    TXTPREENREG5=db.Column(db.String(100), nullable=True) 
    TXTPREENREG6=db.Column(db.String(100), nullable=True) 
    TXTPREENREG7=db.Column(db.String(100), nullable=True) 
    TXTPREENREG8=db.Column(db.String(100), nullable=True) 
    AFFCLDCOD=db.Column(db.String(100), nullable=True) 
    IDENTITEEXT=db.Column(db.String(100), nullable=True) 
    CONTACTTIERS=db.Column(db.String(100), nullable=True) 
    CODESTAT1=db.Column(db.String(100), nullable=True) 
    CODESTAT2=db.Column(db.String(100), nullable=True) 
    CODESTAT3=db.Column(db.String(100), nullable=True) 
    REGIMETPF=db.Column(db.String(100), nullable=True) 
    GROUPEMENT=db.Column(db.String(100), nullable=True) 
    LIBREA=db.Column(db.String(100), nullable=True) 
    CA=db.Column(db.String(100), nullable=True) 
    NBRESALARIE=db.Column(db.String(100), nullable=True) 
    ENCOURSMAXI1=db.Column(db.String(100), nullable=True) 
    ENCOURSMAXI2=db.Column(db.String(100), nullable=True) 
    TXESC=db.Column(db.String(100), nullable=True) 
    TXACOMPTE=db.Column(db.String(100), nullable=True) 
    LIBREN=db.Column(db.String(100), nullable=True) 
    REGTVATIERS=db.Column(db.String(100), nullable=True) 
    GROUPE1LIB=db.Column(db.String(100), nullable=True)
    GROUPE2LIB=db.Column(db.String(100), nullable=True) 
    MEDIA=db.Column(db.String(100), nullable=True) 
    CGVTEXCOD=db.Column(db.String(100), nullable=True) 
    CODETARIFTTC=db.Column(db.String(100), nullable=True) 
    FAMILLECOMMCLIENT=db.Column(db.String(100), nullable=True) 
    NATURETIERS=db.Column(db.String(100), nullable=True) 
    ORIGINETIERS=db.Column(db.String(100), nullable=True) 
    COMMERCIAL1=db.Column(db.String(100), nullable=True) 
    COMMERCIAL2=db.Column(db.String(100), nullable=True) 
    COMMERCIAL3=db.Column(db.String(100), nullable=True) 
    TIERSADRESSE1=db.Column(db.String(100), nullable=True) 
    TIERSADRESSE2=db.Column(db.String(100), nullable=True) 
    TIERSADRESSE3=db.Column(db.String(100), nullable=True) 
    TIERSADRESSE4=db.Column(db.String(100), nullable=True) 
    TIERSADRESSE5=db.Column(db.String(100), nullable=True) 
    CODEADRESSE1=db.Column(db.String(100), nullable=True) 
    CODEADRESSE2=db.Column(db.String(100), nullable=True) 
    CODEADRESSE3=db.Column(db.String(100), nullable=True) 
    CODEADRESSE4=db.Column(db.String(100), nullable=True) 
    CODEADRESSE5=db.Column(db.String(100), nullable=True) 
    TIERSSTAT=db.Column(db.String(100), nullable=True) 
    TIERSDIVALTOREGLT=db.Column(db.String(100), nullable=True) 
    RELIQUATGERE1=db.Column(db.String(100), nullable=True) 
    RELIQUATGERE2=db.Column(db.String(100), nullable=True) 
    RELIQUATGERE3=db.Column(db.String(100), nullable=True) 
    MODETRANSP=db.Column(db.String(100), nullable=True) 
    DEBIDENT=db.Column(db.String(100), nullable=True) 
    DEBPAYSIDENT=db.Column(db.String(100), nullable=True) 
    DEBCOEFTRANSP=db.Column(db.String(100), nullable=True) 
    DEBINCOTERM3=db.Column(db.String(100), nullable=True) 
    MTFRANCHISETVA=db.Column(db.String(100), nullable=True) 
    NBREJOURTRANSP=db.Column(db.String(100), nullable=True) 
    RFCCTRCOD=db.Column(db.String(100), nullable=True) 
    PROTOCOL=db.Column(db.String(100), nullable=True) 
    TIERSEXTERNE=db.Column(db.String(100), nullable=True) 
    FEU=db.Column(db.String(100), nullable=True) 
    RELIQUATLIGNE=db.Column(db.String(100), nullable=True) 
    VALLIGCOD=db.Column(db.String(100), nullable=True) 
    DEMATERIALISATIONTYPE=db.Column(db.String(100), nullable=True) 
    TYPEUNITE=db.Column(db.String(100), nullable=True) 
    MODEEXP=db.Column(db.String(100), nullable=True) 
    CONDEXP=db.Column(db.String(100), nullable=True) 
    DATEDEROPERATION=db.Column(db.Date(), nullable=True)
    CODEAGENCE=db.Column(db.String(100), nullable=True) 
    CRMUPDATEDH = db.Column(db.String(100), nullable=True) 
    FAMILLERELANCE=db.Column(db.String(100), nullable=True) 
    TIERSRELANCE=db.Column(db.String(100), nullable=True) 
    MODEFACTURE=db.Column(db.String(100), nullable=True) 
    PERIODEFACTURE=db.Column(db.String(100), nullable=True) 
    TOURNEE=db.Column(db.String(100), nullable=True) 
    RANGTOURNEE=db.Column(db.String(100), nullable=True) 
    JOURBL=db.Column(db.Date(), nullable=True) 
    CODEADV=db.Column(db.String(100), nullable=True) 
    PRIORITE=db.Column(db.String(100), nullable=True) 
    INDICCDEWEB=db.Column(db.String(100), nullable=True) 
    BPBASCOD=db.Column(db.String(100), nullable=True) 
    BPRUPTCOD=db.Column(db.String(100), nullable=True) 
    BLGENCOD=db.Column(db.String(100), nullable=True) 
    BPRELCOD=db.Column(db.String(100), nullable=True) 
    MTFANCO=db.Column(db.String(100), nullable=True) 
    TYPEBASEFRANCO=db.Column(db.String(100), nullable=True) 
    COEFFPOINT=db.Column(db.String(100), nullable=True) 
    NBPASSAGE=db.Column(db.String(100), nullable=True) 
    NBPOINT=db.Column(db.String(100), nullable=True) 
    CDLET=db.Column(db.String(100), nullable=True) 
    NUMCARTE=db.Column(db.String(100), nullable=True) 
    PANNO=db.Column(db.String(100), nullable=True) 
    BQEV=db.Column(db.String(100), nullable=True) 
    WMPREPMAX=db.Column(db.String(100), nullable=True) 
    RETNAT=db.Column(db.String(100), nullable=True) 
    IDCLIENT=db.Column(db.String(100), nullable=True) 
    CARTENO=db.Column(db.String(100), nullable=True) 
    TRANSICOD=db.Column(db.String(100), nullable=True) 
    LIEUINCOTERM=db.Column(db.String(100), nullable=True) 
    CATCLICOD=db.Column(db.String(100), nullable=True) 
    SOURCE=db.Column(db.String(100), nullable=True) 
    SYSTEME=db.Column(db.String(100), nullable=True) 
    DOSEXTERNE=db.Column(db.String(100), nullable=True) 
    ETBEXTERNE=db.Column(db.String(100), nullable=True) 
    FOURNISSEUR=db.Column(db.String(100), nullable=True) 
    IMPLSTCOL=db.Column(db.String(100), nullable=True) 
    BPSILIGCOMPLETE=db.Column(db.String(100), nullable=True) 
    CLASCODTAR=db.Column(db.String(100), nullable=True) 
    PIREFOBLIG=db.Column(db.String(100), nullable=True) 
    PCEPIREFOBLPICOD1=db.Column(db.String(100), nullable=True) 
    PCEPIREFOBLPICOD2=db.Column(db.String(100), nullable=True) 
    PCEPIREFOBLPICOD3=db.Column(db.String(100), nullable=True) 
    PCEPIREFOBLPICOD4=db.Column(db.String(100), nullable=True) 
    CTRLREFPIECE=db.Column(db.String(100), nullable=True) 
    TYPEETATDST=db.Column(db.String(100), nullable=True) 
    MOTIFCHGTETAT=db.Column(db.String(100), nullable=True) 
    CGVIMPTYP=db.Column(db.String(100), nullable=True) 
    PCEPIREFPINOOBL=db.Column(db.String(100), nullable=True) 
    PCEPIREFPINOCTRL=db.Column(db.String(100), nullable=True) 
    AGENTRECOUVR=db.Column(db.String(100), nullable=True) 
    CIRCUITVALIDATIONBLFL=db.Column(db.String(100), nullable=True) 
    CIRCUITVALIDATIONFCTFL=db.Column(db.String(100), nullable=True) 
    GENPIVOTPRERECEPCOD=db.Column(db.String(100), nullable=True) 
    PRERECEPACTIONCOD=db.Column(db.String(100), nullable=True) 
    ACPTIMPLICITE1=db.Column(db.String(100), nullable=True) 
    ACPTIMPLICITE2=db.Column(db.String(100), nullable=True) 
    ACPTIMPLICITE3=db.Column(db.String(100), nullable=True) 
    ACPTIMPLICITE4=db.Column(db.String(100), nullable=True) 
    ACPTIMPLICITE5=db.Column(db.String(100), nullable=True) 
    ACPTIMPLICITE6=db.Column(db.String(100), nullable=True) 
    ACPTBIENTX=db.Column(db.String(100), nullable=True) 
    ACPTSERVTX=db.Column(db.String(100), nullable=True) 
    ACPTTOTFLG=db.Column(db.String(100), nullable=True) 
    ACPTCTMFLG=db.Column(db.String(100), nullable=True) 
    ACPTEPHFLG=db.Column(db.String(100), nullable=True) 
    ACPTMTSEUIL=db.Column(db.String(100), nullable=True) 
    ACPTMTARR=db.Column(db.String(100), nullable=True) 
    CLASCODTX=db.Column(db.String(100), nullable=True)
    DUNS=db.Column(db.String(100), nullable=True)
    BLJRDEPART = db.Column(db.Date(), nullable=True) 
    
# __repr__: Cette méthode spéciale permet de définir une représentation en chaîne de caractères de l'objet. Dans cet exemple, il affiche l'identifiant de l'objet Client_ISFACT suivi du nom et prénom de la personne.
    def __repr__(self):
        return f"<Client_DIVALTO {self.id}: {self.DOSSIER} {self.TIERS} {self.NOM_CLIENT} {self.TIERSEXTERNE}>"

# to_dict(): Cette méthode convertit l'objet Client_ISFACT en un dictionnaire. Elle facilite la conversion de l'objet en un format plus facilement sérialisable, par exemple, pour le convertir en JSON.
    def to_dict(self):
        return {
            'id':self.id,
            'DOSSIER':self.DOSSIER,
            'TIERS':self.TIERS,
            'CONF':self.CONF,
            'VISA':self.VISA,
            'NOMABREGE':self.NOMABREGE,
            'NOM_CLIENT':self.NOM_CLIENT,
            'ADRCPL1':self.ADRCPL1,
            'ADRCPL2':self.ADRCPL2,
            'RUE':self.RUE,
            'LOCALITE':self.LOCALITE,
            'VILLE':self.VILLE,
            'PAYS':self.PAYS,
            'CODEPOSTAL':self.CODEPOSTAL,
            'ZIPCOD':self.ZIPCOD,
            'REGIONADMINISTRATIVE':self.REGIONADMINISTRATIVE,
            'CODEINSEE':self.CODEINSEE,
            'LATITUDE':self.LATITUDE,
            'LONGITUDE':self.LONGITUDE,
            'TEL':self.TEL,
            'FAX':self.FAX,
            'ADRESSEWEB':self.ADRESSEWEB,
            'EMAIL':self.EMAIL,
            'NAF':self.NAF,
            'TITRE':self.TITRE,
            'MODEREGL':self.MODEREGL,
            'DEVISE':self.DEVISE,
            'LANGUE':self.LANGUE,
            'COMPTE':self.COMPTE,
            'COMPTEMASQUE':self.COMPTEMASQUE,
            'CRITERESELECTION':self.CRITERESELECTION,
            'SIRET':self.SIRET,
            'ETABLISSEMENT':self.ETABLISSEMENT,
            'DATEFINVALID':self.DATEFINVALID,
            'NUMERONOTE':self.NUMERONOTE,
            'JOINT':self.JOINT,
            'IDCONNECT':self.IDCONNECT,
            'CALENDRIER':self.CALENDRIER,
            'GLN':self.GLN,
            'TELCLE':self.TELCLE,
            'ICPFL':self.ICPFL,
            'CATEGORIEPIECE':self.CATEGORIEPIECE,
            'TAGS':self.TAGS,
            'CODETARIF':self.CODETARIF,
            'CODEREMISE':self.CODEREMISE,
            'CODETARIFPROMOTION':self.CODETARIFPROMOTION,
            'CODEREMISEPROMOTION':self.CODEREMISEPROMOTION,
            'FAMILLETARIFCLIENT':self.FAMILLETARIFCLIENT,
            'FAMILLETARIFEXCEPTIONCLIENT':self.FAMILLETARIFEXCEPTIONCLIENT,
            'CLASSEREMISECLIENT':self.CLASSEREMISECLIENT,
            'CLASSEREMISEEXCEPTIONCLIENT':self.CLASSEREMISEEXCEPTIONCLIENT,
            'REMISE1':self.REMISE1,
            'REMISE2':self.REMISE2,
            'REMISE3':self.REMISE3,
            'TYPEREMISE1':self.TYPEREMISE1,
            'TYPEREMISE2':self.TYPEREMISE2,
            'TYPEREMISE3':self.TYPEREMISE3,
            'DATEDEROPERATION':self.DATEDEROPERATION,
            'NBEX1':self.NBEX1,
            'NBEX2':self.NBEX2,
            'NBEX3':self.NBEX3,
            'NBEX4':self.NBEX4,
            'EDITTYP1':self.EDITTYP1,
            'EDITTYP2':self.EDITTYP2,
            'EDITTYP3':self.EDITTYP3,
            'EDITTYP4':self.EDITTYP4,
            'ETANO1':self.ETANO1,
            'ETANO2':self.ETANO2,
            'ETANO3':self.ETANO3,
            'ETANO4':self.ETANO4,
            'AXEMASQUE':self.AXEMASQUE,
            'AXENO':self.AXENO,
            'STLGTGAMCOD':self.STLGTGAMCOD,
            'WMAUDITFL':self.WMAUDITFL,
            'WMDOCEMP':self.WMDOCEMP,
            'WMRESAIMPFL':self.WMRESAIMPFL,
            'PLANTRANSPORT':self.PLANTRANSPORT,
            'TXTPREENREG1':self.TXTPREENREG1,
            'TXTPREENREG2':self.TXTPREENREG2,
            'TXTPREENREG3':self.TXTPREENREG3,
            'TXTPREENREG4':self.TXTPREENREG4,
            'TXTPREENREG5':self.TXTPREENREG5,
            'TXTPREENREG6':self.TXTPREENREG6,
            'TXTPREENREG7':self.TXTPREENREG7,
            'TXTPREENREG8':self.TXTPREENREG8,
            'AFFCLDCOD':self.AFFCLDCOD,
            'IDENTITEEXT':self.IDENTITEEXT,
            'CONTACTTIERS':self.CONTACTTIERS,
            'CODESTAT1':self.CODESTAT1,
            'CODESTAT2':self.CODESTAT2,
            'CODESTAT3':self.CODESTAT3,
            'REGIMETPF':self.REGIMETPF,
            'GROUPEMENT':self.GROUPEMENT,
            'LIBREA':self.LIBREA,
            'CA':self.CA,
            'NBRESALARIE':self.NBRESALARIE,
            'ENCOURSMAXI1':self.ENCOURSMAXI1,
            'ENCOURSMAXI2':self.ENCOURSMAXI2,
            'TXESC':self.TXESC,
            'TXACOMPTE':self.TXACOMPTE,
            'LIBREN':self.LIBREN,
            'REGTVATIERS':self.REGTVATIERS,
            'GROUPE1LIB':self.GROUPE1LIB,
            'GROUPE2LIB':self.GROUPE2LIB,
            'MEDIA':self.MEDIA,
            'CGVTEXCOD':self.CGVTEXCOD,
            'CODETARIFTTC':self.CODETARIFTTC,
            'FAMILLECOMMCLIENT':self.FAMILLECOMMCLIENT,
            'NATURETIERS':self.NATURETIERS,
            'ORIGINETIERS':self.ORIGINETIERS,
            'COMMERCIAL1':self.COMMERCIAL1,
            'COMMERCIAL2':self.COMMERCIAL2,
            'COMMERCIAL3':self.COMMERCIAL3,
            'TIERSADRESSE1':self.TIERSADRESSE1,
            'TIERSADRESSE2':self.TIERSADRESSE2,
            'TIERSADRESSE3':self.TIERSADRESSE3,
            'TIERSADRESSE4':self.TIERSADRESSE4,
            'TIERSADRESSE5':self.TIERSADRESSE5,
            'CODEADRESSE1':self.CODEADRESSE1,
            'CODEADRESSE2':self.CODEADRESSE2,
            'CODEADRESSE3':self.CODEADRESSE3,
            'CODEADRESSE4':self.CODEADRESSE4,
            'CODEADRESSE5':self.CODEADRESSE5,
            'TIERSSTAT':self.TIERSSTAT,
            'TIERSDIVALTOREGLT':self.TIERSDIVALTOREGLT,
            'RELIQUATGERE1':self.RELIQUATGERE1,
            'RELIQUATGERE2':self.RELIQUATGERE2,
            'RELIQUATGERE3':self.RELIQUATGERE3,
            'MODETRANSP':self.MODETRANSP,
            'DEBIDENT':self.DEBIDENT,
            'DEBPAYSIDENT':self.DEBPAYSIDENT,
            'DEBCOEFTRANSP':self.DEBCOEFTRANSP,
            'DEBINCOTERM3':self.DEBINCOTERM3,
            'MTFRANCHISETVA':self.MTFRANCHISETVA,
            'NBREJOURTRANSP':self.NBREJOURTRANSP,
            'RFCCTRCOD':self.RFCCTRCOD,
            'PROTOCOL':self.PROTOCOL,
            'TIERSEXTERNE':self.TIERSEXTERNE,
            'FEU':self.FEU,
            'RELIQUATLIGNE':self.RELIQUATLIGNE,
            'VALLIGCOD':self.VALLIGCOD,
            'DEMATERIALISATIONTYPE':self.DEMATERIALISATIONTYPE,
            'TYPEUNITE':self.TYPEUNITE,
            'MODEEXP':self.MODEEXP,
            'CONDEXP':self.CONDEXP,
            'CRMUPDATEDH':self.CRMUPDATEDH,
            'CODEAGENCE':self.CODEAGENCE,
            'FAMILLERELANCE':self.FAMILLERELANCE,
            'TIERSRELANCE':self.TIERSRELANCE,
            'MODEFACTURE':self.MODEFACTURE,
            'PERIODEFACTURE':self.PERIODEFACTURE,
            'TOURNEE':self.TOURNEE,
            'RANGTOURNEE':self.RANGTOURNEE,
            'JOURBL':self.JOURBL,
            'CODEADV':self.CODEADV,
            'PRIORITE':self.PRIORITE,
            'INDICCDEWEB':self.INDICCDEWEB,
            'BPBASCOD':self.BPBASCOD,
            'BPRUPTCOD':self.BPRUPTCOD,
            'BLGENCOD':self.BLGENCOD,
            'BPRELCOD':self.BPRELCOD,
            'MTFANCO':self.MTFANCO,
            'TYPEBASEFRANCO':self.TYPEBASEFRANCO,
            'COEFFPOINT':self.COEFFPOINT,
            'NBPASSAGE':self.NBPASSAGE,
            'NBPOINT':self.NBPOINT,
            'CDLET':self.CDLET,
            'NUMCARTE':self.NUMCARTE,
            'PANNO':self.PANNO,
            'BQEV':self.BQEV,
            'WMPREPMAX':self.WMPREPMAX,
            'RETNAT':self.RETNAT,
            'IDCLIENT':self.IDCLIENT,
            'CARTENO':self.CARTENO,
            'TRANSICOD':self.TRANSICOD,
            'LIEUINCOTERM':self.LIEUINCOTERM,
            'CATCLICOD':self.CATCLICOD,
            'SOURCE':self.SOURCE,
            'SYSTEME':self.SYSTEME,
            'DOSEXTERNE':self.DOSEXTERNE,
            'ETBEXTERNE':self.ETBEXTERNE,
            'FOURNISSEUR':self.FOURNISSEUR,
            'IMPLSTCOL':self.IMPLSTCOL,
            'BPSILIGCOMPLETE':self.BPSILIGCOMPLETE,
            'CLASCODTAR':self.CLASCODTAR,
            'PIREFOBLIG':self.PIREFOBLIG,
            'PCEPIREFOBLPICOD1':self.PCEPIREFOBLPICOD1,
            'PCEPIREFOBLPICOD2':self.PCEPIREFOBLPICOD2,
            'PCEPIREFOBLPICOD3':self.PCEPIREFOBLPICOD3,
            'PCEPIREFOBLPICOD4':self.PCEPIREFOBLPICOD4,
            'CTRLREFPIECE':self.CTRLREFPIECE,
            'TYPEETATDST':self.TYPEETATDST,
            'MOTIFCHGTETAT':self.MOTIFCHGTETAT,
            'CGVIMPTYP':self.CGVIMPTYP,
            'PCEPIREFPINOOBL':self.PCEPIREFPINOOBL,
            'PCEPIREFPINOCTRL':self.PCEPIREFPINOCTRL,
            'AGENTRECOUVR':self.AGENTRECOUVR,
            'CIRCUITVALIDATIONBLFL':self.CIRCUITVALIDATIONBLFL,
            'CIRCUITVALIDATIONFCTFL':self.CIRCUITVALIDATIONFCTFL,
            'GENPIVOTPRERECEPCOD':self.GENPIVOTPRERECEPCOD,
            'PRERECEPACTIONCOD':self.PRERECEPACTIONCOD,
            'ACPTIMPLICITE1':self.ACPTIMPLICITE1,
            'ACPTIMPLICITE2':self.ACPTIMPLICITE2,
            'ACPTIMPLICITE3':self.ACPTIMPLICITE3,
            'ACPTIMPLICITE4':self.ACPTIMPLICITE4,
            'ACPTIMPLICITE5':self.ACPTIMPLICITE5,
            'ACPTIMPLICITE6':self.ACPTIMPLICITE6,
            'ACPTBIENTX':self.ACPTIMPLICITE2,
            'ACPTSERVTX':self.ACPTSERVTX,
            'ACPTTOTFLG':self.ACPTEPHFLG,
            'ACPTCTMFLG':self.ACPTCTMFLG,
            'ACPTEPHFLG':self.ACPTEPHFLG,
            'ACPTMTSEUIL':self.ACPTMTSEUIL,
            'ACPTMTARR':self.ACPTMTARR,
            'CLASCODTX':self.CLASCODTX,
            'DUNS':self.DUNS,
            'BLJRDEPART':self.BLJRDEPART
        }