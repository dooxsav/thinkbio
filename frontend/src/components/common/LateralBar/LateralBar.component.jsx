import "./LateralBar.style.css";
import logo from "../../../ressources/img/images-removebg-preview.png"; // Importez l'image avec le bon chemin relatif

const LateralBar = () => {
  return (
    <div className="lateralbar-container">
      <div className="lateralbar-logo">
        <img src={logo} alt="" />
      </div>
    </div>
  );
};

export default LateralBar;
