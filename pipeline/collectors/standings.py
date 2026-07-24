from datetime import datetime, timezone

from nba_api.stats.endpoints import leaguestandingsv3

from config import REQUEST_TIMEOUT_SECONDS
from models import StandingsPayload, StandingGroup, TeamStanding
from nba_client import fetch_with_retry


def _standing_group(conference_rank: int) -> StandingGroup:
    if conference_rank <= 6:
        return "playoff"
    if conference_rank <= 10:
        return "play_in"
    return "out"


def _format_games_back(value: float) -> str:
    if value == 0:
        return "-"
    return f"{value:g}"


def collect_standings(season: str) -> StandingsPayload:
    def _fetch():
        response = leaguestandingsv3.LeagueStandingsV3(
            season=season, timeout=REQUEST_TIMEOUT_SECONDS
        )
        return response.get_data_frames()[0]

    df = fetch_with_retry(_fetch)

    teams = [
        TeamStanding(
            team_id=int(row["TeamID"]),
            team_name=f'{row["TeamCity"]} {row["TeamName"]}',
            conference=row["Conference"],
            division=row["Division"],
            conference_rank=int(row["PlayoffRank"]),
            wins=int(row["WINS"]),
            losses=int(row["LOSSES"]),
            win_pct=float(row["WinPCT"]),
            last_10=row["L10"],
            current_streak=row["strCurrentStreak"],
            conference_games_back=_format_games_back(float(row["ConferenceGamesBack"])),
            standing_group=_standing_group(int(row["PlayoffRank"])),
        )
        for _, row in df.iterrows()
    ]
    teams.sort(key=lambda t: (t.conference, t.conference_rank))

    return StandingsPayload(
        season=season,
        generated_at=datetime.now(timezone.utc).isoformat(),
        standings=teams,
    )
