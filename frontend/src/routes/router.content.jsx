import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

const RouterContent = () => {
  return (
    <Routes>
      <Route path="/test" element={<Navigate to="/welcome" />} />
    </Routes>
  );
};

export default RouterContent;
