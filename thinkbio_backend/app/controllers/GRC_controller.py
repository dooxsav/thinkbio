# controler/GRC_controller
# import des services
import os
from flask import jsonify
from datetime import datetime
from app.services import extract_text_from_pdf, search_patterns, create_excel_file



def extraction_GRC(pdf_file):
    # Gestion des chemins des fichiers :
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Récupérer le répertoire du fichier actuel (GRC_controller.py)
    path_to_input = os.path.join(current_directory, '..', '..', 'ressources', 'input', 'GRC')  # Chemin vers le répertoire "ressources/input"
    
    # Gestion du nommage : 
    datefichier = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Formater la date
    nom_fichier = f"input_{datefichier}.pdf"  # Créer un nom de fichier pour sauvegarder le fichier PDF
    file_path = os.path.join(path_to_input, nom_fichier)  # Chemin complet du fichier à enregistrer
    
    # Sauvegarder le fichier avec un nom spécifique dans le dossier spécifié
    pdf_file.save(file_path)
    
    # Extraire les informtions du pdf
    extracted_text = extract_text_from_pdf(file_path)
    
    # Appelez la fonction de recherche de motifs avec le texte extrait
    pattern_results = search_patterns(extracted_text)
    
    # Créez un fichier Excel temporaire en utilisant la fonction du module excel_export
    excel_file = create_excel_file(pattern_results)

    return jsonify({"message" : "job done"})