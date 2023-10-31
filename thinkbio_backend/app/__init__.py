from flask import Flask
from app.routes import hello_bp, GRC_bp
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    app = Flask(__name__)
    # Charger les variables d'environnement à partir du fichier .env
    load_dotenv()
    # Configuration de la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    db = SQLAlchemy(app)
    # Configuration de l'application Flask, par exemple :
    # app.config['SECRET_KEY'] = 'your_secret_key'
    # ...

    # Importer les blueprints (routes) ici
    app.register_blueprint(hello_bp)
    app.register_blueprint(GRC_bp)

    return app