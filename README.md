# Secrets in Git – Detection & Prevention Using Gitleaks

A practical demonstration of detecting and preventing committed secrets using both **GitHub Advanced Security** and **Gitleaks** in a CI/CD pipeline.
This project was developed as a 10-minute demo for **CSEC141 (Fall 2025)** and serves as a portfolio example for DevSecOps practices.

[![CI - Test (Clean Control)](https://github.com/crow50/scanning-secrets-demo/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/crow50/scanning-secrets-demo/actions/workflows/test.yml)

[![Secrets Scan](https://github.com/crow50/scanning-secrets-demo/actions/workflows/secrets-scan.yml/badge.svg?branch=main)](https://github.com/crow50/scanning-secrets-demo/actions/workflows/secrets-scan.yml)

<img alt="gitleaks badge" src="https://img.shields.io/badge/protected%20by-gitleaks-blue">


---

## Why Secrets Scanning Matters

Accidentally committing secrets like API keys or passwords to a public repository can expose sensitive systems to attackers. Even brief exposure can lead to:

* Unauthorized access to cloud resources
* Data breaches or service disruptions
* Costly incident response and key rotation efforts

---

## What Counts as a Secret?

A "secret" can be any sensitive value not intended for the public:

* API keys (AWS, Azure, GCP)
* Database connection strings
* Access tokens or SSH keys
* User credentials or OAuth secrets

---

## GitHub Advanced Security

* **Built-in Secret Scanning:**
  All public repositories automatically have GitHub's native secret scanning enabled. It alerts repo owners when known secret patterns, such as AWS Keys, are pushed.

* **Push Protection:**
  Blocks commits containing *supported* secret types before they leave the local environment.

* **Limitations:**

  * Only covers predefined secret patterns
  * No custom rule support
  * Alerts after-the-fact unless Push Protection is enabled

---

## Gitleaks Integration in CI/CD

[Gitleaks](https://github.com/gitleaks/gitleaks) is an open-source secrets scanning tool. In this demo, it is integrated into a GitHub Actions workflow to:

1. Scan commits and pull requests for **known** and **custom** patterns
2. Fail the CI pipeline if secrets are detected
3. Provide auditable logs for security reviews

Key advantages:

* Supports **custom regex rules** for org-specific secrets
* Detects **high-entropy strings** likely to be secrets
* Works on **local hooks** (pre-commit) and CI pipelines

---

## Project Structure

```
scanning-secrets-demo/
|- .github/workflows/
|-- test.yml
|-- gitleaks-scanning.yml
|- src/
|-- __init__.py
|-- app.py
|-- utils.py
|- tests/test_app.py
|- LICENSE
|- README.md
|- requirements.txt
|- .gitignore
```

---

## Demo Workflow

1. **Native Protection** – Show GitHub blocking a known secret pattern via Push Protection.
2. **CI/CD Enforcement** – Push code containing a fake secret → Gitleaks scans → pipeline fails.
3. **Remediation** – Remove the secret, push clean code → pipeline passes.

---

## Local Development

To run demo files:

```bash
# Activate Python venv
python3 -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the app
python3 -m src.app

# Run tests
python3 -m pytest -q
```
![Local Demo Run](local-demo-run.png)

To run Gitleaks locally (Optional):

```bash
# Install gitleaks
brew install gitleaks   # Mac
choco install gitleaks  # Windows
sudo apt install gitleaks # Linux

# Run scan
gitleaks detect # --source . # set source string default $PWD # --no-git # to scan current repo dir # --redact # to redact secrets from logs and stdout
```
![Local Gitleaks Run](local-gitleaks-scan.png)

---

## License

This project is licensed under the MIT License.

---