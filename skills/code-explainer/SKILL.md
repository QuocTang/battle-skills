---
name: code-explainer
description: |
  Explain and analyze source code in detail for learning purposes. Automatically
  detects foundational knowledge required and creates prerequisite docs before
  explaining code. Use when the user asks to "explain this code", "analyze code",
  "document code for learning", "create code walkthrough", "break down this script",
  "I don't understand this code", or "teach me this codebase".
tags: [documentation, learning, code-analysis, education]
tools: [claude-code, cursor, gemini-cli, codex-cli]
version: 1.0.0
category: documentation
risk: low
date_added: 2026-03-05
---

# Code Explainer

Create comprehensive, beginner-friendly code explanations that include foundational
knowledge, line-by-line annotations, analogies, ASCII diagrams, and FAQ sections.

---

## When to Use This Skill

- User asks to explain, analyze, or document code for learning
- User wants to understand a new codebase or unfamiliar script
- Creating educational documentation for a project
- Onboarding material for new developers joining a project
- User says "I don't understand this code" or "what does this do"

## When NOT to Use This Skill

- User wants API reference docs → use a doc-generation tool instead
- User wants to refactor or fix code → just do the refactoring
- User only needs a one-line summary → answer directly, don't create full docs

---

## Core Rules

1. **English only** — All output documents must be in English
2. **Analogies first** — Every complex concept MUST have a real-world analogy
3. **Progressive depth** — Start simple, then go deeper. Never assume prior knowledge
4. **Show, don't just tell** — Use ASCII diagrams, code examples, tables for comparison
5. **Language-agnostic** — This skill works for ANY programming language or framework
6. **Foundational knowledge auto-detect** — If the code uses domain-specific concepts (DL, web frameworks, databases, DevOps, etc.), create a prerequisite knowledge doc FIRST

---

## Workflow

### Step 1 — Survey the Code

Read the code and determine:

- **Language & framework** (Python + PyTorch? TypeScript + Next.js? Go + gRPC?)
- **Domain** (Machine Learning? Web? Systems? Data pipeline? DevOps?)
- **Complexity level** — Does the reader need foundational knowledge?
- **Key concepts** — List every concept a beginner would NOT know

```
Example survey output (internal, not in final doc):

  Language: Python
  Framework: Ultralytics (YOLO), PyTorch
  Domain: Deep Learning — Object Detection
  Foundational knowledge needed: YES
  Key concepts: transfer learning, GPU/CUDA, loss functions,
                hyperparameters, bounding boxes, epochs, batch size
```

### Step 2 — Create Foundational Knowledge Doc (if needed)

If Step 1 identifies domain-specific concepts, create `00_foundational_knowledge.md` BEFORE explaining any code.

**When to create this doc:**

- Code uses specialized libraries (PyTorch, TensorFlow, React, Kubernetes, etc.)
- Domain has jargon a general developer wouldn't know
- Multiple scripts share common concepts → explain once, reference everywhere

**Structure of the foundational knowledge doc:**

```markdown
# 🧠 Foundational Knowledge — Read Before Starting

> **Goal:** Understand the core concepts needed to read the code in this project.
> If you already know [DOMAIN], you can skip this file.

---

## 1. [High-Level Concept]

[Analogy] + [Simple explanation] + [Why it matters for this project]

## 2. [Next Concept]

...

## N. Key Terminology

| Term | Explanation | Analogy |
| ---- | ----------- | ------- |
| ...  | ...         | ...     |

## Project Flow Summary

[ASCII diagram showing how all scripts connect]
```

> For the full template, see [references/output-template.md](references/output-template.md)

### Step 3 — Explain the Code

For each code file, create a documentation file following this structure:

```markdown
# 📄 File: `filename.py` — [One-line purpose]

> **Goal:** [What the reader will understand after reading this doc]

---

## 📋 Original Code (Annotated)

\`\`\`python

# — SECTION NAME —

code_line_here # Inline comment explaining what this does
\`\`\`

---

## 🧩 Detailed Explanation

### [Concept 1 from the code]

[Analogy] → [Technical explanation] → [ASCII diagram if applicable]

### [Concept 2]

...

---

## 📝 Language Syntax Explained

### `some_syntax_here`

\`\`\`python

# What it does + example

\`\`\`

---

## ❓ FAQ

**Q: [Common question]**
A: [Clear answer]

---

> **Next:** [link to next file]
```

### Step 4 — Create README Index

If multiple files are documented, create/update a `README.md` index:

```markdown
# 📚 Code Documentation

## Table of Contents

| #   | File                                | Content       |
| --- | ----------------------------------- | ------------- |
| 0   | [00_foundational_knowledge.md](...) | Prerequisites |
| 1   | [01_filename.md](...)               | [Description] |
| ... | ...                                 | ...           |

## Reading Order

[ASCII flow showing dependencies]
```

---

## Analogy Writing Guide

Good analogies are the **most important** part of this skill. Rules:

| Rule                       | Example                                                 |
| -------------------------- | ------------------------------------------------------- |
| Use everyday objects       | "A batch is like a teacher grading 8 papers at once"    |
| Match complexity           | Don't use a PhD analogy for a simple concept            |
| Be consistent              | If you compare training to studying, keep that metaphor |
| Use tables for comparisons | CPU vs GPU, SQL vs NoSQL, etc.                          |

### Good Analogy

```
Learning Rate = the "step size" each time the model updates its knowledge

  Too large (0.1):  Jumping wildly — never converges!
  Just right (0.005): Steady descent — converges well
  Too small (0.00001): Standing still — takes forever!
```

### Bad Analogy

```
Learning rate is a hyperparameter that controls the step size
during gradient descent optimization.
```

(Too technical, no analogy, no visual — useless for beginners)

---

## ASCII Diagram Guide

Use ASCII diagrams for:

- **Data flow** between scripts/components
- **Architecture** of systems or models
- **Comparisons** (before/after, good/bad)
- **Visual math** (coordinates, grids, layouts)

```
Example — Data pipeline flow:

  Raw Data → Clean → Split → Train → Evaluate → Deploy
  ┌──────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌────────┐  ┌──────┐
  │ CSV  │→ │Clean│→ │Split│→ │Train│→ │Evaluate│→ │Deploy│
  │ JSON │  │ NaN │  │70/30│  │Model│  │Metrics │  │ API  │
  └──────┘  └─────┘  └─────┘  └─────┘  └────────┘  └──────┘
```

---

## Anti-Patterns (Avoid)

| ❌ Don't                                      | ✅ Do Instead                                 |
| --------------------------------------------- | --------------------------------------------- |
| Explain only WHAT code does                   | Explain WHY + WHEN + HOW                      |
| Skip library/framework context                | Explain what the library is and why it's used |
| Write walls of text                           | Use tables, diagrams, code blocks             |
| Assume the reader knows jargon                | Define every term with an analogy             |
| Copy-paste official docs                      | Rewrite in beginner-friendly language         |
| Hard-code for one language                    | Keep patterns language-agnostic               |
| Write foundational knowledge inside code docs | Separate into `00_foundational_knowledge.md`  |

---

## Output File Naming Convention

```
docs/
├── README.md                        ← Index + reading order
├── 00_foundational_knowledge.md     ← Domain prerequisites (if needed)
├── 01_[script_name].md              ← First script explanation
├── 02_[script_name].md              ← Second script
└── ...
```

> For full output templates with examples, see [references/output-template.md](references/output-template.md)
> For foundational knowledge patterns by domain, see [references/knowledge-patterns.md](references/knowledge-patterns.md)
