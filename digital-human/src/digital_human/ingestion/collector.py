from __future__ import annotations

from digital_human.config.schema import Source
from digital_human.connectors.base import CollectedRecord
from digital_human.connectors.im_connector import IMConnector
from digital_human.connectors.local_file_connector import LocalFileConnector
from digital_human.connectors.wiki_connector import WikiConnector


class Collector:
    def __init__(self, sources: list[Source]) -> None:
        self.sources = [s for s in sources if s.enabled]

    def _build_connector(self, source: Source):
        if source.type == "im":
            return IMConnector(source.id, source.config)
        if source.type == "wiki":
            return WikiConnector(source.id, source.config)
        if source.type == "local_files":
            return LocalFileConnector(source.id, source.config)
        raise ValueError(f"Unknown source type: {source.type}")

    def run(self) -> list[CollectedRecord]:
        records: list[CollectedRecord] = []
        for source in self.sources:
            records.extend(self._build_connector(source).collect())
        return records
