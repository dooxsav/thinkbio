# models/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)

    # Import des modèles ici pour les enregistrer dans la base de données
    from .commercial_model import Commercial
    from .secteur_model import Secteur

    # Vous pouvez également ajouter d'autres modèles au fur et à mesure de leur création

    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas encore (à des fins de démonstration)

# Assurez-vous d'importer vos modèles ici pour qu'ils soient enregistrés dans la base de données
from . import commercial_model
from . import secteur_model
