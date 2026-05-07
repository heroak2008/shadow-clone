from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from digital_human.skills.runtime import SkillRuntime

app = FastAPI(title="digital-human")
runtime = SkillRuntime(base_dir=".")


class ExecuteRequest(BaseModel):
    skill_id: str
    task: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/skills")
def list_skills() -> dict[str, list[str]]:
    return {"skills": runtime.list_skill_ids()}


@app.post("/skills/execute")
def execute(req: ExecuteRequest) -> dict:
    try:
        result = runtime.execute(req.skill_id, req.task)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return result.model_dump()
