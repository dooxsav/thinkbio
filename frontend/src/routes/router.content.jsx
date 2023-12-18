import React from "react";
import { Routes, Route } from "react-router-dom";

import Content from "../components/Content/content.component";
import Clients360 from "../components/Clients360/client360.component"; 
import HistoriqueClient from "../components/HistoriqueClient/HistoriqueClient.component";

const RouterContent = () => {
  return (
    <Routes>
      <Route path="/" element={<Content />} />
      <Route path="/clients360" element={<Clients360 />} />{" "}
      <Route path="/historiqueclient" element={<HistoriqueClient />} />{" "}
    </Routes>
  );
};

export default RouterContent;
