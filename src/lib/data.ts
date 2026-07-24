import fs from "node:fs";
import path from "node:path";
import type { StandingsPayload } from "@/types/standings";

const DATA_DIR = path.join(process.cwd(), "data", "nba");

/**
 * Descobre a temporada mais recente disponível em data/nba, em vez de
 * fixar um valor no front-end. Isso mantém o cálculo de "temporada atual"
 * concentrado apenas no pipeline Python (config.py), como definido na
 * arquitetura do projeto.
 */
function getLatestSeason(): string {
  const seasons = fs
    .readdirSync(DATA_DIR, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort();

  const latest = seasons.at(-1);
  if (!latest) {
    throw new Error(`Nenhuma temporada encontrada em ${DATA_DIR}`);
  }
  return latest;
}

export function getStandings(): StandingsPayload {
  const season = getLatestSeason();
  const filePath = path.join(DATA_DIR, season, "standings.json");
  const raw = fs.readFileSync(filePath, "utf-8");
  return JSON.parse(raw) as StandingsPayload;
}
