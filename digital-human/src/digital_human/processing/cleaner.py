from __future__ import annotations


class Cleaner:
    @staticmethod
    def clean(text: str) -> str:
        return "\n".join(line.strip() for line in text.splitlines() if line.strip())
