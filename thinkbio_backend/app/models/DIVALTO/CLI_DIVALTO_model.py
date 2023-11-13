# models/DIVALTO/CLI_DIVALTO_model.py
# Table DIVALTO

from app import db

class Client_DIVALTO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DOSSIER=db.Column(db.String(10))
    TIERS=db.Column(db.String(10))
    CONF=db.Column(db.String(10))
    VISA=db.Column(db.String(10))
    NOMABREGE=db.Column(db.String(100))
    NOM_CLIENT=db.Column(db.String(100))
    ADRCPL1=db.Column(db.String(100))
    ADRCPL2=db.Column(db.String(100))
    RUE=db.Column(db.String(100))
    LOCALITE=db.Column(db.String(100))
    VILLE=db.Column(db.String(100))
    PAYS=db.Column(db.String(100))
    CODEPOSTAL=db.Column(db.String(10))
    ZIPCOD=db.Column(db.String(100))
    REGIONADMINISTRATIVE=db.Column(db.String(100))
    CODEINSEE=db.Column(db.String(100))
    LATITUDE=db.Column(db.String(100))
    LONGITUDE=db.Column(db.String(100))
    TEL=db.Column(db.String(20))
    FAX=db.Column(db.String(20))
    ADRESSEWEB=db.Column(db.String(100))
    EMAIL=db.Column(db.String(100))
    NAF=db.Column(db.String(100))
    TITRE=db.Column(db.String(100))
    MODEREGL=db.Column(db.String(100))
    DEVISE=db.Column(db.String(100))
    LANGUE=db.Column(db.String(100))
    COMPTE=db.Column(db.String(100))
    COMPTEMASQUE=db.Column(db.String(100))
    CRITERESELECTION=db.Column(db.String(100))
    SIRET=db.Column(db.String(100))
    ETABLISSEMENT=db.Column(db.String(100))
    DATEFINVALID=db.Column(db.String(100))
    NUMERONOTE=db.Column(db.String(100))
    JOINT=db.Column(db.String(100))
    IDCONNECT=db.Column(db.String(100))
    CALENDRIER=db.Column(db.String(100))
    GLN=db.Column(db.String(100))
    TELCLE=db.Column(db.String(100))
    ICPFL=db.Column(db.String(100))
    CATEGORIEPIECE=db.Column(db.String(100))
    TAGS=db.Column(db.String(100))
    CODETARIF=db.Column(db.String(100))
    CODEREMISE=db.Column(db.String(100))
    CODETARIFPROMOTION=db.Column(db.String(100))
    CODEREMISEPROMOTION=db.Column(db.String(100))
    FAMILLETARIFCLIENT=db.Column(db.String(100))
    FAMILLETARIFEXCEPTIONCLIENT=db.Column(db.String(100))
    CLASSEREMISECLIENT=db.Column(db.String(100))
    CLASSEREMISEEXCEPTIONCLIENT=db.Column(db.String(100))
    REMISE1=db.Column(db.String(100))
    REMISE2=db.Column(db.String(100))
    REMISE3=db.Column(db.String(100))
    TYPEREMISE1=db.Column(db.String(100))
    TYPEREMISE2=db.Column(db.String(100))
    TYPEREMISE3=db.Column(db.String(100))
    DATEDEROPERATION=db.Column(db.String(100))
    NBEX1=db.Column(db.String(100))	
    NBEX2=db.Column(db.String(100))
    NBEX3=db.Column(db.String(100))
    NBEX4=db.Column(db.String(100))
    EDITTYP1=db.Column(db.String(100))
    EDITTYP2=db.Column(db.String(100))
    EDITTYP3=db.Column(db.String(100))
    EDITTYP4=db.Column(db.String(100))
    ETANO1=db.Column(db.String(100))
    ETANO2=db.Column(db.String(100))
    ETANO3=db.Column(db.String(100))
    ETANO4=db.Column(db.String(100))
    AXEMASQUE=db.Column(db.String(100))
    AXENO=db.Column(db.String(100))
    STLGTGAMCOD=db.Column(db.String(100))
    WMAUDITFL=db.Column(db.String(100))
    WMDOCEMP=db.Column(db.String(100))
    WMRESAIMPFL=db.Column(db.String(100))
    PLANTRANSPORT=db.Column(db.String(100))
    TXTPREENREG1=db.Column(db.String(100))
    TXTPREENREG2=db.Column(db.String(100))
    TXTPREENREG3=db.Column(db.String(100))
    TXTPREENREG4=db.Column(db.String(100))
    TXTPREENREG5=db.Column(db.String(100))
    TXTPREENREG6=db.Column(db.String(100))
    TXTPREENREG7=db.Column(db.String(100))
    TXTPREENREG8=db.Column(db.String(100))
    AFFCLDCOD=db.Column(db.String(100))
    IDENTITEEXT=db.Column(db.String(100))
    CONTACTTIERS=db.Column(db.String(100))
    CODESTAT1=db.Column(db.String(100))
    CODESTAT2=db.Column(db.String(100))
    CODESTAT3=db.Column(db.String(100))
    REGIMETPF=db.Column(db.String(100))
    GROUPEMENT=db.Column(db.String(100))
    LIBREA=db.Column(db.String(100))
    CA=db.Column(db.String(100))
    NBRESALARIE=db.Column(db.String(100))
    ENCOURSMAXI1=db.Column(db.String(100))
    ENCOURSMAXI2=db.Column(db.String(100))
    TXESC=db.Column(db.String(100))
    TXACOMPTE=db.Column(db.String(100))
    LIBREN=db.Column(db.String(100))
    REGTVATIERS=db.Column(db.String(100))
    GROUPE1LIB=db.Column(db.String(100))
    GROUPE2LIB=db.Column(db.String(100))
    MEDIA=db.Column(db.String(100))
    CGVTEXCOD=db.Column(db.String(100))
    CODETARIFTTC=db.Column(db.String(100))
    FAMILLECOMMCLIENT=db.Column(db.String(100))
    NATURETIERS=db.Column(db.String(100))
    ORIGINETIERS=db.Column(db.String(100))
    COMMERCIAL1=db.Column(db.String(100))
    COMMERCIAL2=db.Column(db.String(100))
    COMMERCIAL3=db.Column(db.String(100))
    TIERSADRESSE1=db.Column(db.String(100))
    TIERSADRESSE2=db.Column(db.String(100))
    TIERSADRESSE3=db.Column(db.String(100))
    TIERSADRESSE4=db.Column(db.String(100))
    TIERSADRESSE5=db.Column(db.String(100))
    CODEADRESSE1=db.Column(db.String(100))
    CODEADRESSE2=db.Column(db.String(100))
    CODEADRESSE3=db.Column(db.String(100))
    CODEADRESSE4=db.Column(db.String(100))
    CODEADRESSE5=db.Column(db.String(100))
    TIERSSTAT=db.Column(db.String(100))
    TIERSDIVALTOREGLT=db.Column(db.String(100))
    RELIQUATGERE1=db.Column(db.String(100))
    RELIQUATGERE2=db.Column(db.String(100))
    RELIQUATGERE3=db.Column(db.String(100))
    MODETRANSP=db.Column(db.String(100))
    DEBIDENT=db.Column(db.String(100))
    DEBPAYSIDENT=db.Column(db.String(100))
    DEBCOEFTRANSP=db.Column(db.String(100))
    DEBINCOTERM3=db.Column(db.String(100))
    MTFRANCHISETVA=db.Column(db.String(100))
    NBREJOURTRANSP=db.Column(db.String(100))
    RFCCTRCOD=db.Column(db.String(100))
    PROTOCOL=db.Column(db.String(100))
    TIERSEXTERNE=db.Column(db.String(100))
    FEU=db.Column(db.String(100))
    RELIQUATLIGNE=db.Column(db.String(100))
    VALLIGCOD=db.Column(db.String(100))
    DEMATERIALISATIONTYPE=db.Column(db.String(100))
    TYPEUNITE=db.Column(db.String(100))
    MODEEXP=db.Column(db.String(100))
    CONDEXP=db.Column(db.String(100))
    CRMUPDATEDH=db.Column(db.String(100))
    CODEAGENCE=db.Column(db.String(100))
    FAMILLERELANCE=db.Column(db.String(100))
    TIERSRELANCE=db.Column(db.String(100))
    MODEFACTURE=db.Column(db.String(100))
    PERIODEFACTURE=db.Column(db.String(100))
    TOURNEE=db.Column(db.String(100))
    RANGTOURNEE=db.Column(db.String(100))
    JOURBL=db.Column(db.String(100))
    CODEADV=db.Column(db.String(100))
    PRIORITE=db.Column(db.String(100))
    INDICCDEWEB=db.Column(db.String(100))
    BPBASCOD=db.Column(db.String(100))
    BPRUPTCOD=db.Column(db.String(100))
    BLGENCOD=db.Column(db.String(100))
    BPRELCOD=db.Column(db.String(100))
    MTFANCO=db.Column(db.String(100))
    TYPEBASEFRANCO=db.Column(db.String(100))
    COEFFPOINT=db.Column(db.String(100))
    NBPASSAGE=db.Column(db.String(100))
    NBPOINT=db.Column(db.String(100))
    CDLET=db.Column(db.String(100))
    NUMCARTE=db.Column(db.String(100))
    PANNO=db.Column(db.String(100))
    BQEV=db.Column(db.String(100))
    WMPREPMAX=db.Column(db.String(100))
    RETNAT=db.Column(db.String(100))
    IDCLIENT=db.Column(db.String(100))
    CARTENO=db.Column(db.String(100))
    TRANSICOD=db.Column(db.String(100))
    LIEUINCOTERM=db.Column(db.String(100))
    CATCLICOD=db.Column(db.String(100))
    SOURCE=db.Column(db.String(100))
    SYSTEME=db.Column(db.String(100))
    DOSEXTERNE=db.Column(db.String(100))
    ETBEXTERNE=db.Column(db.String(100))
    FOURNISSEUR=db.Column(db.String(100))
    IMPLSTCOL=db.Column(db.String(100))
    BPSILIGCOMPLETE=db.Column(db.String(100))
    CLASCODTAR=db.Column(db.String(100))
    PIREFOBLIG=db.Column(db.String(100))
    PCEPIREFOBLPICOD1=db.Column(db.String(100))
    PCEPIREFOBLPICOD2=db.Column(db.String(100))
    PCEPIREFOBLPICOD3=db.Column(db.String(100))
    PCEPIREFOBLPICOD4=db.Column(db.String(100))
    CTRLREFPIECE=db.Column(db.String(100))
    TYPEETATDST=db.Column(db.String(100))
    MOTIFCHGTETAT=db.Column(db.String(100))
    CGVIMPTYP=db.Column(db.String(100))
    PCEPIREFPINOOBL=db.Column(db.String(100))
    PCEPIREFPINOCTRL=db.Column(db.String(100))
    AGENTRECOUVR=db.Column(db.String(100))
    CIRCUITVALIDATIONBLFL=db.Column(db.String(100))
    CIRCUITVALIDATIONFCTFL=db.Column(db.String(100))
    GENPIVOTPRERECEPCOD=db.Column(db.String(100))
    PRERECEPACTIONCOD=db.Column(db.String(100))
    ACPTIMPLICITE1=db.Column(db.String(100))
    ACPTIMPLICITE2=db.Column(db.String(100))
    ACPTIMPLICITE3=db.Column(db.String(100))
    ACPTIMPLICITE4=db.Column(db.String(100))
    ACPTIMPLICITE5=db.Column(db.String(100))
    ACPTIMPLICITE6=db.Column(db.String(100))
    ACPTBIENTX=db.Column(db.String(100))
    ACPTSERVTX=db.Column(db.String(100))
    ACPTTOTFLG=db.Column(db.String(100))
    ACPTCTMFLG=db.Column(db.String(100))
    ACPTEPHFLG=db.Column(db.String(100))
    ACPTMTSEUIL=db.Column(db.String(100))
    ACPTMTARR=db.Column(db.String(100))
    CLASCODTX=db.Column(db.String(100))
    DUNS=db.Column(db.String(100))
    BLJRDEPART=db.Column(db.String(100))
    
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
            'ACPTEPHFLG':self.ACPTEPHFL,
            'ACPTMTSEUIL':self.ACPTMTSEUIL,
            'ACPTMTARR':self.ACPTMTARR,
            'CLASCODTX':self.CLASCODTX,
            'DUNS':self.DUNS,
            'BLJRDEPART':self.BLJRDEPART
        }