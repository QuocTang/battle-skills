---
name: awesome-readme
description: "When the user wants an 'Awesome' style README.md with advanced sections like Table of Contents, Support, Contributors via contrib.rocks, License, and Star History chart. Use when asked for 'awesome readme' or 'professional github readme'."
tags: [readme, documentation, github]
tools: [claude-code, cursor, gemini-cli]
version: 1.0.0
risk: low
date_added: "2026-03-01"
---

# Awesome README Generator

You are an expert open-source maintainer and technical writer. Your goal is to write a README.md that matches the top-tier "Awesome" repository standards on GitHub (e.g. antigravity-awesome-skills format).

## When to Use This Skill

Use this skill when:

- User asks to create an "awesome readme" or "professional github readme".
- User wants to include advanced sections like Contributors, Star History, and deep Table of Contents.
- The project is aiming to be a popular open-source repository.

## The Awesome Structure Requirements

An awesome README must have the following exact sections with Emojis:

### 1. Title and Badges & Intro

Start with an Emoji + Header 1. Followed by a catchy description line. You can optionally include badges (CI/CD, Version, License) here. 
For badges, use this standard format:
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### 2. Table of Contents

```markdown
## Table of Contents

- [🚀 Quick Start](#quick-start)
- [🛠️ Installation](#installation)
- [📦 Features](#features)
- [🤝 How to Contribute](#how-to-contribute)
- [💬 Community & Support](#community--support)
- [👥 Repo Contributors](#repo-contributors)
- [⚖️ License](#license)
- [🌟 Star History](#star-history)

---
```

### 3. Quick Start & Installation

Provide a 1-minute quick start and precise installation instructions, using tables or clear code blocks.

### 4. Features

Use a Markdown Table to display features elegantly if possible, or bold bullet points with emojis.

### 5. How to Contribute & Support

```markdown
## How to Contribute

We welcome contributions! Please follow these steps:

1. **Fork** the repository.
2. **Create a new branch** for your feature.
3. **Submit a Pull Request**.

## Support the Project

If this repository saves you time, please star the repository!
```

### 6. Repo Contributors

Use `contrib.rocks` to dynamically generate a contributor image based on the repository slug.
Format:

```markdown
## Repo Contributors

<a href="https://github.com/USERNAME/REPO_NAME/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=USERNAME/REPO_NAME" alt="Repository contributors" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
```

_Note: Infer the USERNAME/REPO_NAME from `package.json`, `.git/config` or ask the user._

### 7. License

```markdown
## License

MIT License. See [LICENSE](LICENSE) for details.
```

### 8. Star History

```markdown
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=USERNAME/REPO_NAME&type=Date)](https://star-history.com/#USERNAME/REPO_NAME&Date)
```

## Instructions for Execution

1. Discover the framework and entry points.
2. Find the project name and github slug (e.g. `sickn33/antigravity-awesome-skills`). If missing, use placeholder `your-username/your-repo` or extract from git remote.
3. Strictly follow the structure outlined above.
4. Output the full generated README.md locally to the root folder.
