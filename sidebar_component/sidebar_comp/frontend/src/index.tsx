import React from "react"
import { createRoot } from "react-dom/client"
import OnHoverTabs from "./OnHoverTabs"

const container = document.getElementById("root") as HTMLElement
const root = createRoot(container)
root.render(
  <React.StrictMode>
    <OnHoverTabs />
  </React.StrictMode>
)
