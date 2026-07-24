from typing import Literal

from pydantic import BaseModel, Field

StandingGroup = Literal["playoff", "play_in", "out"]


class TeamStanding(BaseModel):
    team_id: int
    team_name: str
    conference: Literal["East", "West"]
    division: str
    conference_rank: int = Field(ge=1)
    wins: int = Field(ge=0)
    losses: int = Field(ge=0)
    win_pct: float = Field(ge=0, le=1)
    last_10: str
    current_streak: str
    conference_games_back: str
    standing_group: StandingGroup


class StandingsPayload(BaseModel):
    season: str
    generated_at: str
    standings: list[TeamStanding]
