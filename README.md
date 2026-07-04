# 100Hires Portfolio Project - AI Tooling Environment Setup

This public repository contains the technical environment documentation required for the 100Hires junior portfolio project. It outlines the tools requested by Alex Kravets, the precise deployment steps executed, and the raw, real-world troubleshooting process required to get this live.

## Tools Installed
* **Cursor IDE:** Downloaded as the baseline development workspace platform.
* **VS Code:** Installed as an alternative environment when Cursor usage blocks surfaced.
* **Git for Windows:** Installed from scratch to handle local terminal repository pushes.
* **Claude Code & Codex Extensions:** Acquired manually via direct download packages.

## Steps Completed
1. **Workspace Provisioning:** Downloaded and installed Cursor IDE on a clean system architecture.
2. **Repository Configuration:** Initialized a local workspace directory, linked it to a remote public GitHub account, and configured main branch tracking parameters.
3. **Manual Sideloading Matrix:** Extracted missing marketplace extensions by fetching independent package builds.
4. **Issue Tracking:** Systematically isolated command line failures and resolved constraints to stay under the 48-hour deliverable timeline.

## Issues Encountered & Raw Problem Solving

### 1. Zero Prior Coding Experience & Terminal Unknowns
* **Symptom:** Absolute confusion when trying to navigate command prompts, download development binaries, and run scripts like `git init` or `mkdir`.
* **Root Cause:** Total lack of prior software engineering experience. The terminal environment was completely foreign.
* **Resolution:** Executed a heavy trial-and-error loop. Watched multiple YouTube tutorials on how to set up GitHub repositories, but initially understood nothing due to the technical jargon. Instead of quitting, pivoted to using an AI assistant to break down every single terminal error line-by-line, translating complex coding procedures into simple, step-by-step actions until the repository was successfully built.

### 2. Extension Missing from standard IDE Marketplace
* **Symptom:** Searching for `Claude Code` and `Codex` within Cursor's built-in extension marketplace yielded zero results.
* **Root Cause:** Custom IDE forks query separate indexing nodes instead of the full visual studio storefront, missing some proprietary vendor extensions.
* **Resolution:** Bypassed the broken internal marketplace search. Sourced the raw `.vsix` extension package binaries directly from the web browser, then manually sideloaded them into the IDE using the internal command palette.

### 3. Upstream Environment Usage Blockages
* **Symptom:** Workspace environment locked, preventing further testing due to rapid usage threshold blocks.
* **Resolution:** Transferred the local repository configuration smoothly over into a fresh installation of standard open-source **VS Code**, preserving identical project context and bypassing the workspace constraint without stalling the 48-hour deadline.
