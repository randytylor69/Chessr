import "./Table.css";
import { useState } from "react";

import useTable from "../hooks/useTable";
export default function Table() {
  const [sortBy, setSortBy] = useState<string>(sorting_options[0].key);
  const { openings, isLoading, sortOpeningBy } = useTable();

  if (isLoading) {
    return (
      <div>
        <p>Data Loading</p>
      </div>
    );
  }

  return (
    <div className="table-container">
      <div className="table-title-container">
        <h1>Your Openings</h1>
      </div>
      <div className="table-content-wrapper">
        {/** --- sorting handler --- */}
        <section className="table-sorting-container">
          <div className="sorting-tabs-container">
            {sorting_options.map((option) => (
              <button
                key={option.id}
                className="sorting-option"
                onClick={() => {
                  sortOpeningBy(option.key);
                  setSortBy(option.key);
                }}
                style={{
                  color: sortBy == option.key ? "var(--blue-primary)" : "black",
                }}
              >
                <h3>{option.name}</h3>
              </button>
            ))}
          </div>
        </section>
        {/** --- actual table grid --- */}
        <section className="table-openings-container">
          {openings.map((op: any) => (
            <div key={op.opening} className="opening-row-wrapper">
              <div className="opening-name">
                <h3>{op.opening.split(":")[0]}</h3>
                {op.opening.split(":").length > 1 && (
                  <h5>{op.opening.split(":")[1]}</h5>
                )}
              </div>
              <div className="opening-games">
                <p>{op.games_count} games</p>
              </div>
              <div className="opening-color">
                <p>{op.color}</p>
              </div>
              <div className="opening-winrate">
                <p>{(op.winrate * 100).toFixed(2)}%</p>
              </div>
            </div>
          ))}
        </section>
      </div>
    </div>
  );
}

const sorting_options = [
  { id: 0, name: "Sort by Games", key: "games_count" },
  { id: 1, name: "Sort by Win Rate", key: "winrate" },
  { id: 2, name: "Sort by Name", key: "opening" },
  { id: 3, name: "Sort by Color", key: "color" },
];
