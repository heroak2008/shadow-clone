from pathlib import Path

from fastapi.testclient import TestClient
from typer.testing import CliRunner

from digital_human.api.server import app
from digital_human.cli.app import app as cli_app


runner = CliRunner()


def test_cli_list_skills() -> None:
    base_dir = str(Path(__file__).resolve().parents[1])
    result = runner.invoke(cli_app, ["list-skills", "--base-dir", base_dir])
    assert result.exit_code == 0
    assert "darwin" in result.stdout


def test_api_health_and_execute() -> None:
    base_dir = str(Path(__file__).resolve().parents[1])
    import os

    os.environ["DIGITAL_HUMAN_BASE_DIR"] = base_dir
    client = TestClient(app)
    assert client.get("/health").status_code == 200
    resp = client.post("/skills/execute", json={"skill_id": "nuwa", "task": "写一个方案"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["skill_id"] == "nuwa"
