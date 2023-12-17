import "./repartitionClientsContrats.style.css";

import React, { useState, useEffect } from "react"; // Import de useState et useEffect depuis React

import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "react-chartjs-2";
import ChartDataLabels from "chartjs-plugin-datalabels";

import { apiService } from "../../../services/API_think.service";

ChartJS.register(ArcElement, Tooltip, Legend);

const RepartitionClientsContrats = () => {
  /** States locales */
  const [error, setError] = useState(); // Correction du nom de la variable d'état
  const [data, setData] = useState([]);

  /** Chargement des données au montage du composant */
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await apiService.get("/geolocation/sitecontrats");
        setData(response);
        console.log("Données récupérées avec succès:", response);
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
  const countECOcontract = data.filter(
    (item) => item.Contrat_Info.CodeTypeCONTRAT === "OUI.E"
  ).length;
  const countTRAcontract = data.filter(
    (item) => item.Contrat_Info.CodeTypeCONTRAT === "OUI.T"
  ).length;
  const countSMCcontract = data.filter(
    (item) => item.Contrat_Info.CodeTypeCONTRAT === "OUI.S"
  ).length;
  const countNONcontract = data.filter(
    (item) =>
      item.Contrat_Info.CodeTypeCONTRAT !== "OUI.T" &&
      item.Contrat_Info.CodeTypeCONTRAT !== "OUI.E" &&
      item.Contrat_Info.CodeTypeCONTRAT !== "OUI.S"
  ).length;
  const totalContract =
    countECOcontract + countTRAcontract + countSMCcontract + countNONcontract;

  /** Configuration du donuts */
  const doughnutData = {
    labels: ["Contrat ECO", "Contrat TRANQ", "Contrat SEMICO", "SANS Contrat"],
    datasets: [
      {
        label: "Types de contrats",
        data: [
          countECOcontract,
          countTRAcontract,
          countSMCcontract,
          countNONcontract,
        ],
        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"],
      },
    ],
  };
  const options = {
    plugins: {
      datalabels: {
        color: "white",
        font: {
          weight: "bold",
        },
        formatter: (value, context) => {
          const percentage = ((value / totalContract) * 100).toFixed(1); // Formatage du pourcentage à un chiffre après la virgule
          return (
            context.chart.data.labels[context.dataIndex] +
            ": " +
            percentage +
            " %"
          ); // Afficher le label et la valeur
        },
      },
    },
  };

  /** RENDER */
  return (
    <div
      className="repartitionClientsContrats-container"
      style={{ width: "100%", height: "100%" }}
    >
      <div className="card-body">
        {error && (
          <div className="alert alert-danger">
            <strong>Erreur de composant: </strong> {error}
          </div>
        )}{" "}
        <div className="card-graphique">
          <h5 class="card-title text-center bg-light p-1">
            Répartition clients contrats
          </h5>
          <Doughnut
            data={doughnutData}
            options={options}
            plugins={[ChartDataLabels]}
            style={{ height: "100%", width: "100%" }}
          />
          <h6>
            <strong>(TOTAL CLIENT : {totalContract} )</strong>
          </h6>
        </div>
        {/* Affichage de l'erreur */}
      </div>
    </div>
  );
};

export default RepartitionClientsContrats;
