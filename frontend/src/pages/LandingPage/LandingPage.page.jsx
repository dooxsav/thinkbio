import React from "react";
import "./LandingPage.style.css"; // Assurez-vous que le chemin du fichier CSS est correct

import { useNavigate } from "react-router-dom";

import logo from "../../ressources/img/images-removebg-preview.png"; // Importez l'image avec le bon chemin relatif

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div className="landing-page-container container-fluid">
      <div className="logo-app">
        {/* Utilisez l'image importée dans la balise <img> */}
        <img src={logo} alt="Logo" />
      </div>
      <div className="container-app">
        <div className="container-title">
          <h2>Bienvenue !</h2>
        </div>
        <div className="container-message">
          <h5>#think</h5>
        </div>
        <button
          type="button"
          class="btn btn-outline-primary btn-lg"
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
