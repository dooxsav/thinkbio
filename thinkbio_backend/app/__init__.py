from flask import Flask
from app.routes import hello_bp

def create_app():
    app = Flask(__name__)

    # Configuration de l'application Flask, par exemple :
    # app.config['SECRET_KEY'] = 'your_secret_key'
    # ...

    # Importer les blueprints (routes) ici
    app.register_blueprint(hello_bp)

    return app