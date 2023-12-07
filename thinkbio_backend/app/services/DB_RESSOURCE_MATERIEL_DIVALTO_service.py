from app import db
from app.models import RESSOURCE_MATERIEL_DIVALTO, MATERIEL_ISAFACT, TYPE_MATERIEL, SITE_ISAFACT, CLIENT_CONTRAT_ISAFACT
from tqdm import tqdm

def lire_BD_RESSOURCE_MATERIEL_DIVALTO():
    materiels = RESSOURCE_MATERIEL_DIVALTO.query.all()
    return [materiel.to_dict() for materiel in materiels]  # Convertir les objets en dictionnaires

def ecrire_BD_RESSOURCE_MATERIEL_DIVALTO():
    print(' * Attribution des systèmes...')
    systemes_ISA = MATERIEL_ISAFACT.query.all()
    total_systeme = len(systemes_ISA)
    ligne_ajoute = 0
    ligne_modifie = 0
    ligne_ignore = 0
    compteur_beton = 0
    compteur_plastique = 0
    compteur_s = 0

    for systeme in tqdm(systemes_ISA, desc='Attribution des systèmes', total=total_systeme, unit='système/s'):
        systeme_existant = RESSOURCE_MATERIEL_DIVALTO.query.filter_by(NUMEROSERIEBIEN=systeme.CodeClient).first()
        
        if systeme.MATERIAUX == "BETON":
            compteur_beton += 1
            CODEMATERIEL = f'SYSBET{compteur_beton:013d}'
        elif systeme.MATERIAUX == "PLASTIQUE":
            compteur_plastique += 1
            CODEMATERIEL = f'SYSPLAT{compteur_plastique:013d}'
        elif systeme.MATERIAUX == "S":
            compteur_s += 1
            CODEMATERIEL = f'SYSSC{compteur_s:013d}'
        else:
            CODEMATERIEL = 'SYSAUTRE'
            # print(f'Pas de MATERIAUX trouvé pour {systeme.CodeClient}')

        ref_materiel = TYPE_MATERIEL.query.filter_by(CODETYPERESSOURCEMATERIEL=systeme.TYPE).first()
        if ref_materiel:
            code_genre = ref_materiel.CODEGENRE
            designation_materiel = ref_materiel.LIBELLE_TYPE
        else:
            code_genre = 'AUTRES'
            designation_materiel = 'AUTRES'
            ligne_ignore += 1

        ref_client = SITE_ISAFACT.query.filter_by(CodeClient=systeme.CodeClient).first()
        if ref_client:
            client_ID = ref_client.Client_id
            site_ID = ref_client.Site_id
        else:
            client_ID = '#NC'
            site_ID = "#NC"
            # print(f' * INFORMATION : pas de référence client et site pour {systeme.CodeClient}')
        
        # RECHERCHE du CONTRAT (si existe)
        contrat_station = CLIENT_CONTRAT_ISAFACT.query.filter_by(CodeClient=systeme.CodeClient).first()
        if contrat_station:
            code_contrat_divalto = contrat_station.NUMERO_CONTRAT
        else:
            code_contrat_divalto = '#NC'

        if systeme_existant:
            # UPDATE
            ligne_modifie += 1
            systeme_existant.CODEMATERIEL = CODEMATERIEL
            systeme_existant.CODEGENRE = code_genre
            systeme_existant.CODETYPERESSOURCEMATERIEL = systeme.TYPE
            systeme_existant.DESIGNATIONMATERIEL = designation_materiel
            systeme_existant.CODELOCALISATION = site_ID
            systeme_existant.TIERSINDIVIDU = client_ID
            systeme_existant.MARQUE = systeme.FABRIQUANT_CUVE
            systeme_existant.NUMEROSERIEBIEN = systeme.CodeClient
            systeme_existant.CODE_CONTRAT_DIVALTO = code_contrat_divalto
        else:
            # CREATE
            new_systeme = RESSOURCE_MATERIEL_DIVALTO(
                CODEMATERIEL=CODEMATERIEL,
                CODEGENRE=code_genre,
                CODETYPERESSOURCEMATERIEL=systeme.TYPE,
                DESIGNATIONMATERIEL=designation_materiel,
                CODELOCALISATION=site_ID,
                TIERSINDIVIDU=client_ID,
                MARQUE=systeme.FABRIQUANT_CUVE,
                NUMEROSERIEBIEN = systeme.CodeClient,
                CODE_CONTRAT_DIVALTO = code_contrat_divalto
            )
            ligne_ajoute += 1
            db.session.add(new_systeme)
    
    db.session.commit()
    print(f' * Intégration des systèmes terminée. {ligne_ajoute} ligne(s) ajoutée(s), {ligne_modifie} ligne(s) modifiée(s), {ligne_ignore} ligne(s) sont ignorée(s)')
    return ligne_ajoute, ligne_modifie
