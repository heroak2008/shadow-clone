from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class CollectedRecord:
    source_id: str
    source_type: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    collected_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class BaseConnector(ABC):
    def __init__(self, source_id: str, config: dict[str, Any] | None = None) -> None:
        self.source_id = source_id
        self.config = config or {}

    @abstractmethod
    def collect(self) -> list[CollectedRecord]:
        raise NotImplementedError
