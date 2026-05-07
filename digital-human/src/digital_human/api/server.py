from __future__ import annotations

import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from digital_human.skills.runtime import SkillRuntime

app = FastAPI(title="digital-human")


class ExecuteRequest(BaseModel):
    skill_id: str
    task: str


def _runtime() -> SkillRuntime:
    return SkillRuntime(base_dir=os.getenv("DIGITAL_HUMAN_BASE_DIR", "."))


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/skills")
def list_skills() -> dict[str, list[str]]:
    return {"skills": _runtime().list_skill_ids()}


@app.post("/skills/execute")
def execute(req: ExecuteRequest) -> dict:
    try:
        result = _runtime().execute(req.skill_id, req.task)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return result.model_dump()
