import React, { useState } from "react";
import "./HistoriqueClient.style.css";
import { useForm } from "react-hook-form";
import { apiService } from "../../services/API_think.service";

const HistoriqueClient = () => {
  /** CONSTANTES  */
  const {
    register,
    handleSubmit,
    setValue, // Ajout de setValue depuis useForm
    formState: { errors },
  } = useForm();

  /** STATES LOCAL */
  const [error, setError] = useState();
  const [data, setData] = useState([]);
  const [disabledButton, setDisabledButton] = useState(false);

  /** Methodes */
  const onSubmit = async (data) => {
    setDisabledButton(true);
    try {
      const response = await apiService.get(
        `/situation/?codeclient=${data.CodeClient}`
      );
      setData(response);
      console.log("Données récupérées avec succès:", response);
    } catch (error) {
      console.log("Erreur lors de la récupération des données:", error.message);
      setError(
        "Une erreur s'est produite lors de la récupération des données."
      );
    }
    setDisabledButton(false);
  };

  // Regroupement des données par 'numero_document'
  const groupedData = data.reduce((acc, item) => {
    if (!acc[item.numero_document]) {
      acc[item.numero_document] = [];
    }
    acc[item.numero_document].push(item);
    return acc;
  }, {});

  // Conversion de l'objet regroupé en tableau
  const groupedArray = Object.values(groupedData);                                                                                          

  console.log(groupedArray);

  // Fonction pour mettre à jour la valeur en majuscules à chaque changement
  const handleInputChange = (e) => {
    const value = e.target.value.toUpperCase();
    setValue("CodeClient", value); // Met à jour la valeur avec react-hook-form
  };

  /** render */
  return (
    <div className="historiqueClient-container container card p-1">
      <div className="card-header">
        <h4>Historique & Récapitulatif Client</h4>
      </div>

      <div className="card-body">
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="form-group row align-items-center"
        >
          <label htmlFor="" className="col-sm-2 col-form-label text-right">
            Numéro de Client :
          </label>
          <div className="col-sm-3">
            <input
              type="text"
              id="inputField"
              className="form-control p-1 m-1"
              maxLength={7}
              {...register("CodeClient")}
              onChange={handleInputChange} // Écoute les changements et met à jour en majuscules
            />
          </div>
          <div className="col-sm-3">
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
      <div className="card-body"></div>
    </div>
  );
};

export default HistoriqueClient;
