from __future__ import annotations

from digital_human.skills.schema import SkillDefinition

IDEAL_SAMPLE_COUNT = 10.0
IDEAL_TEMPLATE_LENGTH = 2000.0


class SkillEvaluator:
    def evaluate(self, skill: SkillDefinition, samples: list[str]) -> dict:
        sample_denominator = IDEAL_SAMPLE_COUNT or 1.0
        coverage = min(1.0, (len(samples) / sample_denominator))
        richness = min(1.0, len(skill.template) / IDEAL_TEMPLATE_LENGTH)
        return {
            "skill_id": skill.id,
            "version": skill.version,
            "coverage": round(coverage, 3),
            "richness": round(richness, 3),
            "score": round((coverage + richness) / 2, 3),
        }
