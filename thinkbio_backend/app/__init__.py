from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import hello_bp, GRC_bp, Client_bp
from dotenv import load_dotenv

db = SQLAlchemy()  # Initialisez l'instance SQLAlchemy

def create_app():
    app = Flask(__name__)

    # Charger les variables d'environnement à partir du fichier .env
    load_dotenv()

    # Configuration de la base de données pour SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votre_base_de_donnees.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Liez l'instance SQLAlchemy à votre application Flask

    # Importer les blueprints (routes) ici
    app.register_blueprint(hello_bp)
    app.register_blueprint(GRC_bp)
    app.register_blueprint(Client_bp)

    return app