from __future__ import annotations

import requests

from digital_human.connectors.base import BaseConnector, CollectedRecord


class WikiConnector(BaseConnector):
    def collect(self) -> list[CollectedRecord]:
        urls = self.config.get("urls", [])
        records: list[CollectedRecord] = []
        for url in urls:
            text: str
            try:
                text = requests.get(url, timeout=10).text
            except Exception:
                text = f"[MOCK WIKI] {url}"
            records.append(
                CollectedRecord(
                    source_id=self.source_id,
                    source_type="wiki",
                    content=text,
                    metadata={"url": url},
                )
            )
        return records
