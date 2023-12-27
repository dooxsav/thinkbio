# service/DB_service
import csv
import re

from flask import jsonify	
from app import db
from app.models import Client, Geography, Client_ISAFACT, Client_DIVALTO
from app.utils import sanitarise_donnes_niveau1, convert_specific_to_date, clean_phone_number, extract_email
from tqdm import tqdm
from sqlalchemy.exc import IntegrityError

import pandas as pd
from datetime import datetime, date

## ------------------------------------------------------------------------------------------------------------------------------------------------ ##
## ------------------------------------------------------------** Methods **----------------------------------------------------------------------- ##
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##

def testServiceDB():
    return "DBService Work !"

def remove_special_characters(text):
    if text is None:  # Vérifier si la valeur est nulle
        return "NC"
    return re.sub(r'[^A-Za-z0-9\s]', '', text)

def check_email(email):
    if not email or email.isspace():  # Vérifie si l'e-mail est vide ou ne contient que des espaces
        return "email non communiqué"

    # Si l'e-mail contient un espace ou un caractère '/', on le divise en plusieurs adresses
    emails = re.split(r'\s+|/', email)
    
    valid_emails = []
    for mail in emails:
        # Vérification du modèle d'e-mail
        if re.match(r'^\S+@\S+\.\S+$', mail.strip()):
            valid_emails.append(mail.strip())
    
    if valid_emails:
        return ', '.join(valid_emails)  # Retourne les adresses valides séparées par une virgule
    else:
        return "email non communiqué"
    
def enregistrerFichier():
    return None

## ------------------------------------------------------------------------------------------------------------------------------------------------ ##
## ----------------------------------------------------** Table CLIENT DIVALTO **------------------------------------------------------------------ ##
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##

