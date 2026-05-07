from __future__ import annotations

import csv
import json
from pathlib import Path

from bs4 import BeautifulSoup
from docx import Document
from pypdf import PdfReader


class Parser:
    def parse_path(self, path: str | Path) -> str:
        p = Path(path)
        suffix = p.suffix.lower()
        if suffix in {".md", ".txt"}:
            return p.read_text(encoding="utf-8", errors="ignore")
        if suffix == ".json":
            return json.dumps(json.loads(p.read_text(encoding="utf-8")), ensure_ascii=False)
        if suffix == ".csv":
            rows = []
            with p.open("r", encoding="utf-8", errors="ignore") as f:
                for row in csv.reader(f):
                    rows.append(", ".join(row))
            return "\n".join(rows)
        if suffix in {".html", ".htm"}:
            raw = p.read_text(encoding="utf-8", errors="ignore")
            return BeautifulSoup(raw, "html.parser").get_text("\n")
        if suffix == ".pdf":
            reader = PdfReader(str(p))
            return "\n".join(page.extract_text() or "" for page in reader.pages)
        if suffix == ".docx":
            doc = Document(str(p))
            return "\n".join(par.text for par in doc.paragraphs)
        return p.read_text(encoding="utf-8", errors="ignore")
