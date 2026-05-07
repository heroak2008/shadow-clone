from __future__ import annotations

from datetime import datetime, timezone

from pydantic import BaseModel, Field


class SkillDefinition(BaseModel):
    id: str
    name: str
    description: str
    version: int
    template: str


class SkillVersion(BaseModel):
    skill_id: str
    version: int
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    reason: str = "distilled"
    file: str
