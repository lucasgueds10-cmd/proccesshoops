import logging
import sys

from collectors.standings import collect_standings
from config import current_season
from writer import record_domain_result, write_standings

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)
logger = logging.getLogger("pipeline.main")


def run() -> bool:
    """Atualiza todos os domínios de dados da temporada atual.

    Cada domínio é isolado em seu próprio try/except: uma falha não impede
    a atualização dos demais, e o último JSON válido é preservado.
    """
    season = current_season()
    logger.info("Iniciando atualização da temporada %s", season)

    success = True

    try:
        payload = collect_standings(season)
        write_standings(season, payload.model_dump())
        record_domain_result(season, "standings", status="ok")
        logger.info("standings: OK (%s times)", len(payload.standings))
    except Exception as error:
        success = False
        logger.error("standings: FALHOU: %s: %s", type(error).__name__, error)
        record_domain_result(season, "standings", status="error", error=str(error))

    return success


if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
