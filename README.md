<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=200&section=header&text=CI%2FCD%20Gatekeeper&fontSize=44&fontColor=ffffff&fontAlignY=38&desc=Gate%20expensive%20ML%20training%20on%20quality%2C%20branch%2C%20and%20intent&descSize=16&descAlignY=60&animation=fadeIn" alt="banner" />

<br/>

[![Stars](https://img.shields.io/github/stars/jilan111/ci-cd-gatekeeper-pipeline?style=for-the-badge&color=0d1117&labelColor=161b22&logo=star)](https://github.com/jilan111/ci-cd-gatekeeper-pipeline/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/jilan111/ci-cd-gatekeeper-pipeline?style=for-the-badge&color=0d1117&labelColor=161b22&logo=git)](https://github.com/jilan111/ci-cd-gatekeeper-pipeline/commits)
[![License: MIT](https://img.shields.io/badge/License-MIT-0d1117?style=for-the-badge&labelColor=161b22)](LICENSE)

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</div>

---

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
