# Week 10 DevSecOps Security Report

## Executive Summary

This project implemented a secure DevSecOps pipeline for a Python Flask application using GitHub Actions. The objective was to detect security vulnerabilities automatically before code reaches the main branch. Three automated security tools were integrated into the CI/CD pipeline: Bandit for static application security testing (SAST), pip-audit for dependency scanning, and Gitleaks for secret detection.

---

# Security Tools Used

## 1. Bandit

Purpose:
- Detect insecure Python code.
- Identify dangerous programming practices.

Examples detected:
- eval()
- os.system()
- subprocess(shell=True)
- pickle.loads()
- MD5 hashing

---

## 2. pip-audit

Purpose:
- Scan Python packages.
- Identify packages with known CVEs.

Packages scanned:
- Flask
- Jinja2
- requests

---

## 3. Gitleaks

Purpose:
- Detect secrets committed to source code.

Secrets scanned:
- AWS Secret Key
- GitHub Personal Access Token
- Database Password

---

# Bandit Findings

Bandit identified multiple High and Medium severity issues including:

- Hardcoded password
- Hardcoded API key
- MD5 hashing
- Command Injection via os.system()
- subprocess(shell=True)
- eval()
- pickle.loads()
- Weak random number generation

Risk:
An attacker could execute arbitrary commands, steal credentials, or compromise application integrity.

---

# Dependency Findings

pip-audit detected vulnerable package versions inside requirements.txt.

Affected packages included:

- Flask
- Jinja2
- requests

These packages were upgraded to supported versions to reduce the attack surface.

---

# Secret Findings

Gitleaks detected:

- Fake AWS Secret Access Key
- Fake GitHub PAT
- Fake Database Password

These secrets were removed from source code and replaced with environment variables.

---

# Remediation Steps

The following actions were taken:

- Upgraded vulnerable packages.
- Removed hardcoded credentials.
- Replaced secrets with environment variables.
- Implemented GitHub Actions security pipeline.
- Added automated security gates.

---

# Final Result

After remediation:

- No plaintext secrets remained in source code.
- Dependencies were upgraded.
- Security pipeline executed automatically on pull requests.
- Bandit, pip-audit and Gitleaks became part of the CI/CD workflow.

---

# Lessons Learned

This project demonstrated how DevSecOps integrates security directly into software development.

Key lessons include:

- Security should be automated.
- Shift-left security reduces remediation costs.
- Secrets should never be committed.
- Vulnerable dependencies must be updated regularly.
- Automated pipelines improve software security and developer productivity.

---

# Screenshots

## Failed Pipeline

Insert screenshot showing pipeline failing due to vulnerabilities.

---

## Successful Pipeline

Insert screenshot showing pipeline passing after remediation.
