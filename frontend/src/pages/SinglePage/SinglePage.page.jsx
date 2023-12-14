import "./SinglePage.style.css";

import LateralBar from "../../components/common/LateralBar/LateralBar.component";

const SinglePage = () => {
  return (
    <div className="main-container">
      <div className="navbar bg-light">navbar</div>
      <div className="lateralbar bg-dark container-fluid text-light">
        <LateralBar />
      </div>
      <div className="content">content</div>
    </div>
  );
};

export default SinglePage;
