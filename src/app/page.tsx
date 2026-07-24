import { StandingsTable } from "@/components/standings/standings-table";
import { getStandings } from "@/lib/data";

export default function Home() {
  const data = getStandings();
  const updatedAt = new Date(data.generated_at).toLocaleString("pt-BR", {
    dateStyle: "short",
    timeStyle: "short",
  });

  return (
    <main className="mx-auto max-w-5xl px-4 py-10">
      <h1 className="text-2xl font-semibold">processhoops analytics</h1>
      <p className="mt-1 text-sm text-neutral-500">
        Temporada {data.season} · atualizado em {updatedAt}
      </p>

      <div className="mt-8">
        <StandingsTable standings={data.standings} />
      </div>
    </main>
  );
}
