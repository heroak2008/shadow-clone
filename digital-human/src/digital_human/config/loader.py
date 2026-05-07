from __future__ import annotations

import os
from pathlib import Path
from typing import TypeVar

import yaml
from pydantic import BaseModel

from digital_human.config.schema import AppConfig, SkillsConfig, SourcesConfig

T = TypeVar("T", bound=BaseModel)


def _expand_env(data: object) -> object:
    if isinstance(data, str):
        return os.path.expandvars(data)
    if isinstance(data, dict):
        return {k: _expand_env(v) for k, v in data.items()}
    if isinstance(data, list):
        return [_expand_env(item) for item in data]
    return data


def load_yaml(path: str | Path, schema: type[T]) -> T:
    with Path(path).open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}
    expanded = _expand_env(raw)
    return schema.model_validate(expanded)


def load_app_config(base_dir: str | Path = "config") -> AppConfig:
    return load_yaml(Path(base_dir) / "config.yaml", AppConfig)


def load_sources_config(base_dir: str | Path = "config") -> SourcesConfig:
    return load_yaml(Path(base_dir) / "sources.yaml", SourcesConfig)


def load_skills_config(base_dir: str | Path = "config") -> SkillsConfig:
    return load_yaml(Path(base_dir) / "skills.yaml", SkillsConfig)
