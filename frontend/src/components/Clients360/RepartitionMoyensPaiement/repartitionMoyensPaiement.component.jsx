import React, { useState, useEffect } from "react"; // Import de useState et useEffect depuis React

import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "react-chartjs-2";
import ChartDataLabels from "chartjs-plugin-datalabels";

import { apiService } from "../../../services/API_think.service";

ChartJS.register(ArcElement, Tooltip, Legend);

const RepartitionMoyensPaiement = () => {
  /** States locales */
  const [error, setError] = useState(); // Correction du nom de la variable d'état
  const [data, setData] = useState([]);

  /** Effet de BORD */
    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await apiService.get("/clientcontrat/lireall");
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
      }, [])

  /** Méthodes */
    /** Méthodes */
  // Utilisation de reduce pour regrouper par CODEGENRE et compter les occurrences
  const countByPaymentMethods = data.reduce((acc, currentValue) => {
    const { MODE_RGLT } = currentValue;

    // Si le CODEGENRE existe déjà, incrémente le compteur, sinon initialise à 1
    if (acc[MODE_RGLT]) {
      acc[MODE_RGLT].count++;
    } else {
      acc[MODE_RGLT] = {
        count: 1,
        // Autres champs du CODEGENRE, si nécessaire
      };
    }

    return acc;
  }, {});

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
    const keysMODE_RGLT = Object.keys(countByPaymentMethods);

    // Parcourir les clés et récupérer les valeurs associées à chaque clé
    keysMODE_RGLT.forEach((key) => {
      const value = countByPaymentMethods[key];
  
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
    <div className="repartitionmoyensPaiment-container">
      <div className="card-body">
        <div className="card-graphique">
          <h5 className="card-title text-center bg-light p-1">
            Répartition des Moyens de Paiement
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

export default RepartitionMoyensPaiement;
