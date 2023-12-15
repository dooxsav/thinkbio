import "./CartographieClient.style.css";

const CartographieClient = () => {
  return (
    <div className="CartographieClient-container card">
      <div className="card-body">
        <h5 className="card-title">Répartition géographique des clients</h5>
        <p className="card-text">
          Ce widget permet de connaitre la répartition géographique des clients
        </p>
        <button className="btn btn-primary">Détails</button>
      </div>
    </div>
  );
};

export default CartographieClient;