def Ecrire_MAJ_Clients_DIVALTO(file_path):
    # Initialisation
    lignes_ajoutees = 0
    ligne_modifies = 0

    
    try:
        # Lire le fichier Excel dans un DataFrame
        dataFrame = pd.read_excel(file_path, sheet_name='Client', skiprows=5)

        # Remplacer tous les NaN par None dans le DataFrame
        dataFrame = dataFrame.where(pd.notna(dataFrame), None)

        
        total_rows = len(dataFrame)
        # Itération sur le DF
        with tqdm(total=total_rows, desc="Importation en cours", unit=" lignes") as pbar:
            # Itération sur le DataFrame
            for index, row in dataFrame.iterrows():
                DOSSIER = str(row['DOSSIER'])
                TIERS = str(row["TIERS"])
                CONF = str(row["CONF"])
                VISA = str(row['VISA'])
                NOMABREGE = str(row['NOMABREGE'])
                NOM_CLIENT=str(row['NOM_CLIENT'])
                ADRCPL1=str(row['ADRCPL1'])
                ADRCPL2=str(row['ADRCPL2'])
                RUE = str(row['RUE'])
                LOCALITE = str(row['LOCALITE'])
                VILLE= str(row['VILLE'])
                PAYS = str(row['PAYS'])
                CODEPOSTAL = str(row['CODEPOSTAL'])
                ZIPCOD = str(row['ZIPCOD'])
                REGIONADMINISTRATIVE= str(row['REGIONADMINISTRATIVE'])
                CODEINSEE= str(row['CODEINSEE'])
                LATITUDE= str(row['LATITUDE'])
                LONGITUDE= str(row['LONGITUDE'])
                TEL = str(row['TEL'])
                FAX = str(row['FAX'])
                ADRESSEWEB= str(row['ADRESSEWEB'])
                EMAIL = str(row['EMAIL'])
                NAF = str(row['NAF'])
                TITRE = str(row['TITRE'])
                MODEREGL = str(row['MODEREGL'])
                DEVISE = str(row['DEVISE'])
                LANGUE = str(row['LANGUE'])
                COMPTE = str(row['COMPTE'])
                COMPTEMASQUE = str(row['COMPTEMASQUE'])
                CRITERESELECTION = str(row['CRITERESELECTION'])
                SIRET = str(row['SIRET'])
                ETABLISSEMENT = str(row['ETABLISSEMENT'])
                NUMERONOTE= str(row['NUMERONOTE'])
                JOINT= str(row['JOINT'])
                IDCONNECT= str(row['IDCONNECT'])
                CALENDRIER= str(row['CALENDRIER'])
                GLN= str(row['GLN'])
                TELCLE = str(row['TELCLE'])
                ICPFL = str(row['ICPFL'])
                CATEGORIEPIECE= str(row['CATEGORIEPIECE'])
                TAGS= str(row['TAGS'])
                CODETARIF= str(row['CODETARIF'])
                CODEREMISE= str(row['CODEREMISE'])
                CODETARIFPROMOTION= str(row['CODETARIFPROMOTION'])
                CODEREMISEPROMOTION= str(row['CODEREMISEPROMOTION'])
                FAMILLETARIFCLIENT= str(row['FAMILLETARIFCLIENT'])
                FAMILLETARIFEXCEPTIONCLIENT= str(row['FAMILLETARIFEXCEPTIONCLIENT'])
                CLASSEREMISECLIENT= str(row['CLASSEREMISECLIENT'])
                CLASSEREMISEEXCEPTIONCLIENT= str(row['CLASSEREMISEEXCEPTIONCLIENT'])
                REMISE1= str(row['REMISE(1)'])
                REMISE2	= str(row['REMISE(2)'])
                REMISE3= str(row['REMISE(3)'])                
                TYPEREMISE1 = str(row['TYPEREMISE(1)'])
                TYPEREMISE2 = str(row['TYPEREMISE(2)'])
                TYPEREMISE3 = str(row['TYPEREMISE(3)'])
                NBEX1= str(row['NBEX(1)']) 
                NBEX2= str(row['NBEX(2)']) 
                NBEX3= str(row['NBEX(3)']) 
                NBEX4= str(row['NBEX(4)']) 
                EDITTYP1 = str(row['EDITTYP(1)'])
                EDITTYP2 = str(row['EDITTYP(2)'])
                EDITTYP3 = str(row['EDITTYP(3)'])
                EDITTYP4 = str(row['EDITTYP(4)'])
                ETANO1= str(row['ETANO(1)'])
                ETANO2= str(row['ETANO(2)'])
                ETANO3= str(row['ETANO(3)'])
                ETANO4= str(row['ETANO(4)'])
                AXEMASQUE = str(row['AXEMASQUE'])
                AXENO = str(row['AXENO'])
                STLGTGAMCOD = str(row['STLGTGAMCOD'])
                WMAUDITFL = str(row['WMAUDITFL'])
                WMDOCEMP = str(row['WMDOCEMP'])
                WMRESAIMPFL = str(row['WMRESAIMPFL'])
                PLANTRANSPORT= str(row['PLANTRANSPORT'])
                TXTPREENREG1= str(row['TXTPREENREG(1)'])
                TXTPREENREG2= str(row['TXTPREENREG(2)'])	
                TXTPREENREG3= str(row['TXTPREENREG(3)'])	
                TXTPREENREG4= str(row['TXTPREENREG(4)'])	
                TXTPREENREG5= str(row['TXTPREENREG(5)'])	
                TXTPREENREG6= str(row['TXTPREENREG(6)'])	
                TXTPREENREG7= str(row['TXTPREENREG(7)'])	
                TXTPREENREG8= str(row['TXTPREENREG(8)'])	
                AFFCLDCOD= str(row['AFFCLDCOD'])	
                IDENTITEEXT= str(row['IDENTITEEXT'])
                CONTACTTIERS= str(row['CONTACTTIERS'])
                CODESTAT1= str(row['CODESTAT(1)'])	
                CODESTAT2= str(row['CODESTAT(2)'])	
                CODESTAT3= str(row['CODESTAT(3)'])	
                REGIMETPF= str(row['REGIMETPF'])	
                GROUPEMENT	= str(row['GROUPEMENT'])
                LIBREA = str(row['LIBREA'])
                CA = str(row['CA'])
                NBRESALARIE = str(row['NBRESALARIE'])
                ENCOURSMAXI1 = str(row['ENCOURSMAXI(1)'])
                ENCOURSMAXI2 = str(row['ENCOURSMAXI(2)'])	
                TXESC = str(row['TXESC'])
                TXACOMPTE = str(row['TXACOMPTE'])
                LIBREN = str(row['LIBREN'])
                REGTVATIERS = str(row['REGTVATIERS'])
                GROUPE1LIB = str(row['GROUPE1LIB'])
                GROUPE2LIB = str(row['GROUPE2LIB'])
                MEDIA = str(row['MEDIA'])
                CGVTEXCOD = str(row['CGVTEXCOD'])
                CODETARIFTTC  = str(row['CODETARIFTTC'])
                FAMILLECOMMCLIENT= str(row['FAMILLECOMMCLIENT'])
                NATURETIERS = str(row['NATURETIERS'])
                ORIGINETIERS= str(row['ORIGINETIERS'])
                COMMERCIAL1 = str(row['COMMERCIAL(1)'])
                COMMERCIAL2 = str(row['COMMERCIAL(2)'])
                COMMERCIAL3 = str(row['COMMERCIAL(3)'])
                TIERSADRESSE1 = str(row['TIERSADRESSE(1)'])
                TIERSADRESSE2 = str(row['TIERSADRESSE(2)'])
                TIERSADRESSE3 = str(row['TIERSADRESSE(3)'])
                TIERSADRESSE4 = str(row['TIERSADRESSE(4)'])
                TIERSADRESSE5 = str(row['TIERSADRESSE(5)'])
                CODEADRESSE1 = str(row['CODEADRESSE(1)'])
                CODEADRESSE2 = str(row['CODEADRESSE(2)'])
                CODEADRESSE3 = str(row['CODEADRESSE(3)'])
                CODEADRESSE4 = str(row['CODEADRESSE(4)'])
                CODEADRESSE5 = str(row['CODEADRESSE(5)'])
                TIERSSTAT = str(row['TIERSSTAT'])
                TIERSDIVALTOREGLT= str(row['TIERSDIVALTOREGLT'])
                RELIQUATGERE1 = str(row['RELIQUATGERE(1)'])
                RELIQUATGERE2 = str(row['RELIQUATGERE(2)'])
                RELIQUATGERE3 = str(row['RELIQUATGERE(3)'])
                MODETRANSP = str(row['MODETRANSP'])
                DEBIDENT = str(row['DEBIDENT'])
                DEBPAYSIDENT = str(row['DEBPAYSIDENT'])
                DEBCOEFTRANSP = str(row['DEBCOEFTRANSP'])
                DEBINCOTERM3 = str(row['DEBINCOTERM3'])
                MTFRANCHISETVA = str(row['MTFRANCHISETVA'])
                NBREJOURTRANSP = str(row['NBREJOURTRANSP'])
                RFCCTRCOD = str(row['RFCCTRCOD'])
                PROTOCOL= str(row['PROTOCOL'])
                TIERSEXTERNE = str(row['TIERSEXTERNE'])
                FEU = str(row['FEU'])
                RELIQUATLIGNE = str(row['RELIQUATLIGNE'])
                VALLIGCOD = str(row['VALLIGCOD'])
                DEMATERIALISATIONTYPE = str(row['DEMATERIALISATIONTYPE'])
                TYPEUNITE = str(row['TYPEUNITE'])
                MODEEXP = str(row['MODEEXP'])
                CONDEXP = str(row['CONDEXP'])
                CRMUPDATEDH = str(row['CRMUPDATEDH'])
                CODEAGENCE = str(row['CODEAGENCE'])
                FAMILLERELANCE = str(row['FAMILLERELANCE'])
                TIERSRELANCE = str(row['TIERSRELANCE'])
                MODEFACTURE = str(row['MODEFACTURE'])
                PERIODEFACTURE = str(row['PERIODEFACTURE'])
                TOURNEE = str(row['TOURNEE'])
                RANGTOURNEE = str(row['RANGTOURNEE'])
                CODEADV = str(row['CODEADV'])
                PRIORITE = str(row['PRIORITE'])
                INDICCDEWEB = str(row['INDICCDEWEB'])
                BPBASCOD = str(row['BPBASCOD'])
                BPRUPTCOD = str(row['BPRUPTCOD'])
                BLGENCOD = str(row['BLGENCOD'])
                BPRELCOD = str(row['BPRELCOD'])
                MTFANCO = str(row['MTFANCO'])
                TYPEBASEFRANCO = str(row['TYPEBASEFRANCO'])
                COEFFPOINT = str(row['COEFFPOINT'])
                NBPASSAGE = str(row['NBPASSAGE']) 
                NBPOINT = str(row['NBPOINT']) 
                CDLET = str(row['CDLET'])
                NUMCARTE = str(row['NUMCARTE'])
                PANNO = str(row['PANNO'])
                BQEV = str(row['BQEV'])
                WMPREPMAX = str(row['WMPREPMAX'])
                RETNAT = str(row['RETNAT'])
                IDCLIENT = str(row['IDCLIENT'])
                CARTENO = str(row['CARTENO'])
                TRANSICOD = str(row['TRANSICOD'])
                LIEUINCOTERM = str(row['LIEUINCOTERM'])
                CATCLICOD = str(row['CATCLICOD'])
                SOURCE = str(row['SOURCE'])
                SYSTEME = str(row['SYSTEME'])
                DOSEXTERNE = str(row['DOSEXTERNE'])
                ETBEXTERNE = str(row['ETBEXTERNE'])
                FOURNISSEUR = str(row['FOURNISSEUR'])
                IMPLSTCOL = str(row['IMPLSTCOL'])
                BPSILIGCOMPLETE = str(row['BPSILIGCOMPLETE'])
                CLASCODTAR= str(row['CLASCODTAR'])
                PIREFOBLIG = str(row['PIREFOBLIG'])
                PCEPIREFOBLPICOD1 = str(row['PCEPIREFOBLPICOD(1)'])
                PCEPIREFOBLPICOD2 = str(row['PCEPIREFOBLPICOD(2)'])
                PCEPIREFOBLPICOD3 = str(row['PCEPIREFOBLPICOD(3)'])
                PCEPIREFOBLPICOD4 = str(row['PCEPIREFOBLPICOD(4)'])
                CTRLREFPIECE = str(row['CTRLREFPIECE'])
                TYPEETATDST = str(row['TYPEETATDST'])
                MOTIFCHGTETAT= str(row['MOTIFCHGTETAT'])
                CGVIMPTYP = str(row['CGVIMPTYP'])
                PCEPIREFPINOOBL = str(row['PCEPIREFPINOOBL'])
                PCEPIREFPINOCTRL = str(row['PCEPIREFPINOCTRL'])
                AGENTRECOUVR = str(row['AGENTRECOUVR'])
                CIRCUITVALIDATIONBLFL = str(row['CIRCUITVALIDATIONBLFL'])
                CIRCUITVALIDATIONFCTFL = str(row['CIRCUITVALIDATIONFCTFL'])
                GENPIVOTPRERECEPCOD = str(row['GENPIVOTPRERECEPCOD'])
                PRERECEPACTIONCOD = str(row['PRERECEPACTIONCOD']) 
                ACPTIMPLICITE1 = str(row['ACPTIMPLICITE(1)'])
                ACPTIMPLICITE2 = str(row['ACPTIMPLICITE(2)'])
                ACPTIMPLICITE3 = str(row['ACPTIMPLICITE(3)'])
                ACPTIMPLICITE4 = str(row['ACPTIMPLICITE(4)'])
                ACPTIMPLICITE5 = str(row['ACPTIMPLICITE(5)'])
                ACPTIMPLICITE6 = str(row['ACPTIMPLICITE(6)'])
                ACPTBIENTX = str(row['ACPTBIENTX'])
                ACPTSERVTX = str(row['ACPTSERVTX'])
                ACPTTOTFLG = str(row['ACPTTOTFLG'])
                ACPTCTMFLG = str(row['ACPTCTMFLG'])
                ACPTEPHFLG = str(row['ACPTEPHFLG'])
                ACPTMTSEUIL = str(row['ACPTMTSEUIL'])
                ACPTMTARR = str(row['ACPTMTARR'])
                CLASCODTX = str(row['CLASCODTX'])
                DUNS = str(row['DUNS'])

                if pd.notna(row['DATEDEROPERATION']) and row['DATEDEROPERATION'] != '0.0' and row['DATEDEROPERATION'] != 0:
                    DATEDEROPERATION = datetime.strptime(str(row['DATEDEROPERATION']), '%Y-%m-%d %H:%M:%S').date()
                else:
                    DATEDEROPERATION = date(1900, 1, 1)


                if pd.notna(row['BLJRDEPART']) and row['BLJRDEPART'] != '0.0' and row['BLJRDEPART'] != 0:
                    BLJRDEPART = datetime.strptime(str(row['BLJRDEPART']), '%d/%m/%Y').date()
                else:
                    BLJRDEPART = date(1900, 1, 1)
                    

                if pd.notna(row['DATEFINVALID']) and row['DATEFINVALID'] != '0.0' and row['DATEFINVALID'] != 0:
                    DATEFINVALID = datetime.strptime(str(row['DATEFINVALID']), '%d/%m/%Y').date()
                else:
                    DATEFINVALID = date(1900, 1, 1)
                    
                if pd.notna(row['JOURBL']) and row['JOURBL'] != '0.0' and row['JOURBL'] != 0:
                    JOURBL = datetime.strptime(str(row['JOURBL']), '%d/%m/%Y').date()
                else:
                    JOURBL = date(1900, 1, 1)
                # Controle présence de l'enregistrement, si présent => UPDATE sinon CREATE
                
                existing_record = Client_DIVALTO.query.filter_by(TIERS=TIERS).first()
                if existing_record:
                    existing_record.DOSSIER = DOSSIER
                    existing_record.CONF = CONF
                    existing_record.TIERS = TIERS
                    existing_record.VISA = VISA
                    existing_record.NOMABREGE = NOMABREGE
                    existing_record.NOM_CLIENT = NOM_CLIENT
                    existing_record.ADRCPL1 = ADRCPL1
                    existing_record.ADRCPL2= ADRCPL2
                    existing_record.RUE = RUE
                    existing_record.LOCALITE = LOCALITE
                    existing_record.VILLE = VILLE
                    existing_record.PAYS = PAYS
                    existing_record.CODEPOSTAL = CODEPOSTAL
                    existing_record.ZIPCOD = ZIPCOD
                    existing_record.REGIONADMINISTRATIVE = REGIONADMINISTRATIVE
                    existing_record.CODEINSEE = CODEINSEE
                    existing_record.LATITUDE = LATITUDE
                    existing_record.LONGITUDE = LONGITUDE
                    existing_record.TEL = TEL
                    existing_record.FAX = FAX
                    existing_record.ADRESSEWEB= ADRESSEWEB
                    existing_record.EMAIL = EMAIL
                    existing_record.NAF = NAF
                    existing_record.TITRE = TITRE
                    existing_record.MODEREGL = MODEREGL
                    existing_record.DEVISE = DEVISE
                    existing_record.LANGUE = LANGUE
                    existing_record.COMPTE = COMPTE
                    existing_record.COMPTEMASQUE = COMPTEMASQUE
                    existing_record.CRITERESELECTION = CRITERESELECTION
                    existing_record.SIRET = SIRET
                    existing_record.ETABLISSEMENT =  ETABLISSEMENT
                    existing_record.DATEFINVALID = DATEFINVALID
                    existing_record.NUMERONOTE=NUMERONOTE
                    existing_record.JOINT= JOINT
                    existing_record.IDCONNECT=IDCONNECT
                    existing_record.CALENDRIER=CALENDRIER
                    existing_record.GLN=GLN
                    existing_record.TELCLE=TELCLE
                    existing_record.ICPFL=ICPFL
                    existing_record.CATEGORIEPIECE=CATEGORIEPIECE
                    existing_record.TAGS= TAGS
                    existing_record.CODETARIF= CODETARIF
                    existing_record.CODEREMISE= CODEREMISE
                    existing_record.CODETARIFPROMOTION = CODETARIFPROMOTION
                    existing_record.CODEREMISEPROMOTION = CODEREMISEPROMOTION
                    existing_record.FAMILLETARIFCLIENT = FAMILLETARIFCLIENT
                    existing_record.FAMILLETARIFEXCEPTIONCLIENT = FAMILLETARIFEXCEPTIONCLIENT
                    existing_record.CLASSEREMISECLIENT = CLASSEREMISECLIENT
                    existing_record.CLASSEREMISEEXCEPTIONCLIENT = CLASSEREMISEEXCEPTIONCLIENT
                    existing_record.REMISE1 = REMISE1
                    existing_record.REMISE2	= REMISE2
                    existing_record.REMISE3 =   REMISE3           
                    existing_record.TYPEREMISE1 = TYPEREMISE1
                    existing_record.TYPEREMISE2 = TYPEREMISE2
                    existing_record.TYPEREMISE3 = TYPEREMISE3
                    existing_record.DATEDEROPERATION = DATEDEROPERATION
                    existing_record.NBEX1 = NBEX1
                    existing_record.NBEX2 =  NBEX2
                    existing_record.NBEX3 = NBEX3
                    existing_record.NBEX4  = NBEX4
                    existing_record.EDITTYP1 = EDITTYP1
                    existing_record.EDITTYP2 = EDITTYP2
                    existing_record.EDITTYP3 = EDITTYP3
                    existing_record.EDITTYP4 = EDITTYP4
                    existing_record.ETANO1= ETANO1
                    existing_record.ETANO2= ETANO2
                    existing_record.ETANO3= ETANO3
                    existing_record.ETANO4= ETANO4
                    existing_record.AXEMASQUE = AXEMASQUE
                    existing_record.AXENO = AXENO
                    existing_record.STLGTGAMCOD = STLGTGAMCOD
                    existing_record.WMAUDITFL = WMAUDITFL
                    existing_record.WMDOCEMP = WMDOCEMP
                    existing_record.WMRESAIMPFL = WMRESAIMPFL
                    existing_record.PLANTRANSPORT= PLANTRANSPORT
                    existing_record.TXTPREENREG1 = TXTPREENREG1
                    existing_record.TXTPREENREG2 = TXTPREENREG2	
                    existing_record.TXTPREENREG3 = TXTPREENREG3	
                    existing_record.TXTPREENREG4 = TXTPREENREG4	
                    existing_record.TXTPREENREG5 = TXTPREENREG5	
                    existing_record.TXTPREENREG6 = TXTPREENREG6	
                    existing_record.TXTPREENREG7 = TXTPREENREG7	
                    existing_record.TXTPREENREG8 = TXTPREENREG8	
                    existing_record.AFFCLDCOD = 	AFFCLDCOD
                    existing_record.IDENTITEEXT= IDENTITEEXT
                    existing_record.CONTACTTIERS = CONTACTTIERS
                    existing_record.CODESTAT1 =	CODESTAT1
                    existing_record.CODESTAT2 =	CODESTAT2
                    existing_record.CODESTAT3 =	CODESTAT3
                    existing_record.REGIMETPF = REGIMETPF
                    existing_record.GROUPEMENT	= GROUPEMENT
                    existing_record.LIBREA= LIBREA
                    existing_record.CA= CA
                    existing_record.NBRESALARIE	= NBRESALARIE
                    existing_record.ENCOURSMAXI1 = ENCOURSMAXI1
                    existing_record.ENCOURSMAXI2 = ENCOURSMAXI2	
                    existing_record.TXESC = TXESC
                    existing_record.TXACOMPTE = TXACOMPTE
                    existing_record.LIBREN= LIBREN
                    existing_record.REGTVATIERS = REGTVATIERS
                    existing_record.GROUPE1LIB= GROUPE1LIB
                    existing_record.GROUPE2LIB= GROUPE2LIB
                    existing_record.MEDIA= MEDIA
                    existing_record.CGVTEXCOD= CGVTEXCOD
                    existing_record.CODETARIFTTC= CODETARIFTTC
                    existing_record.FAMILLECOMMCLIENT= FAMILLECOMMCLIENT
                    existing_record.NATURETIERS = NATURETIERS
                    existing_record.ORIGINETIERS= ORIGINETIERS
                    existing_record.COMMERCIAL1 = COMMERCIAL1
                    existing_record.COMMERCIAL2 = COMMERCIAL2
                    existing_record.COMMERCIAL3 = COMMERCIAL3
                    existing_record.TIERSADRESSE1 = TIERSADRESSE1
                    existing_record.TIERSADRESSE2 = TIERSADRESSE2
                    existing_record.TIERSADRESSE3 = TIERSADRESSE3
                    existing_record.TIERSADRESSE4 = TIERSADRESSE4
                    existing_record.TIERSADRESSE5 = TIERSADRESSE5
                    existing_record.CODEADRESSE1 = CODEADRESSE1
                    existing_record.CODEADRESSE2 = CODEADRESSE2
                    existing_record.CODEADRESSE3 = CODEADRESSE3
                    existing_record.CODEADRESSE4 = CODEADRESSE4
                    existing_record.CODEADRESSE5 = CODEADRESSE5
                    existing_record.TIERSSTAT = TIERSSTAT
                    existing_record.TIERSDIVALTOREGLT= TIERSDIVALTOREGLT
                    existing_record.RELIQUATGERE1 = RELIQUATGERE1
                    existing_record.RELIQUATGERE2 = RELIQUATGERE2
                    existing_record.RELIQUATGERE3 = RELIQUATGERE3
                    existing_record.MODETRANSP = MODETRANSP
                    existing_record.DEBIDENT = DEBIDENT
                    existing_record.DEBPAYSIDENT = DEBPAYSIDENT
                    existing_record.DEBCOEFTRANSP = DEBCOEFTRANSP
                    existing_record.DEBINCOTERM3 = DEBINCOTERM3
                    existing_record.MTFRANCHISETVA = MTFRANCHISETVA
                    existing_record.NBREJOURTRANSP = NBREJOURTRANSP
                    existing_record.RFCCTRCOD = RFCCTRCOD
                    existing_record.PROTOCOL = PROTOCOL
                    existing_record.TIERSEXTERNE = TIERSEXTERNE
                    existing_record.FEU = FEU
                    existing_record.RELIQUATLIGNE = RELIQUATLIGNE
                    existing_record.VALLIGCOD = VALLIGCOD
                    existing_record.DEMATERIALISATIONTYPE = DEMATERIALISATIONTYPE
                    existing_record.TYPEUNITE = TYPEUNITE
                    existing_record.MODEEXP = MODEEXP
                    existing_record.CONDEXP = CONDEXP
                    existing_record.CRMUPDATEDH = CRMUPDATEDH
                    existing_record.CODEAGENCE = CODEAGENCE
                    existing_record.FAMILLERELANCE = FAMILLERELANCE
                    existing_record.TIERSRELANCE = TIERSRELANCE
                    existing_record.MODEFACTURE = MODEFACTURE
                    existing_record.PERIODEFACTURE = PERIODEFACTURE
                    existing_record.TOURNEE = TOURNEE
                    existing_record.RANGTOURNEE = RANGTOURNEE
                    existing_record.JOURBL = JOURBL
                    existing_record.CODEADV = CODEADV
                    existing_record.PRIORITE = PRIORITE
                    existing_record.INDICCDEWEB = INDICCDEWEB
                    existing_record.BPBASCOD = BPBASCOD
                    existing_record.BPRUPTCOD = BPRUPTCOD
                    existing_record.BLGENCOD = BLGENCOD
                    existing_record.BPRELCOD = BPRELCOD
                    existing_record.MTFANCO = MTFANCO
                    existing_record.TYPEBASEFRANCO = TYPEBASEFRANCO
                    existing_record.COEFFPOINT = COEFFPOINT
                    existing_record.NBPASSAGE = NBPASSAGE
                    existing_record.NBPOINT = NBPOINT
                    existing_record.CDLET = CDLET
                    existing_record.NUMCARTE = NUMCARTE
                    existing_record.PANNO = PANNO
                    existing_record.BQEV = BQEV
                    existing_record.WMPREPMAX = WMPREPMAX
                    existing_record.RETNAT = RETNAT
                    existing_record.IDCLIENT = IDCLIENT
                    existing_record.CARTENO = CARTENO
                    existing_record.TRANSICOD = TRANSICOD
                    existing_record.LIEUINCOTERM = LIEUINCOTERM
                    existing_record.CATCLICOD = CATCLICOD
                    existing_record.SOURCE = SOURCE
                    existing_record.SYSTEME = SYSTEME
                    existing_record.DOSEXTERNE = DOSEXTERNE
                    existing_record.ETBEXTERNE = ETBEXTERNE
                    existing_record.FOURNISSEUR = FOURNISSEUR
                    existing_record.IMPLSTCOL = IMPLSTCOL
                    existing_record.BPSILIGCOMPLETE = BPSILIGCOMPLETE
                    existing_record.CLASCODTAR= CLASCODTAR
                    existing_record.PIREFOBLIG = PIREFOBLIG
                    existing_record.PCEPIREFOBLPICOD1 = PCEPIREFOBLPICOD1
                    existing_record.PCEPIREFOBLPICOD2 = PCEPIREFOBLPICOD2
                    existing_record.PCEPIREFOBLPICOD3 = PCEPIREFOBLPICOD3
                    existing_record.PCEPIREFOBLPICOD4 = PCEPIREFOBLPICOD4
                    existing_record.CTRLREFPIECE = CTRLREFPIECE
                    existing_record.TYPEETATDST = TYPEETATDST
                    existing_record.MOTIFCHGTETAT= MOTIFCHGTETAT
                    existing_record.CGVIMPTYP = CGVIMPTYP
                    existing_record.PCEPIREFPINOOBL = PCEPIREFPINOOBL
                    existing_record.PCEPIREFPINOCTRL = PCEPIREFPINOCTRL
                    existing_record.AGENTRECOUVR = AGENTRECOUVR
                    existing_record.CIRCUITVALIDATIONBLFL = CIRCUITVALIDATIONBLFL
                    existing_record.CIRCUITVALIDATIONFCTFL = CIRCUITVALIDATIONFCTFL
                    existing_record.GENPIVOTPRERECEPCOD = GENPIVOTPRERECEPCOD
                    existing_record.PRERECEPACTIONCOD = PRERECEPACTIONCOD
                    existing_record.ACPTIMPLICITE1 = ACPTIMPLICITE1
                    existing_record.ACPTIMPLICITE2 = ACPTIMPLICITE2 
                    existing_record.ACPTIMPLICITE3 = ACPTIMPLICITE3 
                    existing_record.ACPTIMPLICITE4 = ACPTIMPLICITE4 
                    existing_record.ACPTIMPLICITE5 = ACPTIMPLICITE5 
                    existing_record.ACPTIMPLICITE6 = ACPTIMPLICITE6 
                    existing_record.ACPTBIENTX = ACPTBIENTX
                    existing_record.ACPTSERVTX = ACPTSERVTX
                    existing_record.ACPTTOTFLG = ACPTTOTFLG
                    existing_record.ACPTCTMFLG = ACPTCTMFLG
                    existing_record.ACPTEPHFLG = ACPTEPHFLG
                    existing_record.ACPTMTSEUIL = ACPTMTSEUIL
                    existing_record.ACPTMTARR = ACPTMTARR
                    existing_record.CLASCODTX = CLASCODTX
                    existing_record.DUNS = DUNS
                    existing_record.BLJRDEPART = BLJRDEPART
                    ligne_modifies += 1
                    # Sauvegarde des modifications dans la base de données
                    db.session.commit()
                    # Mise à jour de la barre de progression
                    pbar.update(1)
                else:
                    new_divalto_entry = Client_DIVALTO(
                        DOSSIER = DOSSIER,
                        CONF = CONF,
                        TIERS = TIERS,
                        VISA = VISA,
                        NOMABREGE = NOMABREGE,
                        NOM_CLIENT = NOM_CLIENT,
                        ADRCPL1 = ADRCPL1,
                        ADRCPL2= ADRCPL2,
                        RUE = RUE,
                        LOCALITE = LOCALITE,
                        VILLE = VILLE,
                        PAYS = PAYS,
                        CODEPOSTAL = CODEPOSTAL,
                        ZIPCOD = ZIPCOD,
                        REGIONADMINISTRATIVE = REGIONADMINISTRATIVE,
                        CODEINSEE = CODEINSEE,
                        LATITUDE = LATITUDE,
                        LONGITUDE = LONGITUDE,
                        TEL = TEL,
                        FAX = FAX,
                        ADRESSEWEB= ADRESSEWEB,
                        EMAIL = EMAIL,
                        NAF = NAF,
                        TITRE = TITRE,
                        MODEREGL = MODEREGL,
                        DEVISE = DEVISE,
                        LANGUE = LANGUE,
                        COMPTE = COMPTE,
                        COMPTEMASQUE = COMPTEMASQUE,
                        CRITERESELECTION = CRITERESELECTION,
                        SIRET = SIRET,
                        ETABLISSEMENT =  ETABLISSEMENT,
                        DATEFINVALID = DATEFINVALID,
                        NUMERONOTE=NUMERONOTE,
                        JOINT= JOINT,
                        IDCONNECT=IDCONNECT,
                        CALENDRIER=CALENDRIER,
                        GLN=GLN,
                        TELCLE=TELCLE,
                        ICPFL=ICPFL,
                        CATEGORIEPIECE=CATEGORIEPIECE,
                        TAGS= TAGS,
                        CODETARIF= CODETARIF,
                        CODEREMISE= CODEREMISE,
                        CODETARIFPROMOTION = CODETARIFPROMOTION,
                        CODEREMISEPROMOTION = CODEREMISEPROMOTION,
                        FAMILLETARIFCLIENT = FAMILLETARIFCLIENT,
                        FAMILLETARIFEXCEPTIONCLIENT = FAMILLETARIFEXCEPTIONCLIENT,
                        CLASSEREMISECLIENT = CLASSEREMISECLIENT,
                        CLASSEREMISEEXCEPTIONCLIENT = CLASSEREMISEEXCEPTIONCLIENT,
                        REMISE1 = REMISE1,
                        REMISE2	= REMISE2,
                        REMISE3 =   REMISE3,           
                        TYPEREMISE1 = TYPEREMISE1,
                        TYPEREMISE2 = TYPEREMISE2,
                        TYPEREMISE3 = TYPEREMISE3,
                        DATEDEROPERATION = DATEDEROPERATION,
                        NBEX1 = NBEX1,
                        NBEX2 =  NBEX2,
                        NBEX3 = NBEX3,
                        NBEX4  = NBEX4,
                        EDITTYP1 = EDITTYP1,
                        EDITTYP2 = EDITTYP2,
                        EDITTYP3 = EDITTYP3,
                        EDITTYP4 = EDITTYP4,
                        ETANO1= ETANO1,
                        ETANO2= ETANO2,
                        ETANO3= ETANO3,
                        ETANO4= ETANO4,
                        AXENO = AXENO,
                        AXEMASQUE = AXEMASQUE,
                        STLGTGAMCOD = STLGTGAMCOD,
                        WMAUDITFL = WMAUDITFL,
                        WMDOCEMP = WMDOCEMP,
                        WMRESAIMPFL = WMRESAIMPFL,
                        PLANTRANSPORT= PLANTRANSPORT,
                        TXTPREENREG1 = TXTPREENREG1,
                        TXTPREENREG2 = TXTPREENREG2,	
                        TXTPREENREG3 = TXTPREENREG3,	
                        TXTPREENREG4 = TXTPREENREG4,	
                        TXTPREENREG5 = TXTPREENREG5,	
                        TXTPREENREG6 = TXTPREENREG6,	
                        TXTPREENREG7 = TXTPREENREG7,	
                        TXTPREENREG8 = TXTPREENREG8,	
                        AFFCLDCOD = AFFCLDCOD,
                        IDENTITEEXT = IDENTITEEXT,
                        CONTACTTIERS = CONTACTTIERS,
                        CODESTAT1 =	CODESTAT1,
                        CODESTAT2 =	CODESTAT2,
                        CODESTAT3 =	CODESTAT3,
                        REGIMETPF = REGIMETPF,
                        GROUPEMENT	= GROUPEMENT,
                        LIBREA = LIBREA,
                        CA = CA,
                        NBRESALARIE	= NBRESALARIE,
                        ENCOURSMAXI1 = ENCOURSMAXI1,
                        ENCOURSMAXI2 = ENCOURSMAXI2	,
                        TXESC = TXESC,
                        TXACOMPTE = TXACOMPTE,
                        LIBREN= LIBREN,
                        REGTVATIERS = REGTVATIERS,
                        GROUPE1LIB= GROUPE1LIB,
                        GROUPE2LIB= GROUPE2LIB,
                        MEDIA = MEDIA,
                        CGVTEXCOD= CGVTEXCOD,
                        CODETARIFTTC= CODETARIFTTC,
                        FAMILLECOMMCLIENT= FAMILLECOMMCLIENT,
                        NATURETIERS = NATURETIERS,
                        ORIGINETIERS= ORIGINETIERS,
                        COMMERCIAL1 = COMMERCIAL1,
                        COMMERCIAL2 = COMMERCIAL2,
                        COMMERCIAL3 = COMMERCIAL3,
                        TIERSADRESSE1 = TIERSADRESSE1,
                        TIERSADRESSE2 = TIERSADRESSE2,
                        TIERSADRESSE3 = TIERSADRESSE3,
                        TIERSADRESSE4 = TIERSADRESSE4,
                        TIERSADRESSE5 = TIERSADRESSE5,
                        CODEADRESSE1 = CODEADRESSE1,
                        CODEADRESSE2 = CODEADRESSE2,
                        CODEADRESSE3 = CODEADRESSE3,
                        CODEADRESSE4 = CODEADRESSE4,
                        CODEADRESSE5 = CODEADRESSE5,
                        TIERSSTAT = TIERSSTAT,
                        TIERSDIVALTOREGLT= TIERSDIVALTOREGLT,
                        RELIQUATGERE1 = RELIQUATGERE1,
                        RELIQUATGERE2 = RELIQUATGERE2,
                        RELIQUATGERE3 = RELIQUATGERE3,
                        MODETRANSP = MODETRANSP,
                        DEBIDENT = DEBIDENT,
                        DEBPAYSIDENT = DEBPAYSIDENT,
                        DEBCOEFTRANSP = DEBCOEFTRANSP,
                        DEBINCOTERM3 = DEBINCOTERM3,
                        MTFRANCHISETVA = MTFRANCHISETVA,
                        NBREJOURTRANSP = NBREJOURTRANSP,
                        RFCCTRCOD = RFCCTRCOD,
                        PROTOCOL = PROTOCOL,
                        TIERSEXTERNE = TIERSEXTERNE,
                        FEU = FEU,
                        RELIQUATLIGNE = RELIQUATLIGNE,
                        VALLIGCOD = VALLIGCOD,
                        DEMATERIALISATIONTYPE = DEMATERIALISATIONTYPE,
                        TYPEUNITE = TYPEUNITE,
                        MODEEXP = MODEEXP,
                        CONDEXP = CONDEXP,
                        CRMUPDATEDH = CRMUPDATEDH,
                        CODEAGENCE = CODEAGENCE,
                        FAMILLERELANCE = FAMILLERELANCE,
                        TIERSRELANCE = TIERSRELANCE,
                        MODEFACTURE = MODEFACTURE,
                        PERIODEFACTURE = PERIODEFACTURE,
                        TOURNEE = TOURNEE,
                        RANGTOURNEE = RANGTOURNEE,
                        JOURBL = JOURBL,
                        CODEADV = CODEADV,
                        PRIORITE = PRIORITE,
                        INDICCDEWEB = INDICCDEWEB,
                        BPBASCOD = BPBASCOD,
                        BPRUPTCOD = BPRUPTCOD,
                        BLGENCOD = BLGENCOD,   
                        BPRELCOD = BPRELCOD,
                        MTFANCO = MTFANCO,
                        TYPEBASEFRANCO = TYPEBASEFRANCO,
                        COEFFPOINT = COEFFPOINT,
                        NBPASSAGE = NBPASSAGE,
                        NBPOINT = NBPOINT,
                        CDLET = CDLET,
                        NUMCARTE = NUMCARTE,
                        PANNO = PANNO,
                        BQEV = BQEV,
                        WMPREPMAX = WMPREPMAX,
                        RETNAT = RETNAT,
                        IDCLIENT = IDCLIENT,
                        CARTENO = CARTENO,
                        TRANSICOD = TRANSICOD,
                        LIEUINCOTERM = LIEUINCOTERM,
                        CATCLICOD = CATCLICOD,
                        SOURCE = SOURCE,
                        SYSTEME = SYSTEME,
                        DOSEXTERNE = DOSEXTERNE,
                        ETBEXTERNE = ETBEXTERNE,
                        FOURNISSEUR = FOURNISSEUR,
                        IMPLSTCOL = IMPLSTCOL,
                        BPSILIGCOMPLETE = BPSILIGCOMPLETE,
                        CLASCODTAR= CLASCODTAR,
                        PIREFOBLIG = PIREFOBLIG,
                        PCEPIREFOBLPICOD1 = PCEPIREFOBLPICOD1,
                        PCEPIREFOBLPICOD2 = PCEPIREFOBLPICOD2,
                        PCEPIREFOBLPICOD3 = PCEPIREFOBLPICOD3,
                        PCEPIREFOBLPICOD4 = PCEPIREFOBLPICOD4,
                        CTRLREFPIECE = CTRLREFPIECE,
                        TYPEETATDST = TYPEETATDST,
                        MOTIFCHGTETAT= MOTIFCHGTETAT,
                        CGVIMPTYP = CGVIMPTYP,
                        PCEPIREFPINOOBL = PCEPIREFPINOOBL,
                        PCEPIREFPINOCTRL = PCEPIREFPINOCTRL,
                        AGENTRECOUVR = AGENTRECOUVR,
                        CIRCUITVALIDATIONBLFL = CIRCUITVALIDATIONBLFL,
                        CIRCUITVALIDATIONFCTFL = CIRCUITVALIDATIONFCTFL,
                        GENPIVOTPRERECEPCOD = GENPIVOTPRERECEPCOD,
                        PRERECEPACTIONCOD = PRERECEPACTIONCOD,
                        ACPTIMPLICITE1 = ACPTIMPLICITE1,
                        ACPTIMPLICITE2 = ACPTIMPLICITE2,
                        ACPTIMPLICITE3 = ACPTIMPLICITE3,
                        ACPTIMPLICITE4 = ACPTIMPLICITE4, 
                        ACPTIMPLICITE5 = ACPTIMPLICITE5, 
                        ACPTIMPLICITE6 = ACPTIMPLICITE6, 
                        ACPTBIENTX = ACPTBIENTX,
                        ACPTSERVTX = ACPTSERVTX,
                        ACPTTOTFLG = ACPTTOTFLG,
                        ACPTCTMFLG = ACPTCTMFLG,
                        ACPTEPHFLG = ACPTEPHFLG,
                        ACPTMTSEUIL = ACPTMTSEUIL,
                        ACPTMTARR = ACPTMTARR,
                        CLASCODTX = CLASCODTX,
                        DUNS = DUNS,
                        BLJRDEPART = BLJRDEPART
                    )
                    
                    db.session.add(new_divalto_entry)
                    # Ajout du nouvel enregistrement dans la base de données
                    db.session.commit()
                    lignes_ajoutees += 1
                    # Mise à jour de la barre de progression
                    pbar.update(1)
                


            return jsonify({
            "message": f"Fichier .xlsx importé avec succès dans la base de données. {lignes_ajoutees} lignes ont été ajoutées, {ligne_modifies} lignes ont été mises à jour."
        })
        
    except Exception as e:
        error_message = f"Une erreur s'est produite : {str(e)}"
        return jsonify({
            "error": error_message,
            "details": {
                "lignes_ajoutees": lignes_ajoutees,
                "ligne_modifies": ligne_modifies,
                "error_type": str(type(e).__name__),  # Ajout du type d'erreur
                "error_details": str(e)  # Ajout des détails spécifiques de l'erreur
            }
        }), 405


