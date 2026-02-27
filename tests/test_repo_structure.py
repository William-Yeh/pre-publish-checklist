from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_skill_md_exists():
    assert (REPO_ROOT / "SKILL.md").exists()


def test_license_exists():
    assert (REPO_ROOT / "LICENSE").exists()


def test_license_is_apache_or_mit():
    content = (REPO_ROOT / "LICENSE").read_text()
    assert "Apache License" in content or "MIT License" in content


def test_license_has_copyright_notice():
    import re
    content = (REPO_ROOT / "LICENSE").read_text()
    assert re.search(r"Copyright \d{4}(-\d{4})? \S+", content), "LICENSE must contain a copyright notice with a year and author"


def test_ci_workflow_exists():
    assert (REPO_ROOT / ".github" / "workflows" / "ci.yml").exists()


def test_ci_workflow_runs_skill_lint():
    content = (REPO_ROOT / ".github" / "workflows" / "ci.yml").read_text()
    assert "skill-lint check" in content
