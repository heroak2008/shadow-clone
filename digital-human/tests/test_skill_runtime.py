from pathlib import Path

from digital_human.skills.runtime import SkillRuntime


def test_runtime_execute_returns_structured_result() -> None:
    base_dir = str(Path(__file__).resolve().parents[1])
    runtime = SkillRuntime(base_dir=base_dir)

    result = runtime.execute("darwin", "总结最近知识")

    assert result.skill_id == "darwin"
    assert result.version >= 1
    assert "[Task]" in result.output
