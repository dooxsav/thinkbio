import "./repartitionSystemesClients.style.css";

import React, { useState, useEffect } from "react"; // Import de useState et useEffect depuis React

import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "react-chartjs-2";
import ChartDataLabels from "chartjs-plugin-datalabels";

import { apiService } from "../../../services/API_think.service";

ChartJS.register(ArcElement, Tooltip, Legend);

const RepartitionSystemesClients = () => {
  /** States locales */
  const [error, setError] = useState(); // Correction du nom de la variable d'état
  const [data, setData] = useState([]);

  /** Chargement des données au montage du composant */
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await apiService.get(
          "/RessourcesMaterielDivalto/allmateriels"
        );
        setData(response);
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

  /** Méthodes */
  // Utilisation de reduce pour regrouper par CODEGENRE et compter les occurrences
  const countByGenre = data.reduce((acc, currentValue) => {
    const { CODEGENRE } = currentValue;

    // Si le CODEGENRE existe déjà, incrémente le compteur, sinon initialise à 1
    if (acc[CODEGENRE]) {
      acc[CODEGENRE].count++;
    } else {
      acc[CODEGENRE] = {
        count: 1,
        // Autres champs du CODEGENRE, si nécessaire
      };
    }

    return acc;
  }, {});

  const countByGenreAndBrand = data.reduce((acc, currentValue) => {
    const { CODEGENRE, MARQUE } = currentValue;
  
    // Si le CODEGENRE existe déjà dans l'accumulateur
    if (acc[CODEGENRE]) {
      // Si la marque existe déjà pour ce CODEGENRE
      if (acc[CODEGENRE][MARQUE]) {
        acc[CODEGENRE][MARQUE]++;
      } else {
        acc[CODEGENRE][MARQUE] = 1;
      }
    } else {
      // Si le CODEGENRE n'existe pas, l'initialise avec la marque à 1
      acc[CODEGENRE] = {
        [MARQUE]: 1,
      };
    }
  
    return acc;
  }, {});
  
 // console.log(countByGenreAndBrand);

  const doughnutData = {
    labels: [], // Initialisez un tableau vide pour les labels
    datasets: [
      {
        label: "Types de systèmes",
        data: [], // Initialisez un tableau vide pour les données
        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"],
      },
    ],
  };

  // Utilisation de Object.keys pour récupérer les clés de countByGenre
  const keysCODEGENRE = Object.keys(countByGenre);

  // Parcourir les clés et récupérer les valeurs associées à chaque clé
  keysCODEGENRE.forEach((key) => {
    const value = countByGenre[key];

    // Ajouter les clés aux labels
    doughnutData.labels.push(key);

    // Ajouter les valeurs correspondantes aux données
    doughnutData.datasets[0].data.push(value.count);
  });
  
  const options = {
    plugins: {
      datalabels: {
        color: "white",
        font: {
          weight: "bold",
        },
        formatter: (value, context) => {
          const percentage = ((value / data.length) * 100).toFixed(1); // Formatage du pourcentage à un chiffre après la virgule
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

  /** Render */
  return (
    <div className="repartitionSystemesClients-container">
      <div className="card-body">
        <div className="card-graphique">
          <h5 className="card-title text-center bg-light p-1">
            Répartition des systèmes
          </h5>
          {error && (
            <div className="alert alert-danger">
              <strong>Erreur de composant: </strong> {error}
            </div>
          )}{" "}
          <Doughnut
            data={doughnutData}
            options={options}
            plugins={[ChartDataLabels]}
            style={{ height: "100%", width: "100%" }}
          />
          <h6>
            <strong>(TOTAL ENREGISTREMENTS : {data.length} )</strong>
          </h6>
        </div>
      </div>
    </div>
  );
};

export default RepartitionSystemesClients;
