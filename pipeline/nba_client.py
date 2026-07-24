import logging
import time
from typing import Callable, TypeVar

from config import MAX_RETRIES, RETRY_BACKOFF_BASE_SECONDS

logger = logging.getLogger("pipeline.nba_client")

T = TypeVar("T")


def fetch_with_retry(fetch_fn: Callable[[], T]) -> T:
    """Executa fetch_fn com retry e backoff exponencial.

    A stats.nba.com (usada pela nba_api) é conhecida por respostas
    instáveis a partir de IPs de datacenter. Isso isola essa incerteza
    num único lugar, sem espalhar try/except pelos collectors.
    """
    last_error: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return fetch_fn()
        except Exception as error:  # nba_api pode levantar tipos variados
            last_error = error
            logger.warning(
                "Tentativa %s/%s falhou: %s: %s",
                attempt,
                MAX_RETRIES,
                type(error).__name__,
                error,
            )
            if attempt < MAX_RETRIES:
                sleep_seconds = RETRY_BACKOFF_BASE_SECONDS**attempt
                time.sleep(sleep_seconds)

    assert last_error is not None
    raise last_error
