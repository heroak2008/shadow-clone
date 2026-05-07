from __future__ import annotations

from pydantic import BaseModel

from digital_human.config.loader import load_skills_config
from digital_human.skills.loader import SkillLoader


class SkillResult(BaseModel):
    skill_id: str
    version: int
    task: str
    output: str


class SkillRuntime:
    def __init__(self, base_dir: str = ".") -> None:
        self.base_dir = base_dir
        self.loader = SkillLoader(base_dir)

    def list_skill_ids(self) -> list[str]:
        skills_cfg = load_skills_config(f"{self.base_dir}/config")
        return [s.id for s in skills_cfg.skills]

    def execute(self, skill_id: str, task: str) -> SkillResult:
        skills_cfg = load_skills_config(f"{self.base_dir}/config")
        refs = {s.id: s for s in skills_cfg.skills}
        if skill_id not in refs:
            raise ValueError(f"Skill not found: {skill_id}")
        skill = self.loader.load_skill(refs[skill_id].file)
        rendered = f"{skill.template}\n\n[Task]\n{task}"
        return SkillResult(skill_id=skill.id, version=skill.version, task=task, output=rendered)
