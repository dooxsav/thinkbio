import "./clients360.style.css";

import RepartitionClientsContrats from "./RepartitionClientsContrats/repartitionClientsContrats.component";
import RepartitionSystemesClients from "./RepartitionSystemesClients/repartitionSystemesClients.component";
import RepartitionMoyensPaiement from "./RepartitionMoyensPaiement/repartitionMoyensPaiement.component";

const Clients360 = () => {
  /** Render */
  return (
    <div className="client360-container container text-dark card p-1">
      <div className="card-header text-center">
        <h4>Infographie Client</h4>
      </div>
      <div className="client360-subcontainer">
        <div className="equal-height">
          <RepartitionClientsContrats />
        </div>
        <div className="equal-height">
          <RepartitionSystemesClients />
        </div>
        <div className="equal-height">
          <RepartitionMoyensPaiement />
        </div>
      </div>
    </div>
  );
};

export default Clients360; // Correction de la casse du nom du composant pour respecter les conventions (Clients360)
