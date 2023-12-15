from app import db
from app.models import RIB_ISAFACT, CLI_ISFACT, Client_ISAFACT
from tqdm import tqdm
from sqlalchemy.orm.exc import NoResultFound

def Ecrire_Table_RIB_from_ISAFACT():
    lignes_ajoutees = 0
    lignes_modifiees = 0

    # Ecriture de la table RIB depuis ISFACT
    cli = CLI_ISFACT.query.all()
    total_cli = len(cli)

    for client in tqdm(cli, desc=" * Processing RIB", unit='client/s', total=total_cli):
        client_ISAFACT = Client_ISAFACT.query.filter_by(CodeClient=client.CodeClient).first()
        
        if client_ISAFACT:
            IBAN = client_ISAFACT.RIB_IBAN

            if IBAN is not None:
                IBAN_BIC = client_ISAFACT.RIB_CodeBIC

                entree_RIB = RIB_ISAFACT.query.filter_by(CodeClient=client.CodeClient).first()
                # UPDATE
                if entree_RIB:
                    entree_RIB.Client_id = client.Client_id
                    entree_RIB.FamilleTIERS = client.FamilleTIERS
                    entree_RIB.IBANPAYS = IBAN[:2]
                    entree_RIB.IBANCLE = IBAN[2:4]
                    entree_RIB.IBANCOMPTE = IBAN[4:]
                    entree_RIB.RIBBIC = IBAN_BIC
                    entree_RIB.RIBDO = client_ISAFACT.RIB_Domic
                    lignes_modifiees += 1

                else:
                    # CREATE
                    new_entry_RIB = RIB_ISAFACT(
                        Client_id=client.Client_id,
                        FamilleTIERS = client.FamilleTIERS,
                        IBANPAYS=IBAN[:2],
                        IBANCLE=IBAN[2:4],
                        IBANCOMPTE=IBAN[4:],
                        RIBBIC=IBAN_BIC,
                        RIBDO=client_ISAFACT.RIB_Domic
                    )
                    db.session.add(new_entry_RIB)
                    lignes_ajoutees += 1

    db.session.commit()
    return lignes_ajoutees, lignes_modifiees