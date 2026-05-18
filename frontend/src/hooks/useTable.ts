import { useQuery, useQueryClient } from "@tanstack/react-query";
import type { OpeningWinrateType } from "../Types";

export default function useTable() {
  const queryClient = useQueryClient();
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
      return;
    }
  };

  // ReactQuery: store fetched data in global state

  const { data: openings, isLoading } = useQuery({
    queryFn: () =>
      fetchData(import.meta.env.VITE_BACKEND_API_OPENING_WINRATE_URL),
    queryKey: ["openings"],
  });

  // ReactQuery: update data inside global state

  const sortOpeningBy = (sortBy: string) => {
    console.log("clicked");
    queryClient.setQueryData(
      ["openings"],
      (prevOpenings: OpeningWinrateType[]) => {
        let sortedOpenings = [...prevOpenings];
        switch (sortBy) {
          case "games_count":
            return sortedOpenings.sort((a, b) =>
              a.games_count > b.games_count
                ? -1
                : a.games_count < b.games_count
                  ? 1
                  : 0,
            );
          case "winrate":
            return sortedOpenings.sort((a, b) =>
              a.winrate > b.winrate ? -1 : a.winrate < b.winrate ? 1 : 0,
            );
          case "opening":
            return sortedOpenings.sort((a, b) =>
              a.opening > b.opening ? 1 : a.opening < b.opening ? -1 : 0,
            );
          case "color":
            return sortedOpenings.sort((a, b) =>
              a.color > b.color ? -1 : a.color < b.color ? 1 : 0,
            );
        }
      },
    );
  };

  return { fetchData, openings, isLoading, sortOpeningBy };
}
