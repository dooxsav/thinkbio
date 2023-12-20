import React from "react";
import { useEffect } from "react";
import "./LandingPage.style.css"; // Assurez-vous que le chemin du fichier CSS est correct

import { useNavigate } from "react-router-dom";

import logo from "../../ressources/img/images-removebg-preview.png"; // Importez l'image avec le bon chemin relatif

const LandingPage = () => {
  const navigate = useNavigate();
  useEffect(() => {
    // Modifier le titre de la page lorsque le composant est monté
    document.title = "BIENVENUE";
  }, []);

  return (
    <div className="landing-page-container container-fluid">
      <div className="logo-app">
        {/* Utilisez l'image importée dans la balise <img> */}
        <img src={logo} alt="Logo" />
      </div>
      <div className="container-app card">
        <div className="container-title">
          <h2 className="display-5 fw-bold">#THINK</h2>
        </div>
        <div className="container-message">
          <h5>par BIONEST</h5>
          <p>- Application de suivi - </p>
        </div>
        <button
          type="button"
          className="btn btn-outline-primary btn-lg"
          onClick={() => {
            navigate("../home");
          }}
        >
          Accéder à l'application
        </button>
      </div>
    </div>
  );
};

export default LandingPage;
