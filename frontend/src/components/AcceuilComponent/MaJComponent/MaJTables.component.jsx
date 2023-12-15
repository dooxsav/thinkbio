import "./MaJTables.style.css";
import { useForm } from "react-hook-form";

const MaJTables = () => {
  const { register, handleSubmit, errors } = useForm();
  const onSubmit = (data) => {
    const { clientFile, situationFile } = data;
    // Traiter les fichiers ici (clientFile et situationFile)
    console.log("Fichier client ISAFACT:", clientFile);
    console.log("Fichier situation ISAFACT:", situationFile);
  };

  return (
    <div className="card MaJTables-container">
      <div className="card-body">
        <h5 className="card-title">
          Mettre à jour les tables de la base de données
        </h5>
        <hr />
        <p className="card-text">
          Ce widget permet la mise à jour des tables de la base de données
        </p>
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className="isafact-form">
            <label>Fichier Client ISAFACT: </label>
            <input className='btn' type="file" name="clientFile" {...register('clientFile')} />
          </div>
          <div className="isafact-form">
            <label>Fichier SITUATION ISAFACT: </label>
            <input className='btn' type="file" name="situationFile" {...register('situationFile')} />
          </div>
          <div>
            <button type="submit" className="btn btn-secondary">Envoyer</button>
          </div>
        </form>
        <hr />
        <button className="btn btn-primary">Détails</button>
      </div>
    </div>
  );
};

export default MaJTables;
