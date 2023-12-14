import "./SinglePage.style.css";

import LateralBar from "../../components/common/LateralBar/LateralBar.component";
import Navbar from "../../components/common/NavBar/Navbar.component";
import RouterContent from "../../routes/router.content";

const SinglePage = () => {
  return (
    <div className="main-container">
      <div className="navbar bg-light">
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
