import React from "react";
import { MapContainer, TileLayer, Marker } from "react-leaflet";
import "./CartographieClient.style.css"; // Assurez-vous que le chemin d'importation est correct
import "leaflet/dist/leaflet.css"; // Assurez-vous d'importer les styles CSS de Leaflet

const CartographieClient = () => {
  return (
<div className="CartographieClient-container card" style={{ height: '100%', width: '100%' }}>
  <div className="card-body" style={{ height: '100%', width: '100%' }}>
    <h5 className="card-title">Répartition géographique des clients  </h5>
    <hr />
    <p className="card-text">
      Ce widget permet de connaître la répartition géographique des clients :
    </p>
    <div className="card-map" style={{ height: '100%', width: '100%'}}>
      <MapContainer
        center={[48.8566, 2.3522]}
        zoom={5}
        style={{ height: '100%', width: '100%' }}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {/* Ajoutez ici vos marqueurs avec des composants Marker */}
      </MapContainer>
    </div>
    <hr />
    <button className="btn btn-primary">Détails</button>
  </div>
</div>
  );
};

export default CartographieClient;