def Lire_BD_DIVALTO():
    clients = Client_DIVALTO.query.all()  # Récupérer tous les clients depuis la base de données
    clients_json = [client.to_dict() for client in clients]  # Convertir les objets clients en dictionnaires

    return jsonify(clients_json)  # Retourner les données au format JSON
    
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##
## -----------------------------------------------------** Table CLIENT ISFACT **------------------------------------------------------------------ ##
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##

def Ecrire_MAJ_Clients_ISFACT(file_path):
    # Initialisation
    lignes_ajoutees = 0
    ligne_modifies = 0
    ligne_ignores = 0
    try:
        # Lire le fichier Excel dans un DataFrame
        dataFrame = pd.read_excel(file_path)
        longueur_dataFrame_avant_suppression = len(dataFrame) # longueur initiale du DF
        dataFrame.drop_duplicates(subset='CodeClient', keep='first', inplace=True)
        total_rows = len(dataFrame)
        print(f" ** Réduction du DF après suppression des doublons {str(longueur_dataFrame_avant_suppression)}  => " + str(total_rows))
        date_now = str(datetime.now())
        
        # Itération sur le DF
    
        # Utilisation de tqdm pour obtenir une barre de progression
        with tqdm(total=total_rows, desc=" * Importation des données ISAFACT en cours", unit=" lignes") as pbar:
            
            # Avant de commencer l'itération sur le DataFrame, supprimez les doublons basés sur la colonne 'CodeClient'
            # Itération sur le DataFrame
            for index, row in dataFrame.iterrows():
                CodeClient = row['CodeClient']
                FamilleTIERS = row['FamilleTIERS']
                NomFACT = sanitarise_donnes_niveau1(row['NomFACT'])
                PrenomFACT = sanitarise_donnes_niveau1(row['PrenomFACT'])
                AdresseFACT = sanitarise_donnes_niveau1(row['AdresseFACT'])
                CPFACT = row['CPFACT']
                VilleFACT = sanitarise_donnes_niveau1(row['VilleFACT'])
                PaysFACT = row['PaysFACT']
                EmailTIERS = extract_email(row['EmailTIERS'])
                NomLOC = sanitarise_donnes_niveau1(row['NomLOC'])
                PrenomLOC = sanitarise_donnes_niveau1(row['PrenomLOC'])
                AdresseSITE = sanitarise_donnes_niveau1(row['AdresseSITE'])
                CPSITE = row['CPSITE']
                VilleSITE = row['VilleSITE']
                PaysSITE = row['PaysSITE']
                Livrer_adresse_facturation = row['Livrer_adresse_facturation']
                CodeTVA = row['CodeTVA']
                TVA = row['LibelleTVA']
                CodeTypeCONTRAT = row['CodeTypeCONTRAT']
                CodeCONTRAT = row['CodeCONTRAT']
                CategTARIF = row['CategTARIF']
                Code_Rglt = row["Mode_rglt_Code"]
                Mode_rglt = row['Mode_rglt']
                Delai_rglt = row['Delai_rglt']
                StatusTiers = row['StatusTiers']
                NivRelanceTiers = row['NivRelanceTiers']
                Nom_representant = row['Nom_representant']
                RIB_Domic = row['RIB_Domic']
                RIB_Etabl = row['RIB_Etabl']
                RIB_IBAN = row['RIB_IBAN']
                RIB_Cle = row['RIB_Cle']
                RIB_CodeBIC = row['RIB_CodeBIC']
                NEGOCE = (row['NEGOCE'])
                TP_nom = (row['TP_nom'])
                # Gestion des tels
                TP_tel = clean_phone_number(row['TP_tel'])
                TelSITE1 = clean_phone_number(row['TelSITE1'])
                TelSITE2 = clean_phone_number(row['TelSITE2'])
                TelSITE3 = clean_phone_number(row['TelSITE3'])
                TelFACT1 = clean_phone_number(row['TelFACT1'])
                TelFACT2 = clean_phone_number(row['TelFACT2'])
                TelFACT3 = clean_phone_number(row['TelFACT3'])

                # Convertir les dates au format correct
                Date_creation_tiers = datetime.strptime(str(row['Date_creation_tiers']), '%d/%m/%Y').date() if pd.notna(row['Date_creation_tiers']) else None
                DateProchaineIntervention = datetime.strptime(str(row['DateProchaineIntervention']), '%d/%m/%Y').date() if pd.notna(row['DateProchaineIntervention']) else None
                DateMEPContrat = datetime.strptime(str(row['DateMEPContrat']), '%d/%m/%Y').date() if pd.notna(row['DateMEPContrat']) else None
                Date_derniere_facture = convert_specific_to_date(row['Date_derniere_facture'])

                # Vérification de la présence d'une adresse de facturation

                if not (str(row['CPFACT']).isdigit() and str(row['CPFACT']) != ''):
                    ligne_ignores += 1
                    pass
                else:                
                    existing_record = Client_ISAFACT.query.filter_by(CodeClient=CodeClient).first()
                    if existing_record:
                    # Si l'enregistrement existe déjà, mettez à jour ses valeurs
                        existing_record.FamilleTIERS = FamilleTIERS
                        existing_record.NomFACT = NomFACT
                        existing_record.PrenomFACT = PrenomFACT
                        existing_record.AdresseFACT = AdresseFACT
                        existing_record.CPFACT = CPFACT
                        existing_record.VilleFACT = VilleFACT
                        existing_record.PaysFACT = PaysFACT
                        existing_record.EmailTIERS = EmailTIERS
                        existing_record.TelFACT1 = TelFACT1
                        existing_record.TelFACT2 = TelFACT2
                        existing_record.TelFACT3 = TelFACT3
                        existing_record.NomLOC = NomLOC
                        existing_record.PrenomLOC = PrenomLOC
                        existing_record.AdresseSITE = AdresseSITE
                        existing_record.CPSITE = CPSITE
                        existing_record.VilleSITE = VilleSITE
                        existing_record.PaysSITE = PaysSITE
                        existing_record.TelSITE1 = TelSITE1
                        existing_record.TelSITE2 = TelSITE2
                        existing_record.TelSITE3 = TelSITE3
                        existing_record.Livrer_adresse_facturation = Livrer_adresse_facturation
                        existing_record.CodeTVA = CodeTVA
                        existing_record.TVA = TVA
                        existing_record.CodeTypeCONTRAT = CodeTypeCONTRAT
                        existing_record.CodeCONTRAT = CodeCONTRAT
                        existing_record.CategTARIF = CategTARIF
                        existing_record.Code_Rglt = Code_Rglt
                        existing_record.Mode_rglt = Mode_rglt
                        existing_record.Delai_rglt = Delai_rglt
                        existing_record.StatusTiers = StatusTiers
                        existing_record.NivRelanceTiers = NivRelanceTiers
                        existing_record.Nom_representant = Nom_representant
                        existing_record.RIB_Domic = RIB_Domic
                        existing_record.RIB_Etabl = RIB_Etabl
                        existing_record.RIB_IBAN = RIB_IBAN
                        existing_record.RIB_Cle  = RIB_Cle 
                        existing_record.RIB_CodeBIC = RIB_CodeBIC
                        existing_record.NEGOCE = NEGOCE
                        existing_record.TP_nom = TP_nom
                        existing_record.TP_tel = TP_tel
                        existing_record.Date_creation_tiers = Date_creation_tiers
                        existing_record.DateProchaineIntervention = DateProchaineIntervention
                        existing_record.DateMEPContrat = DateMEPContrat
                        existing_record.Date_derniere_facture = Date_derniere_facture
                        existing_record.UpdatedAt = datetime.now()  # Mettez à jour le champ UpdatedAt
                        existing_record.LastUpdatedBy = 'ADMIN2'
                        ligne_modifies += 1
                        pbar.update(1)
                    else:
                        try:
                        # Si l'enregistrement n'existe pas, créez un nouvel enregistrement
                            new_client = Client_ISAFACT(
                                CodeClient=CodeClient,
                                FamilleTIERS=FamilleTIERS,
                                NomFACT=NomFACT,
                                PrenomFACT=PrenomFACT,
                                AdresseFACT=AdresseFACT,
                                CPFACT=CPFACT,
                                VilleFACT=VilleFACT,
                                PaysFACT=PaysFACT,
                                EmailTIERS=EmailTIERS,
                                TelFACT1=TelFACT1,
                                TelFACT2=TelFACT2,
                                TelFACT3=TelFACT3,
                                NomLOC=NomLOC,
                                PrenomLOC=PrenomLOC,
                                AdresseSITE=AdresseSITE,
                                CPSITE=CPSITE,
                                VilleSITE=VilleSITE,
                                PaysSITE=PaysSITE,
                                TelSITE1=TelSITE1,
                                TelSITE2=TelSITE2,
                                TelSITE3=TelSITE3,
                                Livrer_adresse_facturation=Livrer_adresse_facturation,
                                CodeTVA=CodeTVA,
                                TVA=TVA,
                                CodeTypeCONTRAT = CodeTypeCONTRAT,
                                CodeCONTRAT=CodeCONTRAT,
                                CategTARIF=CategTARIF,
                                Code_Rglt = Code_Rglt,
                                Mode_rglt=Mode_rglt,
                                Delai_rglt=Delai_rglt,
                                StatusTiers=StatusTiers,
                                NivRelanceTiers=NivRelanceTiers,
                                Nom_representant=Nom_representant,
                                RIB_Domic=RIB_Domic,
                                RIB_Etabl=RIB_Etabl,
                                RIB_IBAN=RIB_IBAN,
                                RIB_Cle=RIB_Cle,
                                RIB_CodeBIC=RIB_CodeBIC,
                                NEGOCE=NEGOCE,
                                TP_nom=TP_nom,
                                TP_tel=TP_tel,
                                Date_creation_tiers=Date_creation_tiers,
                                DateProchaineIntervention=DateProchaineIntervention,
                                DateMEPContrat=DateMEPContrat,
                                Date_derniere_facture=Date_derniere_facture,
                                CreatedAt= datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S.%f'),
                                UpdatedAt= datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S.%f'),
                                CreatedBy='ADMIN',
                                LastUpdatedBy='ADMIN'
                            )
                            db.session.add(new_client)
                            lignes_ajoutees += 1
                            pbar.update(1)
                        except Exception as e:
                            print(f" * Erreur lors de la création du nouvel enregistrement : {e}")
                            
            db.session.commit()
            return jsonify({
                        "message": "Mise à jour des clients ISAFACT réussie",
                        "lignes_ajoutees": lignes_ajoutees,
                        "ligne_modifies": ligne_modifies
                    }), 200

 
    except Exception as e:
        return jsonify({" * error": f"Une erreur s'est produite : {str(e)}, ceci dit {lignes_ajoutees} ont été ajoutées et {ligne_modifies} ont été modifiées"}), 405
    
