# run.py
from app import create_app, db
from app.services import initialisation_mode_paiement

app = create_app()

# Lié les modèles à l'instance SQLAlchemy
with app.app_context():
    db.create_all()
    initialisation_mode_paiement()

if __name__ == '__main__':
    app.run(debug=True)
