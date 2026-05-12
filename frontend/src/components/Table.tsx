import "./Table.css";
import { useQuery } from "@tanstack/react-query";
import type { OpeningWinrateType } from "../Types.ts";
export default function Table() {
  const fetchData = async (url: string) => {
    try {
      const res = await fetch(url, {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": import.meta.env
            .VITE_BACKEND_API_OPENING_WINRATE_URL,
        },
      });
      if (!res.ok) {
        throw new Error(`Error: Response Status ${res.status}`);
      }
      const data = await res.json();
      return data;
    } catch (e: any) {
      console.error(e.message);
    }
  };

  const { data: winrates, isLoading } = useQuery({
    queryFn: () =>
      fetchData(import.meta.env.VITE_BACKEND_API_OPENING_WINRATE_URL),
    queryKey: ["openings"],
  });

  if (isLoading) {
    return (
      <div>
        <p>Data Loading</p>
      </div>
    );
  }

  return (
    <div>
      {winrates?.map((winrate: OpeningWinrateType) => (
        <div key={winrate.opening}>{winrate.games_count}</div>
      ))}
    </div>
  );
}
