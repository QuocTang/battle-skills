# Changelog

All notable changes to **Battle Skills** are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.0.6] — 2026-03-05

### Added

- `code-explainer` — Skill for detailed source code explanation and analysis for learning purposes.

### Fixed

- Fixed YAML parsing logic for multi-line values (e.g., `description: |`) in `scripts/validate_skills.py` and `scripts/gen_catalog.py`.

---

## [1.0.0] — 2026-03-01

### Added

- `academic-thesis-writer-vi` — Skill for writing master's-level academic essays/theses in Vietnamese
- `awesome-readme` — Awesome README Generator
- `nextjs-feature-module` — Scaffold Next.js feature modules separating IO, logic, and UI (App Router)
- `create-skill` — Meta-skill: guide for creating new Battle Skills from scratch
- `scripts/validate_skills.py` — Validates skill structure, frontmatter, and quality before commit
- `scripts/gen_catalog.py` — Auto-generates `skills_index.json` and `CATALOG.md` from skills directory
- Initial repo structure: `skills/`, `scripts/`, `docs/`

---

[Unreleased]: https://github.com/QuocTang/battle-skills/compare/v1.0.6...HEAD
[1.0.6]: https://github.com/QuocTang/battle-skills/compare/v1.0.0...v1.0.6
[1.0.0]: https://github.com/QuocTang/battle-skills/releases/tag/v1.0.0
