import "./EtatTables.style.css";

const EtatTables = () => {
  return (
    <div className=" card EtatTables-container">
      <div className="card-body">
        <h5 className="card-title">Etat des tables de la base de données</h5>
        <p className="card-text">
          Ce widget permet de connaitre l'état des tables de la base de données
        </p>
        <button className="btn btn-primary">Détails</button>
      </div>
    </div>
  );
};

export default EtatTables;
