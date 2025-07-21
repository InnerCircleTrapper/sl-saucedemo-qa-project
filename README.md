\# SauceDemo QA \& Test Engineering Project

<p align="center">
  <img src="assets/og-banner.png"
       alt="SauceDemo QA & Test Engineering Project – manual, performance, accessibility (pending)"
       width="100%">
</p>




Manual + (planned) automation test assets for the \[Sauce Demo](https://www.saucedemo.com/) sample e‑commerce site.  

\*\*Purpose:\*\* Demonstrate end‑to‑end QA skills: test design, execution evidence, performance analysis, accessibility checks, and traceable defects.



> This repository is a \*portfolio\* style project – not an official Sauce Labs repo.

## Test Scope & Coverage Snapshot

| Area | Included | Notes |
|------|----------|-------|
| Functional (Desktop) | ✅ | Login, inventory listing, cart add/remove, checkout steps, sorting, logout, session clearing |
| Performance | ✅ (executed) | **TC-010 FAIL** – max image finish 15,293 ms (>10,000 ms threshold) (IMG-PERF-001) |
| Accessibility (Keyboard) | ✅ (executed) | **TC-011 FAIL** – missing visible focus indicator (ACC-FOCUS-001) |
| Mobile (Smoke) | ✅ (executed) | Add-to-cart flow defined – **TC-012 PASS** |
| Negative / Validation | 🟡 | Basic invalid creds & form field cases; more planned |
| Automation (pytest scaffold) | 🟡 (planned) | TC‑015 defined – framework not yet executed |

| Performance Optimization | 🟡 | Remediation tasks pending (IMG-PERF-001) |
| Security / API | ❌ | Out of scope for this portfolio |
| Visual Regression | ❌ | Not implemented yet |

### Current Metrics

- **Total Test Cases Defined:** 15  
- **Executed This Cycle:** 14  
- **Pass:** 11  
- **Fail:** 3 (Performance – TC‑010, Accessibility – TC‑011, Performance – TC‑014)  
- **Not Yet Executed:** 1  
- **Pass %:** 78.6 %
- **Open Defects:** IMG-PERF-001, ACC-FOCUS-001, PERF-LH-BASE-001


> _Legend:_ ✅ Implemented • 🟡 Partial / In Progress • ❌ Not in current scope

## Repository Structure

> *Evolving layout – currently definitions & executions are combined; will be split for maintainability.*

```text
.
├── manual-evidence/
│   ├── execution_report.md      # Test case executions + evidence links (includes TC-010 + TC-011 fails)
│   └── screenshots/             # PNG evidence assets
├── assets/                      # Social preview / icons (e.g., og-banner.png)
├── env/                         # (Planned) Environment & tooling notes (browser versions, network profiles)
├── test-cases/                  # (Planned) Individual static TC definition files (TC-001.md etc.)
├── automation/                  # (Planned) Selenium / pytest (or Playwright) smoke tests
├── defects/                     # (Planned) Markdown defect records (one per issue) or ISSUE_TEMPLATE
└── README.md
