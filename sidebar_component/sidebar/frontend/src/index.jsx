import React from "react";
import { createRoot } from "react-dom/client";
import SideNav from "./SideNav";

const container = document.getElementById("root");
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <SideNav />
  </React.StrictMode>
);
