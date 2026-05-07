from __future__ import annotations

from datetime import datetime, timezone


def annotate_metadata(content: str, source_type: str, source_id: str) -> dict[str, str | int]:
    return {
        "source_type": source_type,
        "source_id": source_id,
        "length": len(content),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
