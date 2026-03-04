# Output Template

Standard templates for code explanation documents. Copy and adapt as needed.

---

## Template: Code Explanation Doc

```markdown
# 📄 File: `filename.ext` — [Short description of what this file does]

> **Goal:** [What the reader will learn/understand after reading this doc]

---

## 📋 Original Code (Annotated)

\`\`\`[language]

# — SECTION: [Section Name] —

# [What this section does]

import something # [What this library is and why we need it]

# — SECTION: [Next Section] —

variable = function() # [Explain the function and the result]
\`\`\`

---

## 🧩 Detailed Explanation

### [Concept/Library/Tool Name]

**What is it?**
[1-2 sentence definition]

**Analogy:**
[Real-world comparison that makes it click]

**In this code:**
[How it's specifically used here]

\`\`\`
[ASCII diagram if helpful]
\`\`\`

### [Next Concept]

[Same structure...]

---

## 📝 Language Syntax Explained

### `syntax_expression`

\`\`\`[language]

# General form:

general_syntax

# Example from this code:

specific_usage

# Equivalent to:

simpler_equivalent # (if applicable)
\`\`\`

### `another_syntax`

[Same structure...]

---

## 💡 Key Takeaways

| Observation            | Meaning         | Action                |
| ---------------------- | --------------- | --------------------- |
| [What you see in code] | [Why it's done] | [What to do about it] |

---

## ❓ FAQ

**Q: [Common question a beginner would ask]**
A: [Clear, concise answer]

**Q: [Another common question]**
A: [Answer]

---

> **Next:** [link to next file in sequence]
```

---

## Template: README Index

```markdown
# 📚 Code Documentation — [Project Name]

## 📖 Table of Contents

| #   | File                                                           | Content                         |
| --- | -------------------------------------------------------------- | ------------------------------- |
| 0   | [00_foundational_knowledge.md](./00_foundational_knowledge.md) | Prerequisites and core concepts |
| 1   | [01_script_name.md](./01_script_name.md)                       | [Short description]             |
| 2   | [02_script_name.md](./02_script_name.md)                       | [Short description]             |

## 🗺️ Reading Order

\`\`\`
Step 0: Read foundational knowledge (REQUIRED if new to [domain])
↓
Step 1: [first_script] — understand [what]
↓
Step 2: [second_script] — understand [what]
↓
...
\`\`\`
```

---

## Formatting Conventions

| Element    | Convention                             |
| ---------- | -------------------------------------- |
| File names | Backtick format: `filename.py`         |
| Code terms | Backtick format: `variable_name`       |
| Emphasis   | **Bold** for key terms first mentioned |
| Warnings   | Use blockquotes: `> ⚠️ IMPORTANT: ...` |
| Sections   | Use emoji prefixes: 📋 📊 🧩 📝 💡 ❓  |
| Diagrams   | ASCII art inside fenced code blocks    |
| Navigation | Links at bottom: `> **Next:** [link]`  |

---

## Quality Checklist

Before finalizing any doc, verify:

- [ ] Every complex concept has an analogy
- [ ] Every library/framework is introduced (what it is + why it's used)
- [ ] ASCII diagrams are used for flows, comparisons, or spatial concepts
- [ ] Language syntax is explained separately for beginners
- [ ] FAQ answers real questions a beginner would ask
- [ ] Navigation links connect docs in reading order
- [ ] No unexplained jargon
- [ ] File follows naming convention: `NN_script_name.md`
