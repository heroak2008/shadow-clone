from __future__ import annotations

import json
from pathlib import Path

from digital_human.connectors.base import CollectedRecord


class Archiver:
    def __init__(self, raw_dir: str) -> None:
        self.raw_dir = Path(raw_dir)

    def archive(self, records: list[CollectedRecord]) -> list[Path]:
        outputs: list[Path] = []
        for r in records:
            folder = self.raw_dir / r.source_type
            folder.mkdir(parents=True, exist_ok=True)
            target = folder / f"{r.source_id}-{r.collected_at.replace(':', '-')}.json"
            payload = {
                "source_id": r.source_id,
                "source_type": r.source_type,
                "content": r.content,
                "metadata": r.metadata,
                "collected_at": r.collected_at,
            }
            target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            outputs.append(target)
        return outputs
