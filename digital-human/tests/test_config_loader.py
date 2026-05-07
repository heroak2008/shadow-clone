from pathlib import Path

from digital_human.config.loader import load_app_config, load_skills_config, load_sources_config


def test_load_default_configs() -> None:
    base = Path(__file__).resolve().parents[1] / "config"
    app = load_app_config(base)
    sources = load_sources_config(base)
    skills = load_skills_config(base)

    assert app.project_name == "digital-human"
    assert len(sources.sources) >= 1
    assert {s.id for s in skills.skills} == {"darwin", "nuwa"}
