import "./LateralBar.style.css";
import { useNavigate } from "react-router-dom";
import logo from "../../../ressources/img/images-removebg-preview.png"; // Importez l'image avec le bon chemin relatif

const LateralBar = () => {
  /** constantes */
  const navigate = useNavigate();

  return (
    <div className="lateralbar-container">
      <div className="lateralbar-logo">
        <img src={logo} alt="" />
      </div>
      <div className="lateralbar-content">
        <div className="lateralbar-Menu">
          <h5>📖 MENU</h5>
          <h6
            onClick={() => {
              navigate("./");
            }}
          >
            {" "}
            🧭 Accueil
          </h6>
          <h6
            onClick={() => {
              navigate("./clients360");
            }}
          >
            {" "}
            ✔️ Infographie Clients
          </h6>
          <h6
            onClick={() => {
              navigate("./historiqueclient");
            }}
          >
            {" "}
            ✔️ Historique Client
          </h6>
        </div>
      </div>
    </div>
  );
};

export default LateralBar;
