export type StandingGroup = "playoff" | "play_in" | "out";

export interface TeamStanding {
  team_id: number;
  team_name: string;
  conference: "East" | "West";
  division: string;
  conference_rank: number;
  wins: number;
  losses: number;
  win_pct: number;
  last_10: string;
  current_streak: string;
  conference_games_back: string;
  standing_group: StandingGroup;
}

export interface StandingsPayload {
  season: string;
  generated_at: string;
  standings: TeamStanding[];
}
