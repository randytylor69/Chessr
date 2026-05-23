import "./Header.css";
import { useState } from "react";
import { GoArrowUpRight } from "react-icons/go";
export default function Header() {
  const [currentTab, setCurrentTab] = useState<number>(0);
  const headerElements = [
    {
      name: "Lichess API",
      subscript: null,
      id: 0,
      type: "link",
      URL: "https://lichess.org/account/oauth/token/create",
    },
    {
      name: "GitHub",
      subscript: null,
      id: 1,
      type: "link",
      URL: "https://github.com/RandyTylor69/Chessr",
    },
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
              borderLeft: el.id == 0 ? "var(--black-secondary) 2px solid" : "",
            }}
          >
            {el.type == "link" ? (
              <a href={el.URL} target="_blank">
                {el.name} <GoArrowUpRight />
              </a>
            ) : (
              <h3>{el.name}</h3>
            )}

            <p>{el.subscript}</p>
          </section>
        ))}
      </div>
    </div>
  );
}
