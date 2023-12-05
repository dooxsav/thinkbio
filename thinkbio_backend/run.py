# run.py
from app import create_app, db
from app.services import initialisation_mode_paiement, initialisation_T119, initialisation_Article_facturation_contrat, initialisation_mode_paiement, initialisation_T119, initialisation_T111, initialisation_typemodel, initialisation_model_contrat

app = create_app()

# Lié les modèles à l'instance SQLAlchemy
with app.app_context():
    db.create_all()
    print('\033[33m ** Synchronisation des modèles: **\033[0m ')
    initialisation_model_contrat()
    initialisation_mode_paiement()
    initialisation_T119()
    initialisation_Article_facturation_contrat()
    initialisation_T111()
    initialisation_typemodel()

if __name__ == '__main__':
    app.run(debug=True)
