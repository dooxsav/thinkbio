# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv


db = SQLAlchemy()  # Initialisez l'instance SQLAlchemy

def create_app():
    app = Flask(__name__)
    CORS(app)  # Active CORS pour toute l'application
    # Charger les variables d'environnement à partir du fichier .env
    load_dotenv()

    # Configuration de la base de données pour SQLAlchemy
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '../../DB/bionest.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Liez l'instance SQLAlchemy à votre application Flask



    # Importer les blueprints (routes) ici
    from app.routes import hello_bp, GRC_bp, Client_bp, Geography_bp, Client_ISAFACT_bp, Client_DIVALTO_bp, OperationDB_bp, Geolocation_bp, ClientContrat_bp, OperationDB_bp, MaintenanceDB_bp, RessourcesMaterielDivalto_bp
    app.register_blueprint(hello_bp)
    app.register_blueprint(GRC_bp)
    app.register_blueprint(Client_bp)
    app.register_blueprint(Geography_bp)
    app.register_blueprint(Client_ISAFACT_bp)
    app.register_blueprint(Client_DIVALTO_bp)
    app.register_blueprint(OperationDB_bp)
    app.register_blueprint(Geolocation_bp)
    app.register_blueprint(ClientContrat_bp)
    app.register_blueprint(MaintenanceDB_bp)
    app.register_blueprint(RessourcesMaterielDivalto_bp)

    return app
