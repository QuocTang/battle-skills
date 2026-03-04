# Changelog

All notable changes to **Battle Skills** are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.0.7] — 2026-03-05

### Added

- `publish-skill` — End-to-end release pipeline skill for Battle Skills: validate, catalog, changelog, version bump, git tag, and npm publish.

---

## [1.0.6] — 2026-03-05

### Added

- `code-explainer` — Skill for detailed source code explanation and analysis for learning purposes.

### Fixed

- Fixed YAML parsing logic for multi-line values (e.g., `description: |`) in `scripts/validate_skills.py` and `scripts/gen_catalog.py`.

---

## [1.0.5] — 2026-03-04

### Added

- `academic-thesis-writer-vi` — Skill for writing master's-level academic essays/theses in Vietnamese.
- `nextjs-feature-module` — Scaffold Next.js feature modules separating IO, logic, and UI (App Router).
- `create-skill` — Meta-skill: guide for creating new Battle Skills from scratch.

---

## [1.0.4] — 2026-03-02

### Added

- `awesome-readme` — Awesome README Generator skill.
- Added project badges to the main `README.md`.

---

## [1.0.3] — 2026-03-01

### Changed

- Copied `skills_index.json` during install for faster skill discovery.
- Excluded the `docs` directory from being copied during the installation process.

---

## [1.0.2] — 2026-03-01

### Fixed

- Included `docs` and `skills` directories in the npm package payload correctly.

---

## [1.0.1] — 2026-03-01

### Added

- CLI installation instructions.
- `bin/install.js` script to automatically install battle-skills across different AI agents' configuration directories.

### Changed

- Removed `generated_at` from `skills_index.json` to prevent unnecessary git diffs.
- Updated README installation steps.

---

## [1.0.0] — 2026-03-01

### Added

- Initial repository structure setup: `skills/`, `scripts/`, `docs/`.
- `scripts/validate_skills.py` — Validates skill structure, frontmatter, and quality before committing.
- `scripts/gen_catalog.py` — Auto-generates `skills_index.json` and `CATALOG.md` from the skills directory.

---

[Unreleased]: https://github.com/QuocTang/battle-skills/compare/v1.0.7...HEAD
[1.0.7]: https://github.com/QuocTang/battle-skills/compare/v1.0.6...v1.0.7
[1.0.6]: https://github.com/QuocTang/battle-skills/compare/v1.0.5...v1.0.6
[1.0.5]: https://github.com/QuocTang/battle-skills/compare/v1.0.4...v1.0.5
[1.0.4]: https://github.com/QuocTang/battle-skills/compare/v1.0.3...v1.0.4
[1.0.3]: https://github.com/QuocTang/battle-skills/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/QuocTang/battle-skills/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/QuocTang/battle-skills/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/QuocTang/battle-skills/releases/tag/v1.0.0
