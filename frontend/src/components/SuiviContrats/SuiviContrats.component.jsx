import "./SuiviContrats.style.css";

import { useEffect, useState } from "react";
import { apiService } from "../../services/API_think.service";

import TableauContrat from "./tableaucontrats/tableaucontrats.component";
import GraphiqueContrats from "./graphiqueContrats/graphiqueContrats.component";

const SuiviContrats = () => {
  //** STATE LOCALE */
  const [Data, setData] = useState();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState();

  /** EFFETS DE BORD */
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await apiService.get("/clientcontrat/lireall");
        setData(response);
        setLoading(false);
        // console.log("Données récupérées avec succès:", response);
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
  /** METHODES */

  /** Render */
  return (
    <div className="suivicontrat-container container card">
      {loading ? (
        <>
          <div className="spinner-grow" role="status">
            <span className="sr-only"></span>
          </div>
          <span>
            <small>Chargement... </small>
          </span>
        </>
      ) : (
        <>
          <GraphiqueContrats data={Data} />
          <TableauContrat data={Data} />
        </>
      )}
    </div>
  );
};

export default SuiviContrats;
