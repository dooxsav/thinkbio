# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()  # Initialisez l'instance SQLAlchemy

def create_app():
    app = Flask(__name__)

    # Charger les variables d'environnement à partir du fichier .env
    load_dotenv()

    # Configuration de la base de données pour SQLAlchemy
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '../../DB/bionest.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Liez l'instance SQLAlchemy à votre application Flask

    # Importer les blueprints (routes) ici
    from app.routes import hello_bp, GRC_bp, Client_bp, Geography_bp, Client_ISAFACT_bp
    app.register_blueprint(hello_bp)
    app.register_blueprint(GRC_bp)
    app.register_blueprint(Client_bp)
    app.register_blueprint(Geography_bp)
    app.register_blueprint(Client_ISAFACT_bp)

    return app
