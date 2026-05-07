from __future__ import annotations

from digital_human.memory.vector_store import VectorStore


class Retriever:
    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def retrieve(self, query: str, limit: int = 5) -> list[dict]:
        return [item.__dict__ for item in self.store.search(query, limit=limit)]
