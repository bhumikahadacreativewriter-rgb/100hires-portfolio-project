# 100Hires Portfolio Project - AI Tooling Environment Setup

This public repository contains the technical environment documentation required for the 100Hires junior portfolio project. It outlines the tools requested by Alex Kravets, the precise deployment steps executed, and the engineering workarounds utilized to resolve unexpected dependency blocks.

## Tools Installed
* **Cursor IDE:** Installed as the baseline development workspace platform.
* **VS Code:** Leveraged as a structural, unlimited failover environment when IDE API throttling blocks surfaced.
* **Claude Code Extension (Anthropic):** Sideloaded onto the workspace framework to hook directly into backend LLM workflows.
* **Codex Extension:** Added to provide matching syntax structural analysis.

## Steps Completed
1. **Workspace Provisioning:** Downloaded and installed Cursor IDE on the local system architecture.
2. **Repository Configuration:** Initialized a local workspace directory, linked it to a remote public GitHub storage tree, and configured the main branch tracking parameters.
3. **Manual Sideloading Matrix:** Extracted missing marketplace extensions by fetching independent package builds and applying localized system scripts.
4. **Issue Tracking:** Isolated execution failures and systematically resolved constraints to stay under the 48-hour deliverable timeline.

## Issues Encountered & Engineering Solutions

### 1. Extension Missing from standard IDE Marketplace
* **Symptom:** Searching for `Claude Code` and `Codex` within the internal Extension store yielded no active results.
* **Root Cause:** Custom IDE forks like Cursor query distinct Open VSX indexing nodes instead of the full commercial marketplace, missing some proprietary vendor extensions.
* **Resolution:** Bypassed the search entirely by querying the package nodes, pulling down the raw `.vsix` binaries locally, and running the internal installer layer:
  ```bash
  # Inside the IDE Command Palette (Ctrl+Shift+P)
  Extensions: Install from VSIX... -> Selected downloaded file packages
  ```

### 2. Upstream AI Limit Restrictions
* **Symptom:** Workspace environment locked prompting a standard usage threshold message.
* **Root Cause:** Fast request tiers expired under active usage testing patterns.
* **Resolution:** Transitioned the local repository configurations seamlessly over into standard open-source **VS Code**, preserving identical project context and structural rules to avoid timeline disruption.
 
