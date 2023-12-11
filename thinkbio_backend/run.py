# run.py
from app import create_app, db
from app.services import initialisation_mode_paiement, initialisation_T119, initialisation_Article_facturation_contrat, initialisation_mode_paiement, initialisation_T119, initialisation_T111, initialisation_typemodel, initialisation_model_contrat, initialisation_table_materiel, intialisation_BD_SITUATION_ISFACT, KillAllTable

app = create_app()

# Lié les modèles à l'instance SQLAlchemy
with app.app_context():
    KillAllTable()
    db.create_all()
    print('\033[33m ** Synchronisation des modèles: **\033[0m ')
    intialisation_BD_SITUATION_ISFACT()
    initialisation_table_materiel()
    initialisation_model_contrat()
    initialisation_mode_paiement()
    initialisation_T119()
    initialisation_Article_facturation_contrat()
    initialisation_T111()
    initialisation_typemodel()

if __name__ == '__main__':
    app.run(debug=True)
