from __future__ import annotations


class Chunker:
    @staticmethod
    def chunk(text: str, size: int = 500, overlap: int = 50) -> list[str]:
        if size <= 0:
            return [text]
        overlap = max(0, min(overlap, size - 1))
        chunks: list[str] = []
        start = 0
        while start < len(text):
            end = min(start + size, len(text))
            chunks.append(text[start:end])
            if end >= len(text):
                break
            start = end - overlap
        return chunks
