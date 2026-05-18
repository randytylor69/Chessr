import "./Header.css";
import { useState } from "react";
export default function Header() {
  const [currentTab, setCurrentTab] = useState<number>(0);
  const headerElements = [
    { name: "Openings", subscript: 20, id: 0 },
    { name: "Rating", subscript: 1784, id: 1 },
    { name: "...", subscript: null, id: 2 },
  ];

  return (
    <div className="header-wrapper">
      <div className="header-container">
        <section className="logo-container">
          <h1>Chessr</h1>
        </section>
        {headerElements.map((el) => (
          <section
            onClick={() => setCurrentTab(el.id)}
            className="header-tab-container"
            style={{
              /*             backgroundColor:
                el.id == currentTab
                  ? "var(--black-primary)"
                  : "var(--white-primary)",
              color:
                el.id == currentTab
                  ? "var(--white-primary)"
                  : "var(--black-primary)", */
              borderLeft: el.id == 0 ? "var(--black-secondary) 2px solid" : "",
            }}
          >
            <h3>{el.name}</h3>
            <p>{el.subscript}</p>
          </section>
        ))}
      </div>
    </div>
  );
}
