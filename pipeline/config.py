from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "nba"

REQUEST_TIMEOUT_SECONDS = 30
MAX_RETRIES = 3
RETRY_BACKOFF_BASE_SECONDS = 2


def current_season(today: date | None = None) -> str:
    """Retorna a temporada NBA vigente no formato 'YYYY-YY'.

    A temporada nova começa em outubro: de outubro em diante já é a
    temporada que termina no ano seguinte (ex.: outubro/2026 -> '2026-27').
    """
    today = today or date.today()
    start_year = today.year if today.month >= 10 else today.year - 1
    return f"{start_year}-{str(start_year + 1)[-2:]}"


def season_dir(season: str) -> Path:
    return DATA_DIR / season
