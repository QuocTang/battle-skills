---
name: publish-skill
description: |
  End-to-end release pipeline for Battle Skills — from validation to npm publish.
  Use this skill after a new skill has been created or an existing skill has been
  updated. Triggers on "publish skills", "release new version", "push to npm",
  "validate and publish", "deploy skills", "bump version and publish".
tags: [meta, workflow, ci, npm, publish]
tools: [claude-code, cursor, gemini-cli, codex-cli, antigravity]
version: 1.0.0
category: workflow
risk: medium
date_added: 2026-03-05
---

# Publish Skill

Complete release pipeline for Battle Skills — validate, catalog, changelog, version bump, git tag, and npm publish in one go.

---

## When to Use This Skill

- After creating a new skill with `create-skill`
- After modifying an existing skill's SKILL.md or references
- When you want to release a new version to npm
- User says "publish", "release", "deploy to npm", "bump version"

## When NOT to Use This Skill

- You're still writing the skill content → finish first, then publish
- You only want to validate without publishing → run `python3 scripts/validate_skills.py` directly

---

## Pre-Flight Checklist

Before starting the pipeline, confirm:

- [ ] All skill changes are saved
- [ ] You are in the repo root (`battle-skills/`)
- [ ] `npm whoami` returns a valid npm user
- [ ] No uncommitted changes that shouldn't be included

---

## Pipeline Steps

### Step 1 — Validate All Skills

```bash
python3 scripts/validate_skills.py
```

**Expected:** All skills pass with `✓ OK`. Fix any `[ERROR]` before continuing. Warnings (`⚠ WARN`) are acceptable but should be noted.

> [!CAUTION]
> Do NOT proceed if any skill has `[ERROR]`. Fix the error first.

---

### Step 2 — Generate Catalog

```bash
python3 scripts/gen_catalog.py
```

**Expected:** `skills_index.json` and `CATALOG.md` are regenerated.

**Verify:** Open `CATALOG.md` and confirm the new/updated skill appears with correct description and tags.

---

### Step 3 — Update CHANGELOG.md

Add a new version section **above** the previous version. Follow [Keep a Changelog](https://keepachangelog.com) format. **Always write in English.**

```markdown
## [X.Y.Z] — YYYY-MM-DD

### Added

- `skill-name` — One-line description of the new skill.

### Changed

- Description of what changed in existing skills.

### Fixed

- Description of bug fixes.
```

**Rules:**

1. Read current version from `package.json` → `"version"` field
2. Bump the **patch** number (e.g., `1.0.6` → `1.0.7`) for new skills or fixes
3. Bump the **minor** number (e.g., `1.0.7` → `1.1.0`) for breaking changes or major features
4. Write all entries in **English**
5. Update the comparison links at the bottom of CHANGELOG.md:

```markdown
[Unreleased]: https://github.com/QuocTang/battle-skills/compare/vX.Y.Z...HEAD
[X.Y.Z]: https://github.com/QuocTang/battle-skills/compare/vPREV...vX.Y.Z
```

---

### Step 4 — Bump Version in package.json

Update the `"version"` field in `package.json` to match the version you wrote in CHANGELOG.md.

```bash
# Example: bump patch version
npm version patch --no-git-tag-version
```

Or manually edit `package.json` if a specific version is needed.

**Verify:** `cat package.json | grep version` shows the new version.

---

### Step 5 — Git Commit & Tag

```bash
# Stage all changes
git add .

# Commit with conventional message
git commit -m "feat(skill): add <skill-name> — release vX.Y.Z"

# Create annotated tag
git tag -a vX.Y.Z -m "Release vX.Y.Z"

# Push to remote
git push origin main --tags
```

**Commit message convention:**

| Change Type      | Message Format                             |
| ---------------- | ------------------------------------------ |
| New skill        | `feat(skill): add <name>`                  |
| Skill update     | `improve(skill): update <name>`            |
| Bug fix          | `fix(skill): fix <name>`                   |
| Multiple changes | `feat(skill): add <name> — release vX.Y.Z` |

---

### Step 6 — Publish to npm

```bash
npm publish
```

**Expected:** Output shows `+ battle-skills@X.Y.Z` with the full tarball contents.

**Verify after publish:**

```bash
npm info battle-skills version
```

Should return the new version number.

---

## Quick Reference — Full Pipeline

For a fast copy-paste workflow when everything is ready:

```bash
# 1. Validate
python3 scripts/validate_skills.py

# 2. Generate catalog
python3 scripts/gen_catalog.py

# 3. Update CHANGELOG.md (manual step — edit the file)

# 4. Bump version
npm version patch --no-git-tag-version

# 5. Commit & tag
git add .
git commit -m "feat(skill): add <skill-name> — release v$(node -p 'require(\"./package.json\").version')"
git tag -a "v$(node -p 'require("./package.json").version')" -m "Release v$(node -p 'require("./package.json").version')"
git push origin main --tags

# 6. Publish
npm publish
```

---

## Troubleshooting

| Problem                           | Solution                                             |
| --------------------------------- | ---------------------------------------------------- |
| `npm ERR! 403`                    | Run `npm login` first                                |
| `npm ERR! version already exists` | You forgot to bump version — run `npm version patch` |
| Validator shows `[ERROR]`         | Fix the skill before continuing                      |
| `git push` rejected               | Pull first: `git pull --rebase origin main`          |
| Catalog shows old data            | Re-run `python3 scripts/gen_catalog.py`              |

---

## Anti-Patterns (Avoid)

| ❌ Don't                         | ✅ Do Instead                                |
| -------------------------------- | -------------------------------------------- |
| Publish without validating       | Always run validate first                    |
| Write CHANGELOG in Vietnamese    | Always write in English                      |
| Skip version bump                | Always bump version before `npm publish`     |
| Commit without tagging           | Always create a git tag matching the version |
| Publish with uncommitted changes | Commit everything first, then publish        |
| Use vague commit messages        | Follow conventional commit format            |
