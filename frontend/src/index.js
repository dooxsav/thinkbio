import React from "react";
import ReactDOM from "react-dom/client";

import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";

import Router from "../src/routes/Routes.main";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <Router />
  </React.StrictMode>
);
