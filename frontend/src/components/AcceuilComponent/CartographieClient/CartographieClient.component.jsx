import React from "react";
import { useForm } from "react-hook-form";
import { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";

import { apiService } from "../../../services/API_think.service";

import "./CartographieClient.style.css"; // Assurez-vous que le chemin d'importation est correct
import "leaflet/dist/leaflet.css"; // Assurez-vous d'importer les styles CSS de Leaflet

import markerIconPng from "leaflet/dist/images/marker-icon.png";
import { Icon } from "leaflet";

const CartographieClient = () => {
  /** States LOCALE */
  const [mapData, setMapData] = useState([]);
  const [error, setError] = useState(null);
  const [showWithoutContract, setShowWithoutContract] = useState(false);
  const [showECOContract, setShowECOContract] = useState(false);
  const [showTRAContract, setShowTRAContract] = useState(false);

  /** Effet de BORD */
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await apiService.get("/geolocation/sitecontrats");
        console.log("Données récupérées avec succès:", response);
        setMapData(response);
      } catch (error) {
        console.log(
          "Erreur lors de la récupération des données:",
          error.message
        );
        setError(
          "Une erreur s'est produite lors de la récupération des données."
        );
      }
    };
    fetchData();
  }, []);

  /** Methodes */
  // Fonction pour gérer le changement d'état de la case à cocher
  const handleCheckboxChange = () => {
    setShowWithoutContract(!showWithoutContract);
  };
  // Filtrer les données pour obtenir les clients sans contrat
  const clientsSansContrat = mapData.filter(
    (item) => item.Contrat_Info.CodeCONTRAT === null
  );

  // Fonction pour gérer le changement d'état de la case à cocher pour les contrats de type "ECO"
  const handleECOContractChange = () => {
    setShowECOContract(!showECOContract);
  };

  // Filtrer les données pour obtenir les clients avec contrat de type "ECO"
  const clientsAvecContratECO = mapData.filter(
    (item) => item.Contrat_Info.CodeTypeCONTRAT === "OUI.E"
  );

  // Fonction pour gérer le changement d'état de la case à cocher pour les contrats de type "TRA"
  const handleTRAContractChange = () => {
    setShowTRAContract(!showTRAContract);
  };

  // Filtrer les données pour obtenir les clients avec contrat de type "TRA"
  const clientsAvecContratTRA = mapData.filter(
    (item) => item.Contrat_Info.CodeTypeCONTRAT === "OUI.T"
  );

  /** RENDER */
  return (
    <div
      className="CartographieClient-container card"
      style={{ height: "65%", width: "100%" }}
    >
      <div className="card-body">
        {error && <div className="error-message">{error}</div>}
        <h5 className="card-title">Répartition géographique des clients </h5>
        <hr />
        <p className="card-text">
          Ce widget permet de connaître la répartition géographique des clients
          :
        </p>
        <div className="card-control">
          <div className="form-check">
            <input
              className="form-check-input"
              type="checkbox"
              value=""
              onChange={handleCheckboxChange}
            />
            <label className="form-check-label card-text" htmlFor="">
              Clients sans contrat
            </label>
          </div>
          <div className="form-check">
            <input
              className="form-check-input"
              type="checkbox"
              value=""
              id="ecoContractCheckbox"
              onChange={handleECOContractChange}
            />
            <label
              className="form-check-label card-text"
              htmlFor="ecoContractCheckbox"
            >
              Clients sous contrat ECO
            </label>
          </div>

          <div className="form-check">
            <input
              className="form-check-input"
              type="checkbox"
              value=""
              id="traContractCheckbox"
              onChange={handleTRAContractChange}
            />
            <label
              className="form-check-label card-text"
              htmlFor="traContractCheckbox"
            >
              Clients sous contrat TRANQ
            </label>
          </div>
        </div>
        <div className="card-map" style={{ height: "70%", width: "100%" }}>
          <MapContainer
            center={[46.603354, 1.888334]}
            zoom={6}
            style={{ height: "100%", width: "100%" }}
          >
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

            {/* Utiliser map() pour créer des marqueurs pour chaque position des clients sans contrat */}
            {showWithoutContract &&
              clientsSansContrat.map((item, index) => (
                <Marker
                  key={index}
                  position={[item.Site_Info.latitude, item.Site_Info.longitude]}
                  icon={
                    new Icon({
                      iconUrl: markerIconPng,
                      iconSize: [12, 20], // Nouvelle taille de l'icône [largeur, hauteur]
                      iconAnchor: [6, 20],
                    })
                  }
                >
                  {/* Popup pour afficher des informations supplémentaires */}
                  <Popup>
                    <div>
                      <p>Client ID: {item.Site_Info.Client_id}</p>
                      <p>Code Client: {item.Site_Info.CodeClient}</p>
                      {/* Ajoutez d'autres informations si nécessaire */}
                    </div>
                  </Popup>
                </Marker>
              ))}

            {showECOContract &&
              clientsAvecContratECO.map((item, index) => (
                <Marker
                  key={index}
                  position={[item.Site_Info.latitude, item.Site_Info.longitude]}
                  icon={
                    new Icon({
                      iconUrl: markerIconPng,
                      iconSize: [12, 20],
                      iconAnchor: [6, 20],
                    })
                  }
                >
                  <Popup>
                    <div>
                      <p>Client ID: {item.Site_Info.Client_id}</p>
                      <p>Code Client: {item.Site_Info.CodeClient}</p>
                      {/* Autres informations si nécessaire */}
                    </div>
                  </Popup>
                </Marker>
              ))}

            {showTRAContract &&
              clientsAvecContratTRA.map((item, index) => (
                <Marker
                  key={index}
                  position={[item.Site_Info.latitude, item.Site_Info.longitude]}
                  icon={
                    new Icon({
                      iconUrl: markerIconPng,
                      iconSize: [12, 20],
                      iconAnchor: [6, 20],
                    })
                  }
                >
                  <Popup>
                    <div>
                      <p>Client ID: {item.Site_Info.Client_id}</p>
                      <p>Code Client: {item.Site_Info.CodeClient}</p>
                      {/* Autres informations si nécessaire */}
                    </div>
                  </Popup>
                </Marker>
              ))}
          </MapContainer>
        </div>
        <hr />
        <button className="btn btn-primary">Détails</button>
      </div>
    </div>
  );
};

export default CartographieClient;
