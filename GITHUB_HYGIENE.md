# GitHub Hygiene Instructions

This document provides instructions for manually configuring repository settings that cannot be automated through the GitHub API with my current permissions.

## 1. Enable Dependabot Security Updates

1.  Navigate to the repository's **Settings** tab.
2.  In the **Security** section of the sidebar, click **Code security and analysis**.
3.  Next to **Dependabot security updates**, click **Enable**.

## 2. Set Repository Topics

1.  On the main page of the repository, click the **Settings** icon next to the **About** section.
2.  In the **Topics** field, add the following topics, separated by spaces:
    `agents-cli` `orchestrator` `observability` `security` `benchmarks` `prometheus` `grafana`

## 3. Configure Branch Protection for `main`

1.  Navigate to the repository's **Settings** tab.
2.  In the **Code and automation** section of the sidebar, click **Branches**.
3.  Next to **Branch protection rules**, click **Add rule**.
4.  In the **Branch name pattern** field, type `main`.
5.  Enable **Require a pull request before merging**.
6.  Enable **Require status checks to pass before merging**.
7.  Search for and select the following status checks:
    *   `gitleaks`
    *   `detect-secrets`
    *   `benchmark` (from the nightly workflow)
8.  Enable **Do not allow bypassing the above settings**.
9.  Click **Create**.
