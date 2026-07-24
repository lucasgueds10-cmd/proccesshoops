import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from config import season_dir


def write_json_atomic(path: Path, payload: dict) -> None:
    """Escreve o JSON em arquivo temporário e renomeia por cima do destino.

    Evita que um processo interrompido no meio da escrita deixe um JSON
    corrompido/parcial no lugar de um dado válido anterior.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with open(fd, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        Path(tmp_path).replace(path)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise


def _read_meta(season: str) -> dict:
    meta_path = season_dir(season) / "meta.json"
    if meta_path.exists():
        return json.loads(meta_path.read_text(encoding="utf-8"))
    return {"season": season, "domains": {}}


def record_domain_result(
    season: str, domain: str, *, status: str, error: str | None = None
) -> None:
    """Atualiza meta.json com o resultado da coleta de um domínio.

    'updated_at' só avança quando status == 'ok', preservando o timestamp do
    último dado válido mesmo que a execução atual tenha falhado.
    """
    now = datetime.now(timezone.utc).isoformat()
    meta = _read_meta(season)
    domains = meta.setdefault("domains", {})
    entry = domains.get(domain, {})
    entry["status"] = status
    entry["last_attempt_at"] = now
    entry["error"] = error
    if status == "ok":
        entry["updated_at"] = now
    domains[domain] = entry
    meta["season"] = season
    meta["last_run_at"] = now
    write_json_atomic(season_dir(season) / "meta.json", meta)


def write_standings(season: str, payload: dict) -> None:
    write_json_atomic(season_dir(season) / "standings.json", payload)
