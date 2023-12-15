import { useEffect, useState } from "react";
import "./EtatTables.style.css";
import { apiService } from "../../../services/API_think.service";

const EtatTables = () => {
  const [sortedData, setSortedData] = useState([]);
  const [composantError, setComposantError] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await apiService.get("MaintenanceDB/etatBD");
        // Convertir les clés en minuscules avec la première lettre en majuscule
        const formattedData = Object.fromEntries(
          Object.entries(data).map(([key, value]) => [
            key.charAt(0).toUpperCase() + key.slice(1).toLowerCase(),
            value,
          ])
        );
        // Convertir les données en tableau pour faciliter le tri
        const dataArray = Object.entries(formattedData);
        // Trier le tableau en fonction des valeurs (de manière décroissante)
        dataArray.sort((a, b) => b[1] - a[1]);
        setSortedData(dataArray);
        // console.log("Données récupérées avec succès:", dataArray);
        // Faites quelque chose avec les données ici
      } catch (error) {
        // Gérez l'erreur ici
        console.log(error.message);
        setComposantError(true);
      }
    };

    fetchData();
  }, []);

  return (
    <div className=" card EtatTables-container">
      <div className="card-body">
        {composantError ? (
          <div class="alert alert-danger" role="alert">
            <strong>ERREUR : </strong> les données ne se sont pas importées.
          </div>
        ) : null}

        <h5 className="card-title">Etat des tables de la base de données</h5>
        <hr />
        <p className="card-text">
          Ce widget permet de connaitre l'état des tables de la base de données
          :
        </p>

        <ul>
          {sortedData.map(([key, value]) => (
            <li key={key}>
              <strong>{key}:</strong> {value}
            </li>
          ))}
        </ul>
        <hr />
        <button className="btn btn-primary">Détails</button>
      </div>
    </div>
  );
};

export default EtatTables;
