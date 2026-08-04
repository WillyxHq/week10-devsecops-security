# CI/CD Analysis

## 1. Why should security testing happen before deployment instead of after deployment?

Security testing should occur before deployment because it identifies vulnerabilities early in the software development lifecycle. Detecting issues before code reaches production reduces remediation costs, prevents security incidents, and helps ensure that only secure code is released. This approach supports the DevSecOps principle of integrating security into every stage of development.

---

## 2. Explain Shift Left Security.

Shift Left Security is the practice of moving security activities earlier ("to the left") in the software development lifecycle. Instead of waiting until deployment or production, developers use automated tools to identify and fix vulnerabilities during coding, testing, and pull requests. This leads to faster remediation, lower costs, and more secure software.

---

## 3. What is the purpose of GitHub Actions in an automated workflow?

GitHub Actions automates tasks in the CI/CD pipeline. It can automatically build applications, run tests, perform static application security testing (Bandit), scan dependencies (pip-audit), detect secrets (Gitleaks), and enforce security checks whenever changes are submitted. This ensures consistent and repeatable security validation before code is merged.

---

## 4. What happens if Bandit returns a High severity finding during a pull request check?

If Bandit reports a High severity vulnerability, the GitHub Actions workflow should fail. The failed security check prevents the pull request from being merged until the vulnerability has been reviewed and remediated. This acts as a security gate that blocks insecure code from entering the main branch.

---

## 5. Why are pull requests an ideal place to perform automated security testing?

Pull requests provide a controlled review stage before code is merged. Running automated security scans during pull requests allows vulnerabilities, insecure dependencies, and exposed secrets to be detected before they reach the protected main branch. This supports code review, improves software quality, and enforces security policies consistently across the development team.

