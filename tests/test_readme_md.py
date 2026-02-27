import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def readme():
    return (REPO_ROOT / "README.md").read_text()


def test_ci_badge(readme):
    assert "actions/workflows/ci.yml/badge.svg" in readme


def test_license_badge(readme):
    assert "License" in readme
    assert "badge" in readme.lower()


def test_agent_skill_badge(readme):
    assert "agentskills.io" in readme


def test_installation_section(readme):
    assert "## Installation" in readme


def test_npx_skills(readme):
    assert "npx skills add" in readme


def test_manual_install_table_agents(readme):
    for agent in ["Claude Code", "Cursor", "Gemini CLI", "Copilot"]:
        assert agent in readme, f"Missing agent in install table: {agent}"


def test_usage_section(readme):
    assert "## Usage" in readme


def test_starter_prompt(readme):
    assert "/pre-publish" in readme
