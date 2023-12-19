import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { apiService } from "../../services/API_think.service";

import "./HistoriqueClient.style.css";

const HistoriqueClient = () => {
  const [error, setError] = useState();
  const [data, setData] = useState([]);
  const [nomclient, setnomclient] = useState()
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
      setnomclient(response.nom) ; // Récupérer le nom depuis la réponse
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
          key !== "quantite_unit"
      );

      columns = filteredKeys.map((key) => {
        return {
          Header: key,
          accessor: key,
        };
      });

      rows = groupedArray.flatMap((group) =>
        group.documents.map((doc) => {
          const { code_lot_facture, date_livraison_document, ...rest } = doc; // Exclure code_lot_facture et date_livraison_document
          const sanitizedRow = {};

          Object.entries(rest).forEach(([key, value]) => {
            if (value !== "nan") {
              sanitizedRow[key] = value;
            }
          });

          return sanitizedRow;
        })
      );
    }
  }

  const handleInputChange = (e) => {
    const value = e.target.value.toUpperCase();
    setValue("CodeClient", value);
  };


  return (
    <div className="historiqueClient-container container card p-1">
      <div className="card-header">
        <h4>Historique & Récapitulatif Client</h4>
      </div>
      <div className="card-entete">
        <div className="card-body">
          <form
            onSubmit={handleSubmit(onSubmit)}
            className="form-group row align-items-center"
          >
            <label htmlFor="" className="col-form-label">
              Numéro de Client :
            </label>
            <div className="col-sm-3">
              <input
                type="text"
                id="inputField"
                className="form-control p-1 m-1"
                maxLength={7}
                {...register("CodeClient")}
                onChange={handleInputChange}
              />
            </div>
            <div className="col">
              <button
                type="submit"
                className="btn btn-primary btn-lg"
                disabled={disabledButton}
              >
                Accéder
              </button>
            </div>
          </form>
        </div>
        <div className="card-client">
          <div className="card-client-label">
            <strong>Prénom : </strong> 
          </div>
          <div className="card-client-label">
          <strong>Nom : {nomclient || "vide"} </strong> 
          </div>
          
        </div>
      </div>

      <div className="card-body">
        <table className="custom-table">
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
  );
};

export default HistoriqueClient;
