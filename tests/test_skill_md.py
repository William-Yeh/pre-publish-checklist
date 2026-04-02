import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def skill():
    return (REPO_ROOT / "skill" / "SKILL.md").read_text()


@pytest.fixture
def frontmatter(skill):
    assert skill.startswith("---"), "SKILL.md must start with frontmatter"
    end = skill.index("---", 3)
    return skill[3:end]


@pytest.fixture
def body(skill):
    end = skill.index("---", 3)
    return skill[end + 3:]


# --- Frontmatter ---

def test_name(frontmatter):
    assert "name: pre-publish-checklist" in frontmatter


def test_description_starts_with_use_when(frontmatter):
    assert "Use when" in frontmatter


def test_author_present(frontmatter):
    assert "author:" in frontmatter


def test_license_is_apache_or_mit(frontmatter):
    assert "Apache-2.0" in frontmatter or "MIT" in frontmatter


def test_version_present(frontmatter):
    assert "version:" in frontmatter


def test_body_under_500_lines(body):
    assert len(body.splitlines()) < 500


# --- Detection table ---

@pytest.mark.parametrize("signal", [
    "SKILL.md",
    "pyproject.toml",
    "package.json",
    "go.mod",
    "Cargo.toml",
    "pom.xml",
    "build.gradle.kts",
    "project.clj",
    "deps.edn",
    "*.sln",
    "CMakeLists.txt",
])
def test_detection_signal_present(skill, signal):
    assert signal in skill, f"Detection table missing signal: {signal}"


# --- Check references ---

def test_skill_lint_invocation(skill):
    assert "/skill-lint check" in skill


def test_version_sync_skip_arg(skill):
    assert "version-sync" in skill


def test_version_sync_git_tag_command(skill):
    assert "git describe --tags" in skill


def test_version_sync_not_bumped_is_blocking(skill):
    assert "Version not bumped" in skill


def test_version_sync_older_version_is_blocking(skill):
    assert "is older than existing tag" in skill


def test_code_reviewer_invocation(skill):
    assert "/common-code-reviewer" in skill


def test_ci_status_command(skill):
    assert "gh run list" in skill


@pytest.mark.parametrize("cmd", [
    "uv run pytest",
    "npm test",
    "go test ./...",
    "cargo test",
    "gradlew test",
    "lein test",
    "dotnet test",
    "cmake",
])
def test_test_command_present(skill, cmd):
    assert cmd in skill, f"Missing test command: {cmd}"


# --- Report and handoff ---

def test_blocking_label(skill):
    assert "BLOCKING" in skill


def test_ready_to_publish_verdict(skill):
    assert "READY TO PUBLISH" in skill


def test_handoff_to_commit_push_pr(skill):
    assert "commit-commands:commit-push-pr" in skill
