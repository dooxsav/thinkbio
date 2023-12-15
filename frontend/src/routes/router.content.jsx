import React from "react";
import { Routes, Route } from "react-router-dom";
import Content from "../components/Content/content.component";

const RouterContent = () => {
  return (
    <Routes>
      <Route path="/" element={< Content />} />
    </Routes>
  );
};

export default RouterContent;
