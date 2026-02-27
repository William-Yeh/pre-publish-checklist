# pre-publish-checklist

[![CI](https://github.com/William-Yeh/pre-publish-checklist/actions/workflows/ci.yml/badge.svg)](https://github.com/William-Yeh/pre-publish-checklist/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Agent Skill](https://img.shields.io/badge/Agent_Skill-agentskills.io-6B4FBB)](https://agentskills.io)

An Agent Skill that runs pre-publish checks before you tag or push a repo.
Detects repo type(s) from build manifests, runs applicable checks, and reports a consolidated verdict before handing off to publishing.

## What It Checks

| Repo Type | Checks |
|---|---|
| Agent Skill | Skill spec compliance via `/skill-lint check` |
| Any program | Code review via `/common-code-reviewer`, local tests, CI status |

Findings are classified as **blocking** (must fix before publish) or **warning** (non-blocking).

## Detected Repo Types

Automatically detected from build manifests at the repo root.
A repo can match multiple types simultaneously.

Python · Node.js · Go · Rust · Java · Kotlin · Clojure · C# · F# · C/C++ · Agent Skill

## Installation

### Recommended: `npx skills`

```bash
npx skills add William-Yeh/pre-publish-checklist
```

### Manual installation

Copy the skill directory to your agent's skill folder:

| Agent | Directory |
|-------|-----------|
| Claude Code | `~/.claude/skills/` |
| Cursor | `.cursor/skills/` |
| Gemini CLI | `.gemini/skills/` |
| Amp | `.amp/skills/` |
| Roo Code | `.roo/skills/` |
| Copilot | `.github/skills/` |

## Usage

Compatible with any AI agent that supports the [Agent Skills spec](https://agentskills.io).

### Starter prompts

- `/pre-publish`
- `/pre-publish --skip ci`
- `/pre-publish --skip code-review --skip tests`
