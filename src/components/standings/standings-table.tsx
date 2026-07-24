import { cn } from "@/lib/utils";
import type { TeamStanding } from "@/types/standings";

const GROUP_STYLES: Record<TeamStanding["standing_group"], string> = {
  playoff: "border-l-4 border-l-emerald-500",
  play_in: "border-l-4 border-l-amber-500",
  out: "border-l-4 border-l-transparent",
};

function ConferenceTable({
  title,
  teams,
}: {
  title: string;
  teams: TeamStanding[];
}) {
  return (
    <div>
      <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-neutral-500">
        {title}
      </h2>
      <table className="w-full border-collapse text-sm">
        <thead>
          <tr className="border-b border-neutral-200 text-left text-neutral-500 dark:border-neutral-800">
            <th className="py-2 pr-2 font-medium">#</th>
            <th className="py-2 pr-2 font-medium">Time</th>
            <th className="py-2 pr-2 font-medium text-right">V</th>
            <th className="py-2 pr-2 font-medium text-right">D</th>
            <th className="py-2 pr-2 font-medium text-right">Aprov.</th>
            <th className="py-2 pr-2 font-medium text-right">Últimos 10</th>
            <th className="py-2 pr-2 font-medium text-right">Sequência</th>
            <th className="py-2 pl-2 font-medium text-right">JA</th>
          </tr>
        </thead>
        <tbody>
          {teams.map((team) => (
            <tr
              key={team.team_id}
              className={cn(
                "border-b border-neutral-100 dark:border-neutral-900",
                GROUP_STYLES[team.standing_group],
              )}
            >
              <td className="py-2 pr-2 pl-2">{team.conference_rank}</td>
              <td className="py-2 pr-2 font-medium">{team.team_name}</td>
              <td className="py-2 pr-2 text-right">{team.wins}</td>
              <td className="py-2 pr-2 text-right">{team.losses}</td>
              <td className="py-2 pr-2 text-right">
                {team.win_pct.toFixed(3)}
              </td>
              <td className="py-2 pr-2 text-right">{team.last_10}</td>
              <td className="py-2 pr-2 text-right">{team.current_streak}</td>
              <td className="py-2 pl-2 text-right">
                {team.conference_games_back}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export function StandingsTable({ standings }: { standings: TeamStanding[] }) {
  const east = standings.filter((team) => team.conference === "East");
  const west = standings.filter((team) => team.conference === "West");

  return (
    <div className="grid gap-10 md:grid-cols-2">
      <ConferenceTable title="Conferência Leste" teams={east} />
      <ConferenceTable title="Conferência Oeste" teams={west} />
    </div>
  );
}
