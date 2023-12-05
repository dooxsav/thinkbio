@echo off

REM Activation de l'environnement virtuel Python (backend)
cd thinkbio_backend
call venv\Scripts\activate  REM Assurez-vous de spécifier le chemin correct pour activer l'environnement virtuel Python

REM Lancement du backend
start cmd /k "python run.py"

REM Attente pour laisser le backend démarrer avant de lancer le frontend
timeout /t 5

REM Lancement du frontend
cd /D "%~dp0thinkbio_frontend"
start cmd /k "npm start"

pause