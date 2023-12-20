import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { apiService } from "../../services/API_think.service";

import "./HistoriqueClient.style.css";

const HistoriqueClient = () => {
  const [error, setError] = useState();
  const [data, setData] = useState([]);
  const [nomclient, setnomclient] = useState();
  const [prenomclient, setprenomclient] = useState();
  const [codepostal, setcodepostal] = useState();
  const [disabledButton, setDisabledButton] = useState(false);

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    setDisabledButton(true);
    try {
      const response = await apiService.get(
        `/situation/?codeclient=${data.CodeClient}`
      );
      setData(response);
      //console.log(response)
      setnomclient(response[0].nom); // Récupérer le nom depuis la réponse
      setprenomclient(response[0].prenom);
      setcodepostal(response[0].code_postal);
    } catch (error) {
      console.log("Erreur lors de la récupération des données:", error.message);
      setError(
        "Une erreur s'est produite lors de la récupération des données."
      );
    }
    setDisabledButton(false);
  };

  let columns = [];
  let rows = [];

  if (data.length > 0) {
    const groupedData = data.reduce((acc, item) => {
      if (!acc[item.numero_document]) {
        acc[item.numero_document] = {
          documents: [],
          totalMontantHT: 0,
        };
      }
      acc[item.numero_document].documents.push(item);
      acc[item.numero_document].totalMontantHT += item.montant_HT;
      return acc;
    }, {});

    const groupedArray = Object.values(groupedData);

    if (groupedArray.length > 0 && groupedArray[0].documents.length > 0) {
      const keys = Object.keys(groupedArray[0].documents[0]);

      // Filtrer les colonnes 'code_lot_facture' et 'date_livraison_document' des clés
      const filteredKeys = keys.filter(
        (key) =>
          key !== "code_lot_facture" &&
          key !== "date_livraison_document" &&
          key !== "CodeClient" &&
          key !== "compte_de_vente" &&
          key !== "id" &&
          key !== "volume" &&
          key !== "code_postal" &&
          key !== "quantite_unit" &&
          key !== "prenom" &&
          key !== "nom"
      );

      columns = filteredKeys.map((key) => {
        return {
          Header: key,
          accessor: key,
        };
      });

      rows = groupedArray.flatMap((group) =>
      group.documents.map((doc) => {
        const { code_lot_facture, date_livraison_document, montant_HT, ...rest } = doc; // Exclure certaines clés, y compris montant_HT
    
        // Arrondir la valeur de montant_HT à deux chiffres significatifs
        const roundedMontantHT = parseFloat(montant_HT).toFixed(2);
    
        const sanitizedRow = {
          ...rest,
          montant_HT: roundedMontantHT + " €", // Remplacer la valeur initiale de montant_HT par la version arrondie
        };
    
        // Remplacer les 'nan' par une chaîne vide
        Object.entries(sanitizedRow).forEach(([key, value]) => {
          if (value === 'nan') {
            sanitizedRow[key] = '';
          }
        });
    
        return sanitizedRow;
      })
    );
    }
  }
  // Définir l'ordre des colonnes souhaitées
  const desiredColumnOrder = [
    "date_document",
    "numero_document",
    "libelle_famille_tiers",
    "code_divers",
    "libelle_lot_facture",
    "code_famille_article",
    "libelle_famille_article",
    "code_article",
    "code_lot_articles",
    "nom_representant",
    "montant_HT",
  ];

  // Réorganiser les colonnes dans l'ordre souhaité
  columns = columns
    .filter((column) => desiredColumnOrder.includes(column.accessor))
    .sort(
      (a, b) =>
        desiredColumnOrder.indexOf(a.accessor) -
        desiredColumnOrder.indexOf(b.accessor)
    );

  const handleInputChange = (e) => {
    const value = e.target.value.toUpperCase();
    setValue("CodeClient", value);
  };

  return (
    <div className="Historiqueclient-container container card overflow-hidden">
      <div className="row border-right">
        <div className="col-3 text-center border-right">
          {/** Formulaire */}
          <form onSubmit={handleSubmit(onSubmit)}>
            <div className="row form-group m-1">
              <input
                type="text"
                id="inputField"
                className="col-6 form-control text-center"
                maxLength={7}
                {...register("CodeClient")}
                onChange={handleInputChange}
                placeholder="@CodeClient (ex: 5A12345)"
              />
              <button
                type="submit"
                className="btn btn-primary mt-1"
                disabled={disabledButton}
              >
                Obtenir informations
              </button>
            </div>
          </form>
        </div>
        <div className="col-9 text-center">
          {/** Carte du client */}
          <div className="row">
            <div className="row m-1 mt-2">
              <h6>
                <u>
                  <strong>INFORMATIONS CLIENT :</strong>
                </u>
              </h6>
            </div>
            <div className="row">
              <div className="col-1 text-end">
                <strong>NOM : </strong>
              </div>
              <div className="col-2 text-center border overflow-hidden">
                {nomclient}{" "}
              </div>
              <div className="col-2 text-end">
                <strong>PRENOM : </strong>
              </div>
              <div className="col-2 text-center border">{prenomclient} </div>
              <div className="col-2 text-end">
                <strong>CODE POSTAL : </strong>
              </div>
              <div className="col-2 text-center border">{codepostal} </div>
            </div>
          </div>
        </div>
      </div>
      <hr />
      <div className="row overflow-auto">
        <div className="col-12 historique-content">
          {/** Historique*/}
          <table className="custom-table table-striped">
            <thead>
              <tr>
                {columns.map((column) => (
                  <th key={column.accessor}>{column.Header}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rows.map((row, index) => (
                <tr key={index}>
                  {columns.map((column) => (
                    <td key={column.accessor}>{row[column.accessor]}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default HistoriqueClient;
