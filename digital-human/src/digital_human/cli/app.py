from __future__ import annotations

import typer

from digital_human.config.loader import load_app_config, load_sources_config
from digital_human.ingestion.archiver import Archiver
from digital_human.ingestion.collector import Collector
from digital_human.skills.runtime import SkillRuntime

app = typer.Typer(help="Digital Human CLI")


@app.command("list-skills")
def list_skills(base_dir: str = ".") -> None:
    runtime = SkillRuntime(base_dir=base_dir)
    for sid in runtime.list_skill_ids():
        typer.echo(sid)


@app.command("run-skill")
def run_skill(skill_id: str, task: str, base_dir: str = ".") -> None:
    runtime = SkillRuntime(base_dir=base_dir)
    result = runtime.execute(skill_id, task)
    typer.echo(result.model_dump_json(indent=2))


@app.command("collect")
def collect(base_dir: str = ".") -> None:
    app_cfg = load_app_config(f"{base_dir}/config")
    source_cfg = load_sources_config(f"{base_dir}/config")
    collector = Collector(source_cfg.sources)
    records = collector.run()
    archiver = Archiver(raw_dir=f"{base_dir}/{app_cfg.storage.raw_dir}")
    outputs = archiver.archive(records)
    typer.echo(f"collected={len(records)} archived={len(outputs)}")


if __name__ == "__main__":
    app()
