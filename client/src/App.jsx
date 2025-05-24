import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./components/Home";
const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="*"
          element={
            <div
              style={{
                height: "100dvh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <p style={{ alignSelf: "center" }}>Not Found</p>
            </div>
          }
        />
      </Routes>
    </Router>
  );
};

export default App;
