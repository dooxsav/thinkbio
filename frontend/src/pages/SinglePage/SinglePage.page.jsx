import "./SinglePage.style.css";
import { useEffect } from "react";
import LateralBar from "../../components/common/LateralBar/LateralBar.component";
import Navbar from "../../components/common/NavBar/Navbar.component";
import RouterContent from "../../routes/router.content";

const SinglePage = () => {
  useEffect(() => {
    // Modifier le titre de la page lorsque le composant est monté
    document.title = "#Think Bionest";
  }, []);
  return (
    <div className="main-container">
      <div className="navbar bg-light container-fluid">
        <Navbar />
      </div>
      <div className="lateralbar bg-dark container-fluid text-light">
        <LateralBar />
      </div>
      <div className="content">
        <RouterContent />
      </div>
    </div>
  );
};

export default SinglePage;
