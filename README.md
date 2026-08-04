# Week 10 DevSecOps Security Pipeline

## Project Overview

This project demonstrates the implementation of a secure DevSecOps CI/CD pipeline for a Python Flask application. The pipeline integrates automated security testing into the software development lifecycle to detect insecure code, vulnerable dependencies, and exposed secrets before code is merged into the main branch.

---

## Project Structure

```
week10-devsecops-security/
├── app/
│   └── app.py
├── docs/
│   ├── security_report.md
│   ├── threat_analysis.md
│   └── cicd_analysis.md
├── .github/
│   └── workflows/
│       └── security-pipeline.yml
├── requirements.txt
└── README.md
```

---

## Security Tools

- Bandit (Static Application Security Testing)
- pip-audit (Dependency Scanning)
- Gitleaks (Secret Detection)
- GitHub Actions (CI/CD Automation)

---

## Running the Project

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/app.py
```

---

## GitHub Actions

The workflow automatically runs on every pull request to the `main` branch and performs:

- Bandit security scan
- Dependency audit using pip-audit
- Secret detection using Gitleaks

If vulnerabilities or secrets are detected, the workflow fails and blocks the merge until the issues are resolved.

---

## Author

TechRise 3.0 – Cybersecurity & DevSecOps

# trigger workflow
