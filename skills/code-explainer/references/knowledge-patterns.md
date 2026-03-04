# Knowledge Patterns by Domain

Guide for identifying what foundational knowledge to create based on the code's domain.

---

## How to Decide If Foundational Knowledge Is Needed

Ask these questions:

1. **Does the code use domain-specific jargon?** (e.g., "epoch", "middleware", "pod", "migration")
2. **Would a general developer understand the WHY behind the code?** (not just the WHAT)
3. **Are there 3+ concepts that need explaining before the code makes sense?**
4. **Do multiple scripts share the same foundational concepts?**

If **YES** to any → create `00_foundational_knowledge.md`.

---

## Domain Taxonomy & Common Concepts

### 🤖 Machine Learning / Deep Learning

| Concept                 | When to Explain                         |
| ----------------------- | --------------------------------------- |
| ML vs DL vs AI          | Code imports torch, tensorflow, sklearn |
| Training pipeline       | Code has train/valid/test splits        |
| Loss & Optimization     | Code uses optimizer, loss functions     |
| GPU/CUDA                | Code checks `torch.cuda.is_available()` |
| Transfer Learning       | Code loads pretrained models            |
| Metrics (mAP, F1, etc.) | Code evaluates model performance        |
| Data augmentation       | Code transforms training images         |
| Hyperparameters         | Code has configurable training params   |

### 🌐 Web Development

| Concept             | When to Explain                          |
| ------------------- | ---------------------------------------- |
| Client-Server model | Code has API routes or fetch calls       |
| REST vs GraphQL     | Code defines endpoints or resolvers      |
| Authentication      | Code handles JWT, sessions, OAuth        |
| Middleware          | Code uses Express/Koa/Next.js middleware |
| SSR vs CSR vs SSG   | Code uses Next.js or similar framework   |
| State management    | Code uses Redux, Zustand, Context        |
| Database ORMs       | Code uses Prisma, Sequelize, SQLAlchemy  |

### 📱 Mobile Development

| Concept             | When to Explain                   |
| ------------------- | --------------------------------- |
| Component lifecycle | Code handles mount/unmount events |
| Navigation patterns | Code uses stack/tab navigation    |
| Native bridges      | Code calls platform-specific APIs |
| State management    | Code uses providers, BLoC, etc.   |

### 🏗️ DevOps / Infrastructure

| Concept                | When to Explain                         |
| ---------------------- | --------------------------------------- |
| Containers vs VMs      | Code has Dockerfile or docker-compose   |
| CI/CD pipelines        | Code has GitHub Actions, Jenkins config |
| Kubernetes concepts    | Code has k8s manifests (pods, services) |
| Infrastructure as Code | Code uses Terraform, Pulumi, CDK        |

### 💾 Data Engineering

| Concept            | When to Explain                       |
| ------------------ | ------------------------------------- |
| ETL pipeline       | Code extracts, transforms, loads data |
| Batch vs Stream    | Code uses Spark, Kafka, Flink         |
| Data modeling      | Code has schema definitions           |
| Query optimization | Code has complex SQL or aggregations  |

### 🔒 Security

| Concept          | When to Explain                  |
| ---------------- | -------------------------------- |
| Encryption       | Code uses crypto libraries       |
| Auth flows       | Code implements OAuth, SAML, MFA |
| Input validation | Code sanitizes user input        |

---

## Foundational Knowledge Doc Structure

```markdown
# 🧠 Foundational Knowledge — Read Before Starting

> **Goal:** Understand the core concepts needed to read the code.
> If you already know [DOMAIN], feel free to skip this file.

---

## 1. What is [Domain]?

[Simple analogy explaining the entire domain in 3-5 sentences]

## 2. [Core Concept A]

### What is it?

[1-2 sentence definition]

### Real-world analogy

[Everyday comparison]

### Why it matters in this project

[Direct connection to the code]

### Visual

[ASCII diagram or table]

## 3. [Core Concept B]

[Same structure...]

---

## Key Terminology

| Term     | Explanation  | Analogy   |
| -------- | ------------ | --------- |
| [Term 1] | [Definition] | [Analogy] |
| [Term 2] | [Definition] | [Analogy] |

---

## Project Flow Summary

[ASCII diagram showing how scripts/components connect]

> **Next:** [link to first code doc]
```

---

## Tips

- **Don't over-explain** — only include concepts that appear in the actual code
- **Order matters** — explain dependencies first (concept A before B if B uses A)
- **Cross-reference** — link back to foundational doc from code docs when using a term
- **Keep it short** — aim for 200-400 lines max for the foundational doc
