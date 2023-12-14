import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import LandingPage from "../pages/LandingPage/LandingPage.page";
import SinglePage from "../pages/SinglePage/SinglePage.page";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/welcome" />} />
        <Route path="/welcome" element={<LandingPage />} />
        <Route path="/home" element={<SinglePage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
