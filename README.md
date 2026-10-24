# SecureFix Vulnerable Demo

> WARNING: This repository is intentionally insecure. It is only for local,
> authorized security-scanning demonstrations. Do not deploy it to the public
> internet and do not place real credentials in it.

This small Flask application is a controlled target for a SecureFix demo using:

- Trivy to identify vulnerable dependencies, secrets, and misconfigurations.
- Factory Droid SDK to prepare and test repairs.
- Convex to store findings, approvals, progress events, and final results.

## Intentional findings

The starting version contains four categories of problems:

1. Old Python dependencies in `requirements.txt`.
2. A clearly fake hardcoded key in `app/config.py`.
3. An insecure `Dockerfile` that runs as root.
4. Insecure example AWS Terraform in `infra/main.tf`.

The key and infrastructure names are fake. The Terraform is never meant to be
applied.

## Run the application locally

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m app.main
```

Open `http://127.0.0.1:5000/health`.

## Run the tests

```powershell
python -m pytest
```

## Scan with Trivy

Run this command from the repository root so Trivy automatically loads the
included `trivy-secret.yaml` rule:

```powershell
trivy fs --scanners vuln,secret,misconfig .
```

To save machine-readable results for SecureFix:

```powershell
trivy fs --scanners vuln,secret,misconfig --format json --output trivy-results.json .
```

Do not commit `trivy-results.json`; it is ignored by `.gitignore`.

## Suggested demo

1. Push this starting version to a private or clearly labeled demo repository.
2. Submit its URL through the SecureFix React dashboard.
3. Let the worker clone it into a temporary directory.
4. Run Trivy and send the JSON findings to Convex.
5. Display the findings and ask for human approval.
6. Give Factory one approved category at a time.
7. Run the tests and Trivy again.
8. Show the before-and-after counts and code diff.

For a short demo, repair the hardcoded key and Docker root-user issue first.
They are visually clear and do not depend on a changing vulnerability database.

## Factory prompt

A reusable prompt is provided in `SECUREFIX_PROMPT.md`. Substitute only the
approved findings; do not send the entire raw Trivy report if it is large.

