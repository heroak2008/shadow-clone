from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class StorageConfig(BaseModel):
    db_path: str
    raw_dir: str
    processed_dir: str
    archive_dir: str
    vectorstore_dir: str


class SchedulerConfig(BaseModel):
    enabled: bool = True
    interval_minutes: int = 60


class ProviderOpenAIConfig(BaseModel):
    base_url: str = ""
    api_key: str = ""
    model: str = ""


class ProviderOllamaConfig(BaseModel):
    base_url: str = "http://localhost:11434"
    model: str = "qwen2.5"


class LLMConfig(BaseModel):
    provider: str = "mock"
    openai: ProviderOpenAIConfig = Field(default_factory=ProviderOpenAIConfig)
    ollama: ProviderOllamaConfig = Field(default_factory=ProviderOllamaConfig)


class VectorStoreConfig(BaseModel):
    enabled: bool = False


class AppConfig(BaseModel):
    project_name: str
    storage: StorageConfig
    scheduler: SchedulerConfig = Field(default_factory=SchedulerConfig)
    vectorstore: VectorStoreConfig = Field(default_factory=VectorStoreConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)


class Source(BaseModel):
    id: str
    type: Literal["im", "wiki", "local_files"]
    enabled: bool = True
    config: dict[str, Any] = Field(default_factory=dict)


class SourcesConfig(BaseModel):
    sources: list[Source] = Field(default_factory=list)


class SkillRef(BaseModel):
    id: str
    name: str
    file: str


class SkillsConfig(BaseModel):
    skills: list[SkillRef] = Field(default_factory=list)
