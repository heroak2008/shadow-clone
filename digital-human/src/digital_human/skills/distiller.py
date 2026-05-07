from __future__ import annotations

from digital_human.skills.schema import SkillDefinition


class SkillDistiller:
    def distill(self, skill: SkillDefinition, materials: list[str]) -> SkillDefinition:
        distilled_hint = "\n\n# Distilled Insights\n" + "\n".join(materials[:5])
        return SkillDefinition(
            **skill.model_dump(),
            version=skill.version + 1,
            template=skill.template + distilled_hint,
        )
