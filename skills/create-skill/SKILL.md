---
name: create-skill
description: Guide for creating a new Battle Skill from scratch. Use this skill whenever you want to add a new skill to this repository — whether it's capturing a workflow, documenting a pattern, or turning a battle-tested technique into a reusable skill. Triggers on phrases like "create a skill", "add a skill", "new skill", "turn this into a skill", "document this workflow".
tags: [meta, workflow, documentation]
tools: [claude-code, cursor, gemini-cli, codex-cli]
version: 1.0.0
---

# Create Skill

A guide for creating high-quality Battle Skills that AI agents can reliably use.

---

## TL;DR — Quick Checklist

```
skills/
└── your-skill-name/
    ├── SKILL.md          ← required
    ├── references/       ← optional: large docs, cheat sheets
    ├── scripts/          ← optional: executable helpers
    └── assets/           ← optional: templates, icons, files
```

Run before committing:
```bash
python3 scripts/validate_skills.py skills/your-skill-name
python3 scripts/gen_catalog.py
```

---

## Step 1 — Pick a Name

- Use **lowercase kebab-case**: `react-patterns`, `api-design`, `deploy-vercel`
- Name describes **what the skill does**, not what domain it's in
- No generic names: ~~`frontend`~~, ~~`misc`~~, ~~`helpers`~~

---

## Step 2 — Create the Folder & SKILL.md

```bash
mkdir skills/your-skill-name
touch skills/your-skill-name/SKILL.md
```

### SKILL.md Frontmatter (required)

```yaml
---
name: your-skill-name          # must match folder name exactly
description: |                 # THIS IS THE MOST IMPORTANT FIELD.
  What the skill does and      # Claude uses this to decide when to trigger the skill.
  when to use it. Be specific  # Include user phrases that should trigger it.
  and slightly "pushy".        # Aim for 2-4 sentences, minimum 10 words.
tags: [tag1, tag2]             # lowercase kebab-case, helps with discovery
tools: [claude-code, cursor]   # which AI tools this skill targets
version: 1.0.0                 # semantic versioning
author: your-github-handle     # optional
category: your-category        # optional: grouping category
risk: low                      # optional: low | medium | high
source: https://example.com    # optional: original reference URL
date_added: 2026-01-01         # optional: when this skill was created
---
```

> [!WARNING]
> Chỉ sử dụng các key được liệt kê ở trên. Validator sẽ cảnh báo nếu gặp **unknown frontmatter key** không nằm trong danh sách `name`, `description`, `tags`, `tools`, `version`, `author`, `category`, `risk`, `source`, `date_added`.

### Description Writing Guide

The `description` field is the **primary trigger mechanism** — Claude reads it to decide if a skill is relevant. Write it to match how users naturally phrase requests. **Tối thiểu 10 từ** (validator sẽ cảnh báo nếu ít hơn).

**Bad description:**
```
How to write React components.
```

**Good description:**
```
Best practices for building React components, hooks, and state management.
Use this skill when writing any React code, creating components, managing state,
or when the user mentions React, JSX, hooks, or component architecture.
```

The good version: explains what it does, says when to use it, and lists trigger phrases.

---

## Step 3 — Write the Body

### Anatomy of a Good Skill Body

```markdown
# Skill Name

One sentence explaining what this skill enables.

---

## When to Use This Skill
- Situation A
- Situation B

## When NOT to Use This Skill
- Situation C (use X instead)

## Core Rules
1. Rule one — with brief explanation
2. Rule two — with brief explanation
3. ...

## Examples

### Good Example
\`\`\`language
// correct pattern
\`\`\`

### Bad Example
\`\`\`language
// anti-pattern — explain why
\`\`\`

## Anti-Patterns (Avoid)
- What not to do and why
```

### Principles

**Keep SKILL.md under 500 lines.** If you're going over, move large sections to `references/` and add a pointer in SKILL.md:

```markdown
> For full API reference, see [references/api.md](references/api.md)
```

**Be concrete, not abstract.** Show code examples. Show the diff between right and wrong.

**Principle of No Surprise.** The skill should do exactly what its name and description say — nothing more, nothing less.

**Progressive disclosure:**
- Metadata (name + description) → always in context
- SKILL.md body → loaded when skill triggers
- references/ → loaded on demand when skill needs them

---

## Step 4 — Add Bundled Resources (Optional)

### `references/` — Large Docs

For cheat sheets, API references, framework docs that would bloat the main SKILL.md:

```
references/
├── aws.md
├── gcp.md
└── azure.md
```

Reference them from SKILL.md: `See [references/aws.md](references/aws.md) for AWS-specific config.`

### `scripts/` — Executable Helpers

For deterministic, repetitive tasks the AI should run rather than reason about:

```python
# scripts/scaffold.py
# Scaffolds boilerplate for this skill's workflow
```

### `assets/` — Files & Templates

For starter files, config templates, icons used in skill output.

---

## Step 5 — Validate & Publish

```bash
# Validate your skill
python3 scripts/validate_skills.py skills/your-skill-name

# If all good, regenerate catalog
python3 scripts/gen_catalog.py

# Commit
git add skills/your-skill-name CATALOG.md skills_index.json
git commit -m "feat(skill): add your-skill-name"
```

### Commit Convention

```
feat(skill): add <name>          # new skill
fix(skill): fix <name>           # bug fix in skill
improve(skill): update <name>    # improvement
deprecate(skill): remove <name>  # removal
```

---

## Step 6 — Update CHANGELOG.md

Add an entry under `[Unreleased]`:

```markdown
### Added
- `your-skill-name` — One-line description of what it does
```

---

## Quality Bar

Before submitting, ask yourself:

- [ ] Does the **description** clearly say when to use this skill?
- [ ] Are there **concrete examples** (not just abstract rules)?
- [ ] Does it cover **anti-patterns** (what NOT to do)?
- [ ] Is SKILL.md **under 500 lines**?
- [ ] Did `validate_skills.py` pass with no errors?
- [ ] Is the skill **battle-tested** — from real usage, not theory?

A skill that hasn't been used in a real project yet is a hypothesis, not a battle skill.

---

## Example: Minimal Valid Skill

```
skills/
└── git-commit-message/
    └── SKILL.md
```

```markdown
---
name: git-commit-message
description: Write clear, conventional git commit messages following the
  Conventional Commits specification. Use when the user asks to write a commit
  message, summarize changes for git, or says "commit this".
tags: [git, workflow]
tools: [claude-code, cursor, gemini-cli]
version: 1.0.0
---

# Git Commit Message

Write structured commit messages that make history readable.

## Format

\`\`\`
<type>(<scope>): <subject>

[optional body]

[optional footer]
\`\`\`

## Types
- `feat` — new feature
- `fix` — bug fix
- `docs` — documentation only
- `refactor` — no feature/fix change
- `test` — adding tests
- `chore` — tooling, deps

## Rules
1. Subject line max 72 chars, imperative mood ("add" not "added")
2. Scope is optional but helpful: `feat(auth): add OAuth`
3. Body explains *why*, not *what* (the diff shows what)

## Example

Good: `feat(auth): add Google OAuth login`
Bad: `updated auth stuff`
```
