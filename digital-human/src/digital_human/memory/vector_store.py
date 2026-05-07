from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class VectorItem:
    id: str
    text: str
    metadata: dict


class VectorStore:
    def __init__(self) -> None:
        self.items: list[VectorItem] = []

    def add(self, item_id: str, text: str, metadata: dict) -> None:
        self.items.append(VectorItem(id=item_id, text=text, metadata=metadata))

    def search(self, query: str, limit: int = 5) -> list[VectorItem]:
        q_terms = set(query.lower().split())

        def score(text: str) -> int:
            return len(q_terms.intersection(set(text.lower().split())))

        ranked = sorted(self.items, key=lambda x: score(x.text), reverse=True)
        return [i for i in ranked if score(i.text) > 0][:limit]
