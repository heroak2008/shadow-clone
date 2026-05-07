from __future__ import annotations

from digital_human.connectors.base import BaseConnector, CollectedRecord


class IMConnector(BaseConnector):
    def collect(self) -> list[CollectedRecord]:
        group_ids = self.config.get("group_ids", [])
        records: list[CollectedRecord] = []
        for gid in group_ids:
            records.append(
                CollectedRecord(
                    source_id=self.source_id,
                    source_type="im",
                    content=f"[MOCK IM] group={gid} 用户A: 今日同步完成。",
                    metadata={"group_id": gid, "mode": self.config.get("export_mode", "mock")},
                )
            )
        return records
