from __future__ import annotations


class Deduplicator:
    @staticmethod
    def deduplicate(items: list[str]) -> list[str]:
        seen: set[str] = set()
        unique: list[str] = []
        for item in items:
            key = item.strip()
            if key and key not in seen:
                seen.add(key)
                unique.append(item)
        return unique
