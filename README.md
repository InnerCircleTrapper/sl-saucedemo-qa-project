\# SauceDemo QA \& Test Engineering Project



Manual + (planned) automation test assets for the \[Sauce Demo](https://www.saucedemo.com/) sample e‑commerce site.  

\*\*Purpose:\*\* Demonstrate end‑to‑end QA skills: test design, execution evidence, performance analysis, accessibility checks, and traceable defects.



> This repository is a \*portfolio\* style project – not an official Sauce Labs repo.

## Test Scope & Coverage Snapshot

| Area | Included | Notes |
|------|----------|-------|
| Functional (Desktop) | ✅ | Login, inventory listing, cart add/remove, checkout steps, sorting, logout, session clearing |
| Performance | ✅ | TC-010 image load timing (3G baseline captured) |
| Accessibility (Keyboard) | 🟡 (planned) | TC-011 defined (keyboard navigation) **not yet executed** |
| Mobile (Smoke) | ✅ | Add-to-cart flow on Galaxy S22 (BrowserStack) |
| Negative / Validation | 🟡 | Basic invalid creds & form field cases; more planned |
| Automation | 🟡 (planned) | Selenium + pytest scaffold upcoming |
| Performance Optimization | 🟡 | Remediation tasks pending (IMG-PERF-001) |
| Security / API | ❌ | Out of scope for this portfolio |
| Visual Regression | ❌ | Not implemented yet |

### Current Metrics

- **Total Test Cases Defined:** 14  
- **Executed This Cycle:** 10  
- **Pass:** 9  
- **Fail:** 1 (Performance – TC-010)  
- **Not Yet Executed:** 4 (includes TC-011 accessibility)  
- **Open Defects:** 1 (`IMG-PERF-001`)  
- **Performance Baseline (TC-010 Max Image Finish):** 15,293 ms (Threshold ≤ 10,000 ms)  
- **Accessibility Baseline:** _Pending – TC-011 not executed_

> _Legend:_ ✅ Implemented • 🟡 Partial / In Progress • ❌ Not in current scope
