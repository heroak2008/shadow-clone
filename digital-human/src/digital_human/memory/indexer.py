from __future__ import annotations

from digital_human.memory.vector_store import VectorStore


class Indexer:
    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def index_chunks(self, chunks: list[str], source: str) -> None:
        for idx, chunk in enumerate(chunks):
            self.store.add(f"{source}-{idx}", chunk, {"source": source, "idx": idx})
