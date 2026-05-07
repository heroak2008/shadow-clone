from __future__ import annotations

from pathlib import Path

from digital_human.connectors.base import BaseConnector, CollectedRecord


class LocalFileConnector(BaseConnector):
    def collect(self) -> list[CollectedRecord]:
        paths = self.config.get("paths", [])
        records: list[CollectedRecord] = []
        for item in paths:
            p = Path(item)
            if not p.exists() or not p.is_file():
                continue
            records.append(
                CollectedRecord(
                    source_id=self.source_id,
                    source_type="local_files",
                    content=p.read_text(encoding="utf-8", errors="ignore"),
                    metadata={"path": str(p)},
                )
            )
        return records
