from app import create_app

# Créer une instance de l'application Flask
app = create_app()

if __name__ == '__main__':
    # Démarrer le serveur Flask
    app.run(debug=True)  # Mettez debug=False pour un déploiement en production
