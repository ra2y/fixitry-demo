# Factory Repair Prompt

You are repairing an authorized, intentionally vulnerable demonstration
repository. Work only inside the provided repository directory.

The user approved these Trivy findings:

{{APPROVED_FINDINGS}}

Requirements:

1. Inspect the affected files and explain a short repair plan.
2. Make the smallest safe changes that resolve only the approved findings.
3. Preserve the `/`, `/health`, and `/api/config-status` behavior.
4. Replace hardcoded configuration with environment-based configuration.
5. Preserve local developer setup using a non-secret example file if needed.
6. Run `python -m pytest` after editing.
7. Do not deploy infrastructure.
8. Do not push, merge, or create a pull request.
9. Return a summary of changed files, tests, and any finding that still needs
   human review.