def lire_donnees_ISAFACT():
    clients = Client_ISAFACT.query.all()  # Récupérer tous les clients depuis la base de données
    clients_json = [client.to_dict() for client in clients]  # Convertir les objets clients en dictionnaires

    return jsonify(clients_json)  # Retourner les données au format JSON
      
def nbre_entrée_ISAFACT():
    nbre_client_isafact = len(Client_ISAFACT.query.all())
    return nbre_client_isafact

## ------------------------------------------------------------------------------------------------------------------------------------------------ ##
## ---------------------------------------------------------** Table Client **--------------------------------------------------------------------- ##
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##

def lire_base_de_donnes_client():

    clients = Client.query.all()
            # Convertir les données en format JSON
    data_json = [
        {
            'id': entry.id,
            'code': entry.code,
            'email': entry.courriel,
            'nom': entry.nom,
            'prenom': entry.prenom
        }
        for entry in clients
        ]

    return jsonify(data_json)
 
def lire_ecrire_mettre_a_jour_fichier_csv(file):
    with open(file, 'r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv, delimiter=';')
        next(lecteur_csv)  # Ignorer l'en-tête

        lignes_ajoutees = 0
        lignes_modifiees = 0

        for ligne in tqdm(lecteur_csv, desc="Importation en cours", unit=" lignes"):
            if len(ligne) >= 4:
                code = ligne[0].strip()
                email = check_email(ligne[1].lower())
                nom = remove_special_characters(ligne[2].strip())
                prenom = remove_special_characters(ligne[3].strip())

                # Vérification et nettoyage du champ "Code"
                code = code if code and len(code) >= 7 else ""  # Vérifie si le code est valide

                client_existant = Client.query.filter_by(code=code).first()

                if client_existant:
                    # Mettre à jour les valeurs existantes
                    client_existant.courriel = email
                    client_existant.nom = nom
                    client_existant.prenom = prenom
                    lignes_modifiees += 1
                else:
                    # Créer une nouvelle entrée
                    nouveau_client = Client(
                        code=code,
                        courriel=email,
                        nom=nom,
                        prenom=prenom
                    )
                    db.session.add(nouveau_client)
                    lignes_ajoutees += 1

        db.session.commit()

    return jsonify({" * message": f"Fichier CSV importé avec succès dans la base de données. {lignes_ajoutees} lignes ont été ajoutées, {lignes_modifiees} lignes ont été mises à jour."})

## ------------------------------------------------------------------------------------------------------------------------------------------------ ##
## -------------------------------------------------------** Table GEOGRAPHY **-------------------------------------------------------------------- ##
## ------------------------------------------------------------------------------------------------------------------------------------------------ ##

def lire_ercrire_mettre_a_jour_table_geography(file_path):
    try:
        # Ouvre le fichier Excel
        df = pd.read_excel(file_path)
        lignes_ajoutees = 0
        lignes_modifiees = 0
        
        # Itération sur le DF (DataFrame)
        for index, row in df.iterrows():
            numero_departement = row['numero_departement']
            nom_departement = row['nom_departement']
            region_departement = row['region_departement']
            pays = row['pays']

            # Vérifie s'il existe déjà une entrée pour ce numéro de département
            existing_departement = Geography.query.filter_by(numero_departement=numero_departement).first()

            if existing_departement:
                # Mettre à jour les valeurs de l'entrée existante
                existing_departement.nom_departement = nom_departement
                existing_departement.region_departement = region_departement
                existing_departement.pays = pays
                lignes_modifiees += 1
            else:
                # Création d'une nouvelle instance de la classe Departement
                new_departement = Geography(numero_departement=numero_departement, nom_departement=nom_departement, region_departement=region_departement, pays=pays)
                db.session.add(new_departement)
                lignes_ajoutees += 1

        # Enregistrer les modifications dans la base de données
        db.session.commit()

        return jsonify({
            "message": f" * Fichier CSV importé avec succès dans la base de données. {lignes_ajoutees} lignes ont été ajoutées, {lignes_modifiees} lignes ont été mises à jour."
        })
    except Exception as e:
        return jsonify({"error": f"Une erreur s'est produite : {str(e)}"}), 405
    
def lire_donnees_BD_geography():
    departement = Geography.query.all()

    # Convertir les données en format JSON
    data_json = [
        {
            'numero_departement': str(entry.numero_departement),
            "nom_departement": entry.nom_departement,
            "region_departement": entry.region_departement
        }
        for entry in departement
    ]

    return jsonify(data_json)


