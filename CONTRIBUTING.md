# Contributing to DevSecOps Pipeline

Thank you for your interest in contributing! 🎉

## 🚀 Getting Started

1. Fork the repository
2. Clone your fork
```bash
   git clone https://github.com/your-username/devsecops-pipeline.git
   cd devsecops-pipeline
```
3. Create a feature branch
```bash
   git checkout -b feat/your-feature
```

## ⚙️ Local Setup

1. Install dependencies
```bash
   pip install -r app/requirements.txt
```
2. Copy the example env file
```bash
   cp .env.example .env
   # Fill in your values
```
3. Run tests locally
```bash
   cd app
   python -m pytest test_app.py --cov=.
```
4. Run Bandit locally
```bash
   pip install bandit
   bandit -r app/
```

## 📋 Pull Request Guidelines

- Always branch off `main`
- All 5 pipeline checks must pass before merging
- Use conventional commits:
  - `feat:` new feature
  - `fix:` bug fix
  - `perf:` performance improvement
  - `ci:` pipeline changes
  - `docs:` documentation only

## 🔐 GitHub Secrets Required

See `.env.example` for all required secrets. Add them in:
```
Settings → Secrets → Actions
```

## 🛡️ Security

Found a vulnerability? Please open a private security advisory instead of a public issue.