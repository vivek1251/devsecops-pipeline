# 🛡️ DevSecOps Pipeline — Security-First CI/CD

[![Pipeline](https://github.com/vivek1251/devsecops-pipeline/actions/workflows/deploy.yml/badge.svg)](https://github.com/vivek1251/devsecops-pipeline/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-grade **DevSecOps pipeline** that automatically scans for vulnerabilities, blocks insecure deployments, and delivers secure code to AWS EC2 — with real-time Slack alerts on every run.

> 💡 **The Problem:** Most teams catch vulnerabilities *after* deployment. This pipeline catches them *before* — shifting security left into every git push.

---

## 🚀 Live Pipeline

```
Code Push → GitHub Actions
     ↓
🔍 SAST — SonarCloud (Static Code Analysis)
     ↓
🌐 DAST — OWASP ZAP (Dynamic Attack Simulation)
     ↓
📦 Trivy — Container Image Security Scan
     ↓
🐳 Docker Build & Push to DockerHub
     ↓
☁️ Deploy to AWS EC2
     ↓
📲 Slack Alert (✅ Pass / ❌ Fail)
```

---

## ✨ What Makes This Different

| Feature | What it proves |
|---|---|
| SAST with SonarCloud | Catches SQL injection, hardcoded secrets, code smells before build |
| DAST with OWASP ZAP | Simulates real attacks against live app — finds runtime vulnerabilities |
| Trivy Container Scan | Scans Docker image for CVEs before pushing to DockerHub |
| Auto-blocked deployment | Pipeline fails and blocks deploy if critical vulnerabilities found |
| Slack alerts | Real-time ✅ pass / ❌ fail notifications with commit ID |
| Zero manual intervention | Entire security review automated on every git push |

---
## Demo

### GitHub Actions Pipeline
![Pipeline](f1.gif)

### SonarQube Analysis
![SonarQube](f2.gif)

### Slack Notifications
![Slack](f3.gif)

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python + Flask | REST API with intentional vulnerabilities for scanning |
| Docker | Containerization |
| DockerHub | Image registry |
| GitHub Actions | CI/CD orchestration |
| SonarCloud | SAST — static code analysis |
| OWASP ZAP | DAST — dynamic security scanning |
| Trivy | Container image vulnerability scanning |
| AWS EC2 | Cloud deployment target |
| Slack Webhooks | Real-time pipeline alerts |

---

## 📁 Project Structure

```
devsecops-pipeline/
├── app/
│   ├── app.py              # Flask app with intentional vulnerabilities
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Container configuration
├── .github/
│   └── workflows/
│       └── deploy.yml      # Full DevSecOps pipeline
├── sonar-project.properties # SonarCloud configuration
└── README.md
```

---

## ⚙️ Pipeline Stages

### Stage 1 — SAST (SonarCloud)
Scans source code for:
- SQL Injection vulnerabilities
- Hardcoded credentials
- Code smells and maintainability issues
- Security hotspots

**Result:** 8 issues detected in `app/app.py` including hardcoded password and SQL injection

### Stage 2 — DAST (OWASP ZAP)
- Builds and runs the app temporarily
- Simulates real-world attacks against live endpoints
- Scans `/health`, `/search`, `/user` endpoints
- Reports HIGH/MEDIUM/LOW vulnerability findings

### Stage 3 — Trivy Container Scan
- Scans the Docker image for known CVEs
- Checks base image and installed packages
- Fails pipeline on CRITICAL vulnerabilities

### Stage 4 — Build, Push & Deploy
- Builds Docker image
- Pushes to DockerHub
- SSH deploys to AWS EC2
- Sends Slack success alert

### Stage 5 — Notify Failure
- Fires only when any stage fails
- Sends ❌ Slack alert with commit ID
- Links directly to failed GitHub Actions run

---

## 🔐 GitHub Secrets Required

| Secret | Description |
|---|---|
| `SONAR_TOKEN` | SonarCloud authentication token |
| `DOCKER_USERNAME` | DockerHub username |
| `DOCKER_PASSWORD` | DockerHub password |
| `EC2_HOST` | AWS EC2 public IP |
| `EC2_USERNAME` | EC2 SSH username (ubuntu) |
| `EC2_KEY` | EC2 PEM key (base64 encoded) |
| `SLACK_WEBHOOK` | Slack incoming webhook URL |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/vivek1251/devsecops-pipeline.git
cd devsecops-pipeline
```

### 2. Set up SonarCloud
- Go to [sonarcloud.io](https://sonarcloud.io)
- Sign in with GitHub
- Create organization with key `vivek1251`
- Analyze `devsecops-pipeline` project
- Copy `SONAR_TOKEN`

### 3. Add GitHub Secrets
Go to **Settings → Secrets and variables → Actions** and add all 7 secrets listed above.

### 4. Push to trigger pipeline
```bash
git push origin main
```

Watch GitHub Actions — all 4 stages run automatically!

---

## 📊 Security Scan Results

SonarCloud detected **8 issues** in the intentionally vulnerable app:

- 🔴 **Hardcoded password** — `DB_PASSWORD = "admin123"` (Line 9)
- 🔴 **SQL Injection** — unsanitized query in `/search` endpoint
- 🔴 **Command Injection** — `os.system()` with user input in `/user` endpoint
- 🟡 **HTTP method not restricted** — routes accept all methods

> These vulnerabilities are **intentional** to demonstrate SAST detection capabilities.

---

## 🔄 How to Test

**Test pipeline pass:**
```bash
git commit -m "test: trigger pipeline" --allow-empty
git push
```

**Test failure alert:**
```bash
# Break the Dockerfile temporarily
# Change: RUN pip install -r requirements.txt
# To:     RUN pip install -r requirements_broken.txt
git add . && git commit -m "test: trigger failure" && git push
# Watch Slack for ❌ alert
# Then revert: git revert HEAD && git push
```

---

## 📲 Slack Alerts

**On success:**
```
✅ DevSecOps Pipeline passed! SAST + DAST + Trivy clean. App deployed to EC2.
```

**On failure:**
```
❌ DevSecOps Pipeline FAILED! Check GitHub Actions for details. Commit: abc1234
```

---

## 👨‍💻 Author

**Vivek Bommalla** — DevOps & Cloud Engineer

- 🌐 Portfolio: [vivek1251-portfolio.vercel.app](https://vivek1251-portfolio.vercel.app)
- 💼 LinkedIn: [linkedin.com/in/vivekbommalla1251](https://linkedin.com/in/vivekbommalla1251)
- 🐙 GitHub: [github.com/vivek1251](https://github.com/vivek1251)

---

## 📄 License

MIT License — feel free to use this as a template for your own DevSecOps pipeline!

---

⭐ If this project helped you, please give it a star — it means a lot!

