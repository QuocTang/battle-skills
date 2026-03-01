#!/usr/bin/env python3
"""
validate_skills.py — Battle Skills validator
Checks every skill folder for correctness before publishing.

Usage:
    python3 scripts/validate_skills.py              # validate all skills
    python3 scripts/validate_skills.py skills/my-skill  # validate one skill
"""

import sys
import re
from pathlib import Path

# ── ANSI colors ────────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

# ── Config ─────────────────────────────────────────────────────────────────────
REPO_ROOT   = Path(__file__).parent.parent
SKILLS_DIR  = REPO_ROOT / "skills"

REQUIRED_FRONTMATTER = ["name", "description"]
OPTIONAL_FRONTMATTER = ["tags", "tools", "version", "author"]

MAX_SKILL_MD_LINES   = 500   # warn if SKILL.md exceeds this
MIN_DESCRIPTION_WORDS = 10   # warn if description is too terse
VALID_NAME_PATTERN   = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")  # kebab-case


# ── Helpers ────────────────────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body) from a SKILL.md string."""
    fm: dict = {}
    body = text

    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            raw_fm = parts[1].strip()
            body   = parts[2].strip()
            for line in raw_fm.splitlines():
                if ":" in line:
                    key, _, val = line.partition(":")
                    fm[key.strip()] = val.strip()
    return fm, body


def validate_skill(skill_dir: Path) -> list[str]:
    """
    Validate a single skill directory.
    Returns a list of error/warning strings (empty = all good).
    """
    issues: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    # ── 1. SKILL.md must exist ─────────────────────────────────────────────────
    if not skill_md.exists():
        issues.append(f"{RED}[ERROR]{RESET} Missing SKILL.md")
        return issues  # can't continue without it

    content = skill_md.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)

    # ── 2. Frontmatter: required keys ──────────────────────────────────────────
    for key in REQUIRED_FRONTMATTER:
        if key not in fm or not fm[key]:
            issues.append(f"{RED}[ERROR]{RESET} Frontmatter missing required key: `{key}`")

    # ── 3. name must match folder name & be kebab-case ─────────────────────────
    declared_name = fm.get("name", "")
    if declared_name and declared_name != skill_dir.name:
        issues.append(
            f"{RED}[ERROR]{RESET} `name` in frontmatter ({declared_name!r}) "
            f"doesn't match folder name ({skill_dir.name!r})"
        )
    if declared_name and not VALID_NAME_PATTERN.match(declared_name):
        issues.append(
            f"{YELLOW}[WARN]{RESET}  `name` should be lowercase kebab-case "
            f"(e.g. my-skill), got: {declared_name!r}"
        )

    # ── 4. description quality ─────────────────────────────────────────────────
    description = fm.get("description", "")
    word_count  = len(description.split())
    if description and word_count < MIN_DESCRIPTION_WORDS:
        issues.append(
            f"{YELLOW}[WARN]{RESET}  `description` is very short ({word_count} words). "
            f"Aim for at least {MIN_DESCRIPTION_WORDS} words so Claude can trigger this skill correctly."
        )

    # ── 5. body must not be empty ──────────────────────────────────────────────
    if not body.strip():
        issues.append(f"{RED}[ERROR]{RESET} SKILL.md body is empty (no content after frontmatter)")

    # ── 6. body must have at least one H1 heading ──────────────────────────────
    has_h1 = any(line.startswith("# ") for line in body.splitlines())
    if not has_h1:
        issues.append(f"{YELLOW}[WARN]{RESET}  SKILL.md has no H1 heading (`# Title`)")

    # ── 7. file length ─────────────────────────────────────────────────────────
    line_count = len(content.splitlines())
    if line_count > MAX_SKILL_MD_LINES:
        issues.append(
            f"{YELLOW}[WARN]{RESET}  SKILL.md is {line_count} lines "
            f"(recommended max {MAX_SKILL_MD_LINES}). "
            f"Consider moving large sections to references/ subfolder."
        )

    # ── 8. unknown frontmatter keys ────────────────────────────────────────────
    known = set(REQUIRED_FRONTMATTER + OPTIONAL_FRONTMATTER)
    for key in fm:
        if key not in known:
            issues.append(f"{YELLOW}[WARN]{RESET}  Unknown frontmatter key: `{key}` (will be ignored)")

    # ── 9. tag format (if present) ─────────────────────────────────────────────
    raw_tags = fm.get("tags", "")
    if raw_tags:
        # accept both "tag1, tag2" and "[tag1, tag2]"
        cleaned = raw_tags.strip("[]")
        tags = [t.strip() for t in cleaned.split(",") if t.strip()]
        for tag in tags:
            if not re.match(r"^[a-z0-9-]+$", tag):
                issues.append(
                    f"{YELLOW}[WARN]{RESET}  Tag {tag!r} should be lowercase kebab-case"
                )

    return issues


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    # Determine which skills to validate
    if len(sys.argv) > 1:
        targets = [Path(p) for p in sys.argv[1:]]
    else:
        if not SKILLS_DIR.exists():
            print(f"{RED}skills/ directory not found at {SKILLS_DIR}{RESET}")
            sys.exit(1)
        targets = sorted([d for d in SKILLS_DIR.iterdir() if d.is_dir()])

    if not targets:
        print(f"{YELLOW}No skill directories found.{RESET}")
        sys.exit(0)

    total   = len(targets)
    passed  = 0
    warned  = 0
    failed  = 0

    print(f"\n{BOLD}{CYAN}⚔  Battle Skills — Validator{RESET}")
    print(f"Scanning {total} skill(s) in {SKILLS_DIR.relative_to(REPO_ROOT)}/\n")
    print("─" * 60)

    for skill_dir in targets:
        issues  = validate_skill(skill_dir)
        errors  = [i for i in issues if "[ERROR]" in i]
        warnings= [i for i in issues if "[WARN]"  in i]

        if errors:
            status = f"{RED}✗ FAIL{RESET}"
            failed += 1
        elif warnings:
            status = f"{YELLOW}⚠ WARN{RESET}"
            warned += 1
        else:
            status = f"{GREEN}✓ OK  {RESET}"
            passed += 1

        print(f"  {status}  {skill_dir.name}")
        for issue in issues:
            print(f"         {issue}")

    print("─" * 60)
    print(
        f"\n{BOLD}Results:{RESET} "
        f"{GREEN}{passed} passed{RESET}  "
        f"{YELLOW}{warned} warned{RESET}  "
        f"{RED}{failed} failed{RESET}  "
        f"(total: {total})\n"
    )

    if failed:
        print(f"{RED}Fix all [ERROR] issues before committing.{RESET}\n")
        sys.exit(1)
    elif warned:
        print(f"{YELLOW}Warnings won't block you, but consider fixing them.{RESET}\n")
        sys.exit(0)
    else:
        print(f"{GREEN}All skills look great! Ready to battle. ⚔{RESET}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
