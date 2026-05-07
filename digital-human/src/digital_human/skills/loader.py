from __future__ import annotations

from pathlib import Path

import yaml

from digital_human.skills.schema import SkillDefinition, SkillVersion


class SkillLoader:
    def __init__(self, base_dir: str = ".") -> None:
        self.base_dir = Path(base_dir)

    def load_skill(self, skill_file: str) -> SkillDefinition:
        path = self.base_dir / skill_file
        with path.open("r", encoding="utf-8") as f:
            return SkillDefinition.model_validate(yaml.safe_load(f) or {})

    def save_skill(self, skill: SkillDefinition, skill_file: str) -> None:
        path = self.base_dir / skill_file
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(skill.model_dump(), f, allow_unicode=True, sort_keys=False)

    def version_skill(self, skill: SkillDefinition, versions_dir: str = "skills/versions") -> SkillVersion:
        version_file = f"{skill.id}.v{skill.version}.yaml"
        version_path = self.base_dir / versions_dir / version_file
        version_path.parent.mkdir(parents=True, exist_ok=True)
        with version_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(skill.model_dump(), f, allow_unicode=True, sort_keys=False)
        return SkillVersion(skill_id=skill.id, version=skill.version, file=str(version_path))

    def rollback(self, skill_id: str, version: int, target_file: str) -> SkillDefinition:
        version_file = self.base_dir / "skills" / "versions" / f"{skill_id}.v{version}.yaml"
        with version_file.open("r", encoding="utf-8") as f:
            skill = SkillDefinition.model_validate(yaml.safe_load(f) or {})
        self.save_skill(skill, target_file)
        return skill
