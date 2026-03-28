# 🔐 DevSecOps Pipeline

<div align="center">

![DevSecOps](https://img.shields.io/badge/DevSecOps-Pipeline-blue?style=for-the-badge&logo=github-actions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![SonarCloud](https://img.shields.io/badge/SonarCloud-4E9BCD?style=for-the-badge&logo=sonarcloud&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-Security_Scan-orange?style=for-the-badge&logo=aqua&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-Alerts-4A154B?style=for-the-badge&logo=slack&logoColor=white)
![Bandit](https://img.shields.io/badge/Bandit-SAST-yellow?style=for-the-badge&logo=python&logoColor=white)
![SBOM](https://img.shields.io/badge/SBOM-Syft-green?style=for-the-badge&logo=anchore&logoColor=white)

> **A fully automated, enterprise-grade CI/CD pipeline with security baked in at every stage — secrets scanning, dependency auditing, SAST, DAST, container scanning, SBOM generation, 3-environment deployment with manual approval gate, and real-time stage-level Slack alerts.**

</div>

---

## 📊 Pipeline Health

![Pipeline Status](https://img.shields.io/github/actions/workflow/status/vivek1251/devsecops-pipeline/deploy.yml?label=Pipeline&style=for-the-badge&logo=github-actions)
![Last Commit](https://img.shields.io/github/last-commit/vivek1251/devsecops-pipeline?style=for-the-badge&logo=git&logoColor=white)
![Issues](https://img.shields.io/github/issues/vivek1251/devsecops-pipeline?style=for-the-badge&logo=github)
![Coverage](https://img.shields.io/badge/Coverage-99.4%25-brightgreen?style=for-the-badge&logo=pytest&logoColor=white)
![Security Rating](https://img.shields.io/badge/Security_Rating-A-brightgreen?style=for-the-badge&logo=sonarcloud&logoColor=white)
![Vulnerabilities](https://img.shields.io/badge/Vulnerabilities-0-brightgreen?style=for-the-badge&logo=shield&logoColor=white)
![SBOM](https://img.shields.io/badge/SBOM-Generated-blue?style=for-the-badge&logo=anchore&logoColor=white)
![Dependabot](https://img.shields.io/badge/Dependabot-Enabled-025E8C?style=for-the-badge&logo=dependabot&logoColor=white)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Pipeline in Action](#-pipeline-in-action)
- [Architecture](#-architecture)
- [Pipeline Stages](#-pipeline-stages)
- [3-Environment Deployment](#-3-environment-deployment)
- [Security Tools](#-security-tools)
- [Project Structure](#-project-structure)
- [Setup & Installation](#-setup--installation)
- [Slack Notifications](#-slack-notifications)
- [Contributing](#-contributing)

---

## 🌟 Overview

This project implements a **DevSecOps CI/CD pipeline** that integrates security scanning seamlessly into the software delivery lifecycle. Security is not an afterthought — it is embedded at every stage of the pipeline.

Every push to the repository automatically triggers:

- 🔑 **Secrets scanning** — Gitleaks detects any leaked credentials
- 🐍 **Dependency scanning** — pip-audit checks for CVEs in Python packages
- 🔍 **SAST** — Bandit + SonarCloud perform deep static code analysis
- 🌐 **DAST** — OWASP ZAP full-scan for runtime vulnerabilities
- 🐳 **Build, Push & Scan** — Docker image built, scanned with Trivy, SBOM generated
- 🟡 **Deploy to Staging** — Auto-deploy on every commit
- 🟠 **Deploy to Pre-prod** — Auto-deploy after staging passes
- ⏸️ **Manual Approval Gate** — Human review required before production
- 🟢 **Deploy to Production** — Final deployment after approval
- 📣 **Stage-level Slack alerts** — Real-time pass/fail notifications per stage
- 🤖 **Dependabot** — Automated weekly dependency update PRs

---

## 🎬 Pipeline in Action

### ✅ GitHub Actions — Full Pipeline Run (Success)

> All stages passed — Gitleaks ✅ · pip-audit ✅ · Bandit ✅ · SonarCloud ✅ · OWASP ZAP ✅ · Trivy ✅ · SBOM ✅ · Staging ✅ · Pre-prod ✅ · Production ✅

![GitHub Actions Pipeline](big%20file%201.gif)

---

### 🔍 SonarCloud — Code Quality & Security Results

> Quality Gate: **Passed** · Open Issues: **0** · Duplications: **0.0%** · Coverage: **99.4%** · Security Rating: **A**

![SonarCloud Dashboard](big%20file%203.gif)

---

### 📣 Slack — Real-Time Stage-Level Alerts

> The `devsecops-bot` sends instant Slack notifications per stage — success or failure — with commit info and direct links.

![Slack Alerts](big%20file%202.gif)

---
### 🌍 3-Environment Deploy — Staging → Pre-prod → Production Approval

> Full pipeline passing all stages with manual approval gate for production deployment.

![3-Environment Deploy](big%20file%204.gif)

---

## 🏗️ Architecture

```
Developer Push / Pull Request
            │
            ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          GitHub Actions CI/CD                               │
│                                                                             │
│  ┌──────────┐  ┌───────────┐  ┌──────────────┐  ┌────────┐  ┌──────────┐  │
│  │ Gitleaks │─▶│ pip-audit │─▶│Bandit+Sonar  │─▶│OWASPZap│─▶│Build+    │  │
│  │ Secrets  │  │ Dep Scan  │  │     SAST     │  │  DAST  │  │Trivy+SBOM│  │
│  └──────────┘  └───────────┘  └──────────────┘  └────────┘  └──────────┘  │
│                                                                    │        │
│              ┌─────────────────────────────────────────────────────▼──────┐ │
│              │  🟡 Staging → 🟠 Pre-prod → ⏸️ Manual Approval → 🟢 Prod  │ │
│              └────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                Stage-Level Slack Alerts (each job)                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Pipeline Stages

### 1. 🔑 Secrets — Gitleaks Scan
Scans the entire git history for leaked API keys, passwords, tokens, or credentials.
```yaml
- name: Gitleaks secrets scan
  uses: gitleaks/gitleaks-action@v2
```
> Result: **No leaks detected** ✅

---

### 2. 🐍 Dependency Scan — pip-audit
Audits all Python dependencies in `requirements.txt` against the PyPI Advisory Database for known CVEs.
```yaml
- name: Run pip-audit
  run: pip-audit -r app/requirements.txt --format=json --output=pip-audit-report.json
```
> Report uploaded as downloadable artifact on every run ✅

---

### 3. 🔍 SAST — Bandit + SonarCloud

**Bandit** — Python-specific static security analysis:
```yaml
- name: Run Bandit SAST Scan
  run: bandit -r app/ -f json -o bandit-report.json --exit-zero
```

**SonarCloud** — Deep static analysis for bugs, security hotspots, and code smells:
- Quality Gate: **Passed**
- Security Issues: **0**
- Code Coverage: **99.4%**
- Security Rating: **A**

---

### 4. 🌐 DAST — OWASP ZAP Full-Scan
Actively attacks the running application to find vulnerabilities like XSS, SQL injection, and misconfigurations.
```yaml
- name: OWASP ZAP Scan
  uses: zaproxy/action-full-scan@v0.10.0
```
> 138 checks PASS · 0 FAIL ✅

---

### 5. 🐳 Build, Push, Scan & SBOM
Builds the Docker image, scans with **Trivy**, generates an **SBOM with Syft**, pushes to Docker Hub.
```bash
docker build -t devsecops-app .
trivy image devsecops-app    # CVE scan
syft devsecops-app           # SBOM generation
docker push vivek1251/devsecops-app
```

---

## 🌍 3-Environment Deployment

```
Build & Scan
     │
     ▼
🟡 Staging (auto)          → my-cicd-server      port 5001
     │
     ▼
🟠 Pre-prod (auto)         → cicd-server         port 5000
     │
     ▼
⏸️  Manual Approval Gate   → vivek1251 must approve
     │
     ▼
🟢 Production (approved)   → devsecops-server    port 5000
```

| Environment | Server | Trigger |
|-------------|--------|---------|
| 🟡 Staging | my-cicd-server | Auto on every commit |
| 🟠 Pre-prod | cicd-server | Auto after staging passes |
| 🟢 Production | devsecops-server | Manual approval required |

---

## 🛡️ Security Tools

| Tool | Type | Purpose | Stage |
|------|------|---------|-------|
| **Gitleaks** | Secrets Scan | Detects leaked credentials in git history | Pre-build |
| **pip-audit** | Dependency Scan | CVE scanning of Python packages | Pre-build |
| **Bandit** | SAST | Python-specific static security analysis | Pre-build |
| **SonarCloud** | SAST | Static code quality & security analysis | Pre-build |
| **OWASP ZAP** | DAST | Full active runtime vulnerability testing | Post-deploy |
| **Trivy** | Container Scan | Docker image CVE scanning | Post-build |
| **Syft** | SBOM | Software Bill of Materials generation | Post-build |
| **Dependabot** | Dependency Updates | Automated weekly PRs for outdated packages | Scheduled |
| **Slack Bot** | Alerting | Stage-level real-time notifications | All stages |

---

## 📁 Project Structure

```
devsecops-pipeline/
├── .github/
│   ├── workflows/
│   │   └── deploy.yml              # Main CI/CD pipeline
│   └── dependabot.yml              # Automated dependency updates
├── app/
│   ├── app.py                      # Python Flask application
│   ├── test_app.py                 # Unit tests (99.4% coverage)
│   ├── Dockerfile                  # Container definition
│   └── requirements.txt            # Python dependencies
├── .env.example                    # Required environment variables
├── CONTRIBUTING.md                 # Contribution guidelines
├── LICENSE                         # MIT License
├── sonar-project.properties        # SonarCloud configuration
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.x
- Docker
- GitHub account
- SonarCloud account
- AWS EC2 instances (3 for full environment setup)
- Slack workspace

### Local Setup
```bash
# 1. Clone the repository
git clone https://github.com/vivek1251/devsecops-pipeline.git
cd devsecops-pipeline

# 2. Copy env example and fill in values
cp .env.example .env

# 3. Install dependencies
pip install -r app/requirements.txt

# 4. Run tests
pytest app/ --cov=app

# 5. Run Bandit locally
pip install bandit
bandit -r app/

# 6. Build Docker image
docker build -t devsecops-app ./app

# 7. Scan with Trivy
trivy image devsecops-app
```

### GitHub Secrets Required

Set these in **Settings → Secrets → Actions**:

| Secret | Description |
|--------|-------------|
| `SONAR_TOKEN` | SonarCloud authentication token |
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub password |
| `STAGING_HOST` | Staging EC2 public IP |
| `STAGING_USERNAME` | Staging EC2 SSH username |
| `STAGING_KEY` | Staging EC2 private SSH key |
| `PREPROD_HOST` | Pre-prod EC2 public IP |
| `PREPROD_USERNAME` | Pre-prod EC2 SSH username |
| `PREPROD_KEY` | Pre-prod EC2 private SSH key |
| `EC2_HOST` | Production EC2 public IP |
| `EC2_USERNAME` | Production EC2 SSH username |
| `EC2_KEY` | Production EC2 private SSH key |
| `SLACK_WEBHOOK` | Slack incoming webhook URL |

---

## 📣 Slack Notifications

The pipeline sends **stage-level** real-time Slack alerts:

| Stage | Alert |
|-------|-------|
| 🔑 Gitleaks | ❌ Secret detected in code |
| 🐍 pip-audit | ❌ Vulnerable dependency found |
| 🔍 SAST | ❌ Bandit or SonarCloud Quality Gate failed |
| 🌐 DAST | ❌ OWASP ZAP found critical vulnerabilities |
| 🐳 Trivy | ❌ CRITICAL/HIGH CVE in Docker image |
| 🟡 Staging | ✅ Staging deployed successfully |
| 🟠 Pre-prod | ✅ Pre-prod deployed, awaiting approval |
| 🚀 Production | ✅ Full pipeline passed, production deployed |

---

## 🔮 Future Improvements

| Feature | Effort |
|---------|--------|
| Pipeline metrics dashboard | Advanced |

### ✅ Recently Completed
| Feature | Status |
|---------|--------|
| 3-environment deploy (staging → preprod → prod) | ✅ Done |
| Manual approval gate for production | ✅ Done |
| OWASP ZAP full-scan (vs baseline) | ✅ Done |
| Dependabot auto-PRs for dependency updates | ✅ Done |
| Vigilant mode (commit verification) | ✅ Done |
| pip + Docker layer caching | ✅ Done |
| Stage-level Slack alerts | ✅ Done |
| Branch protection on main | ✅ Done |
| SBOM generation with Syft | ✅ Done |
| Bandit SAST scanning | ✅ Done |
| pip-audit dependency scanning | ✅ Done |

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit your changes: `git commit -m 'feat: add your feature'`
4. Push to the branch: `git push origin feat/your-feature`
5. Open a Pull Request into `main` — all pipeline checks must pass

---

<div align="center">

Made with ❤️ by [vivek1251](https://github.com/vivek1251)

![Security](https://img.shields.io/badge/Security-First-red?style=for-the-badge&logo=shield&logoColor=white)
![Status](https://img.shields.io/badge/Pipeline-Passing-brightgreen?style=for-the-badge&logo=github-actions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Environments](https://img.shields.io/badge/Environments-3-purple?style=for-the-badge&logo=amazon-aws&logoColor=white)

</div>
