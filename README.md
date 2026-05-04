# CI/CD Gatekeeper Pipeline

A smart CI/CD pipeline that gates expensive ML training jobs based on **code quality**, **branch protection**, and **explicit developer intent** — preventing wasted compute on incomplete or low-quality changes.

![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue)
![Python](https://img.shields.io/badge/python-3.10+-blue)

---

## Why this exists

ML training jobs burn compute hours and money. Running them on every push or every branch is wasteful. This pipeline introduces a **gatekeeper layer** that lets training jobs run only when:

1. **Code quality checks pass** — lint, type-check, unit tests
2. **Branch is protected** — main / release branches only
3. **Developer signals intent** — commit message tag, PR label, or manual dispatch

If any gate fails, the expensive training step is skipped and the pipeline reports why.

---

## How it works

```
Push / PR
   │
   ▼
┌─────────────────┐
│ Quality checks  │  lint · tests · type-check
└────────┬────────┘
         │ pass
         ▼
┌─────────────────┐
│ Gate evaluation │  branch · commit tag · PR label
└────────┬────────┘
         │ pass
         ▼
┌─────────────────┐
│  ML training    │  expensive job runs only here
└─────────────────┘
```

---

## Quick start

1. Copy `.github/workflows/` into your repo
2. Configure protected branches in repo settings
3. Tag commits with `[train]` (or apply the `train` PR label) when you want training to run
4. Push — the gatekeeper handles the rest

---

## Tech stack

- GitHub Actions
- Python 3.10+
- Configurable per-project gate rules

---

## Author

Built by **Jilan Ismail** — [GitHub](https://github.com/jilan111) · [LinkedIn](https://www.linkedin.com/in/jilan-ismail-596b2b2b2/)
