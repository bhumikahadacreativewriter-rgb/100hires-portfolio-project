# 100Hires Portfolio Project

Portfolio project for the 100Hires program, requested by Alex Kravets. Two milestones so
far: (1) getting a working AI-assisted dev environment set up, and (2) building a
research dataset on B2B SaaS organic content strategy.

## Milestone 1: AI Tooling Environment Setup

This repository originally contains the technical environment documentation required for
the 100Hires junior portfolio project. It outlines the tools requested by Alex Kravets,
the precise deployment steps executed, and the raw, real-world troubleshooting process
required to get this live.

### Tools Installed
* **Cursor IDE:** Downloaded as the baseline development workspace platform.
* **VS Code:** Installed as an alternative environment when Cursor usage blocks surfaced.
* **Git for Windows:** Installed from scratch to handle local terminal repository pushes.
* **Claude Code & Codex Extensions:** Acquired manually via direct download packages.

### Steps Completed
1. **Workspace Provisioning:** Downloaded and installed Cursor IDE on a clean system architecture.
2. **Repository Configuration:** Initialized a local workspace directory, linked it to a remote public GitHub account, and configured main branch tracking parameters.
3. **Manual Sideloading Matrix:** Extracted missing marketplace extensions by fetching independent package builds.
4. **Issue Tracking:** Systematically isolated command line failures and resolved constraints to stay under the 48-hour deliverable timeline.

### Issues Encountered & Raw Problem Solving

#### 1. Zero Prior Coding Experience & Terminal Unknowns
* **Symptom:** Absolute confusion when trying to navigate command prompts, download development binaries, and run scripts like `git init` or `mkdir`.
* **Root Cause:** Total lack of prior software engineering experience. The terminal environment was completely foreign.
* **Resolution:** Executed a heavy trial-and-error loop. Watched multiple YouTube tutorials on how to set up GitHub repositories, but initially understood nothing due to the technical jargon. Instead of quitting, pivoted to using an AI assistant to break down every single terminal error line-by-line, translating complex coding procedures into simple, step-by-step actions until the repository was successfully built.

#### 2. Extension Missing from standard IDE Marketplace
* **Symptom:** Searching for `Claude Code` and `Codex` within Cursor's built-in extension marketplace yielded zero results.
* **Root Cause:** Custom IDE forks query separate indexing nodes instead of the full visual studio storefront, missing some proprietary vendor extensions.
* **Resolution:** Bypassed the broken internal marketplace search. Sourced the raw `.vsix` extension package binaries directly from the web browser, then manually sideloaded them into the IDE using the internal command palette.

#### 3. Upstream Environment Usage Blockages
* **Symptom:** Workspace environment locked, preventing further testing due to rapid usage threshold blocks.
* **Resolution:** Transferred the local repository configuration smoothly over into a fresh installation of standard open-source **VS Code**, preserving identical project context and bypassing the workspace constraint without stalling the 48-hour deadline.

## Milestone 2: B2B SaaS LinkedIn Organic Content Strategy Playbook

This part of the repository contains a curated, high-signal research dataset analyzing
organic distribution frameworks for B2B SaaS companies. Instead of gathering generic
surface-level advice, this project focuses heavily on active agency founders, SaaS
executives, and deep-funnel copywriters who back their strategies with transparent data
and case studies.

### 🕵️‍♂️ Selection Thesis (Why These Experts?)
Most automated tools pull up generic marketing influencers. To ensure high-quality, actionable playbooks, 10 practitioners were manually vetted based on two strict criteria:
1. They run a real marketing agency or scaling SaaS business today.
2. They share raw metrics, hook templates, and proven psychological frameworks rather than generic tips.

### 🛠️ Technical Execution
* **Folder Architecture:** Structured strictly according to project specifications under the `/research/` workspace.
* **Automation:** Built a custom Python script (`research/fetch_youtube.py`) using the `youtube-transcript-api` to programmatically extract raw transcript data without manual copying.
* **LinkedIn:** No free, ToS-compliant API exists for post content, so LinkedIn posts are collected manually into a consistent per-author markdown template (see `research/linkedin-posts/README.md`).

### 📊 Collection Status (as of 2026-07-08)

| Expert | Platform | Content collected |
|---|---|---|
| Justin Welsh | LinkedIn | 0 posts (template ready) |
| Lara Acosta | LinkedIn | 0 posts (template ready) |
| Nick Bennett | LinkedIn | 0 posts (template ready) |
| Sam Browne | LinkedIn | 0 posts (template ready) |
| Ryan Musselman | LinkedIn | 0 posts (template ready) |
| Jasmin Alić | LinkedIn | 0 posts (template ready) |
| Dina Calakovic | LinkedIn | 0 posts (template ready) |
| Melissa Kwan | LinkedIn / YouTube | 0 posts, 3 transcripts |
| Christopher Lochhead | YouTube | 1 transcript |
| TK Kader | YouTube | 3 transcripts |

**Totals:** 7 YouTube transcripts across 3 experts, 0 LinkedIn posts collected yet across 8 experts.

**Known gap:** LinkedIn post collection hasn't started — next step is manually pulling
3-5 representative posts per LinkedIn-focused author into their `posts.md` file.
