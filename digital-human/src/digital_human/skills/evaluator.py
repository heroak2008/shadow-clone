from __future__ import annotations

from digital_human.skills.schema import SkillDefinition


class SkillEvaluator:
    def evaluate(self, skill: SkillDefinition, samples: list[str]) -> dict:
        coverage = min(1.0, (len(samples) / 10.0))
        richness = min(1.0, len(skill.template) / 2000.0)
        return {
            "skill_id": skill.id,
            "version": skill.version,
            "coverage": round(coverage, 3),
            "richness": round(richness, 3),
            "score": round((coverage + richness) / 2, 3),
        }
