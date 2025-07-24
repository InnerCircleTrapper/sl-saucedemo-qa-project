\# SauceDemo Manual Test Execution Report

\_Date:\_ 2025-07-16  

\_Build / URL:\_ https://www.saucedemo.com  

\_Tester:\_ Steve Louis (SL)  

\_Environment ref:\_ See \[`env-notes.md`](../env-notes.md)



\## Legend

\*\*P\*\* = Pass | \*\*F\*\* = Fail | \*\*B\*\* = Blocked (env / data) | \*\*N/R\*\* = Not Run  

\_Defect ID\_ column links to GitHub Issue numbers (e.g., `#3`).  



## Run Summary (2025‑07‑20)

| Total Cases | Executed | Passed | Failed | Blocked | Not Run | Pass % (Executed) |
|-------------|----------|--------|--------|---------|---------|-------------------|
| **15**      | **15**   | **12** | **3**  | 0       | 0       | **80 %** |

**Executed Through:** TC‑014  
**Fails:** TC‑010 (IMG‑PERF‑001), TC‑011 (ACC‑FOCUS‑001), TC‑014 (PERF‑LH‑BASE‑001)  
> Pass % = Passed ÷ Executed = 12 ÷ 15 ≈ 80%



## Detailed Results

| TC ID  |Result| Defect ID        | Notes |
| TC-010 | Inventory Images Load (Fast 3G) | Low | FAIL | [IMG‑PERF‑001](../issues/11) | Max image finish 15 293 ms |
| TC-011 | Keyboard Tab Navigation Accessible | Low | FAIL | [ACC‑FOCUS‑001](../issues/12) | No visible focus ring |
| TC-014 | Lighthouse Performance Baseline | Low | FAIL | [PERF‑LH‑BASE‑001](../issues/13) | Inventory score 73 |


| TC-001 | Valid Login (standard_user)             | High     | PASS   |                  |       |
| TC-002 | Locked-Out User Blocked on Login        | High     | PASS   |                  |       |
| TC-003 | Add Single Item to Cart                 | High     | PASS   |                  |       |
| TC-004 | Remove Item from Cart                   | Medium   | PASS   |                  |       |
| TC-005 | Complete Checkout Happy Path            | High     | PASS   |                  |       |
| TC-006 | Checkout Missing Zip Validation         | Medium   | PASS   |                  |       |
| TC-007 | Sort Products Price Low→High            | Low      | PASS   |                  |       |
| TC-008 | Logout Ends Session                     | Medium   | PASS   |                  |       |
| TC-009 | Session Cleared on Cookie Delete        | Low      | PASS   |                  |       |
| TC-010 | Inventory Images Load (Fast 3G)         | Low      | FAIL   |  [IMG‑PERF‑001](../issues/11)     | Max image finish 15,293 ms > 10,000 ms threshold |
| TC-011 | Keyboard Tab Navigation Accessible      | Low      | FAIL   | [ACC‑FOCUS‑001](../issues/12)    | Missing visible focus indicator footer links |
| TC-012 | Error Banner Can Be Dismissed           | Low      | PASS   |                  | Banner closed; icons cleared |
| TC-013 | Mobile Add-to-Cart Smoke (Galaxy S22)   | Medium?  | PASS   |                  | Scroll down bit laggy |
| TC-014 | Lighthouse Performance Baseline         | Low      | FAIL   |                  [PERF‑LH‑BASE‑001](../issues/13)| Planned automated perf baseline |
| TC-015 | Automation Smoke Script (pytest) | Low | PASS | | Framework task |



\## Test Case Details



\### TC-001 – Valid Login (standard\_user)

\*\*Preconditions:\*\* User on Login page; valid creds exist (`standard\_user / secret\_sauce`).  

\*\*Steps:\*\*  

1\. Navigate to https://www.saucedemo.com.  

2\. Enter username `standard\_user`.  

3\. Enter password `secret\_sauce`.  

4\. Click \*\*Login\*\*.  

\*\*Expected:\*\* Browser redirects to `/inventory.html`; “Products” header visible; no error banner; cart badge = 0.  

\*\*Priority:\*\* High



\### TC-002 – Locked-Out User Blocked on Login

\*\*Preconditions:\*\* On Login page.  

\*\*Steps:\*\*  

1\. Enter username `locked\_out\_user`.  

2\. Enter password `secret\_sauce`.  

3\. Click \*\*Login\*\*.  

\*\*Expected:\*\* Remain on Login page; error banner text contains “Sorry, this user has been locked out.”  

\*\*Priority:\*\* High



\### TC-003 – Add Single Item to Cart

\*\*Preconditions:\*\* Logged in as `standard\_user`; cart badge = 0.  

\*\*Steps:\*\*  

1\. From Inventory, click \*\*Add to cart\*\* for “Sauce Labs Backpack.”  

2\. Click cart icon (top-right).  

\*\*Expected:\*\* Cart badge = 1; Cart page lists “Sauce Labs Backpack,” qty 1, price matches inventory.  

\*\*Priority:\*\* High



\### TC-004 – Remove Item from Cart

\*\*Preconditions:\*\* Logged in; cart contains ≥1 item (prefer Backpack).  

\*\*Steps:\*\*  

1\. Click cart icon.  

2\. Click \*\*Remove\*\* for the item.  

\*\*Expected:\*\* Item removed from cart; badge decrements; if cart becomes empty badge disappears.  

\*\*Priority:\*\* Medium



\### TC-005 – Complete Checkout Happy Path

\*\*Preconditions:\*\* Logged in; cart contains ≥1 item; on Cart page.  

\*\*Steps:\*\*  

1\. Click \*\*Checkout\*\*.  

2\. On Step One, enter First Name “Alex”, Last Name “Jones”, Zip “10001”; click \*\*Continue\*\*.  

3\. On Overview, verify items \& totals; click \*\*Finish\*\*.  

\*\*Expected:\*\* Checkout complete page appears with “Thank you for your order!” message and confirmation graphic; cart badge resets to 0.  

\*\*Priority:\*\* High



\### TC-006 – Checkout Missing Zip Validation

\*\*Preconditions:\*\* Cart contains ≥1 item; at Checkout Step One form.  

\*\*Steps:\*\*  

1\. Enter First Name \& Last Name; leave Zip blank.  

2\. Click \*\*Continue\*\*.  

\*\*Expected:\*\* Error banner displays “Error: Postal Code is required”; user remains on Step One; Zip field highlighted.  

\*\*Priority:\*\* Medium



\### TC-007 – Sort Products Price Low→High

\*\*Preconditions:\*\* Logged in on Inventory page.  

\*\*Steps:\*\*  

1\. Open sort dropdown (top-right).  

2\. Select \*\*Price (low to high)\*\*.  

\*\*Expected:\*\* Items reorder by ascending price; “Sauce Labs Onesie” (lowest price) appears at top.  

\*\*Priority:\*\* Low



\### TC-008 – Logout Ends Session

\*\*Preconditions:\*\* Logged in on any page.  

\*\*Steps:\*\*  

1\. Click the hamburger (≡) menu.  

2\. Click \*\*Logout\*\*.  

3\. Press browser Back button.  

\*\*Expected:\*\* Returned to Login page; cannot re-enter inventory without credentials; session cleared.  

\*\*Priority:\*\* Medium



\### TC-009 – Session Cleared on Cookie Delete

\*\*Preconditions:\*\* Logged in; DevTools open.  

\*\*Steps:\*\*  

1\. Clear site data (cookies + local/session storage) in DevTools.  

2\. Refresh page.  

\*\*Expected:\*\* Redirected to Login; no authenticated user data displayed; cart badge hidden.  

\*\*Priority:\*\* Low



\### TC-010 – Inventory Images Load (Fast 3G)

\*\*Preconditions:\*\* Logged in on Inventory page; Network throttling set to Fast 3G in DevTools.  

\*\*Steps:\*\*  

1\. Reload the page under throttled network.  

2\. Observe loading behavior of six product images.  

\*\*Expected:\*\* All product thumbnails load within 10s; no broken image icons.  

\*\*Priority:\*\* Low

#### TC-010 – Inventory Product Images Load (3G) – EXECUTION

**Date/Time:** 2025-07-18 16:45 EDT  
**Browser:** Chrome 124.0.x (desktop) 
**Network Throttle:** 3G (built-in DevTools preset)  
**Cache:** Disabled (DevTools)  
**Service Worker:** Bypass ON  
**Procedure Notes:** Hard reload (Ctrl+Shift+R) → immediate full-page scroll → DOM-driven performance timing snippet (`responseEnd`).  
**Images Detected:** 6 / 6 (DOM images = 6, network-backed = 6)  

| Image Filename (base) | Finish (ms) | Duration (ms) | Notes |
|-----------------------|-------------|---------------|-------|
| bike-light-1200x1500.37c843b0.jpg | 13035 | 4489 |  |
| bolt-shirt-1200x1500.c2599ac5.jpg | 13602 | 5098 |  |
| red-onesie-1200x1500.2ec615b2.jpg | 13917 | 5424 |  |
| sauce-backpack-1200x1500.0a0b85a3.jpg | 14082 | 5536 |  |
| test.allthethings()-t-shirt-1200x1500.30dae4ef.jpg | 14782 | 6235 |  |
| sauce-pullover-1200x1500.51d7ffa9.jpg | 15293 | 6746 | **Slowest** |

**Max finish (responseEnd):** 15,293 ms  
**Threshold:** ≤ 10,000 ms  
**Result:** **FAIL**  

**Console Notes:** Only slow-network font fallback warnings + analytics 401 responses; no JS errors affecting image rendering.  
**Suspected Root Cause:** Large 1200×1500 JPEG thumbnails (no responsive `srcset` or modern formats) → high transfer times on 3G.  
**Next Action:** Defect *IMG-PERF-001* opened (optimize thumbnails: smaller derivative, WebP/AVIF, compression, `srcset`).  
**Evidence:** [Console timing screenshot](manual-evidence/screenshots/TC-010_console-timing_FAIL_20250718-1645.png) • (Raw console output saved as `manual-evidence/screenshots/TC-010_perf-output_FAIL_20250718-1645.txt`)  
**Notes:** Earlier runs invalid (only 5 images) due to below-the-fold image not requested before timing; resolved via immediate scroll + DOM/perf join approach.


\### TC-011 – Keyboard Tab Navigation Accessible

\*\*Preconditions:\*\* Logged in on Inventory page.  

\*\*Steps:\*\*  

1\. Press \*\*Tab\*\* repeatedly to move through page controls.  

2\. Use \*\*Space/Enter\*\* to activate first Add-to-Cart button.  

\*\*Expected:\*\* Focus indicator visible; tab order follows logical reading order; Add-to-Cart buttons reachable; no keyboard trap.  

\*\*Priority:\*\* Low

### TC-011 – Keyboard Accessibility (Tab Navigation)

**Executed:** 2025-07-19 23:05 EDT  
**Browser:** Chrome 125 (desktop)  
**Environment:** Windows 11, 100% zoom, no interfering extensions  
**Preconditions:** Logged in; inventory page at top; no modal overlays.  
**Steps:** Press `Tab` sequentially from top of page through footer; observe each focus movement. Press `Shift+Tab` to reverse order.  
**Expected:** Every focusable element appears exactly once in logical sequence with a visible focus indicator (outline/ring/underline change); no element gains “invisible” focus.  
**Actual:** Footer social icon link(s) receive focus but show **no visible focus indicator** (computed style shows `outline: none`). (Add any other elements if affected.)  
**Result:** **FAIL**  
**Evidence:** `manual-evidence/screenshots/TC-011_focus-indicator_FAIL_20250719-2305.png`  
**Defect:** `ACC-FOCUS-001` (open / to be opened)  
**Notes:** Likely global CSS rule removing default outline without a :focus-visible replacement. Retest after adding custom outline style.

\### TC-012 – Error Banner Can Be Dismissed

\*\*Preconditions:\*\* On Login page.  

\*\*Steps:\*\*  

1\. Attempt invalid login (blank fields or wrong password) to trigger error banner.  

2\. Click the \*\*X\*\* (close) icon on banner.  

\*\*Expected:\*\* Banner closes immediately; fields remain editable; no page reload.  

\*\*Priority:\*\* Low



\### TC-013 – Mobile add-to-cart (Android Chrome)

\*\*Preconditions:\*\* BrowserStack Android 12 + Chrome; on Login page.  

\*\*Steps:\*\*  

1\. Login as `standard\_user`.  

2\. Add any item to cart.  

3\. Open cart.  

\*\*Expected:\*\* Mobile layout renders correctly; cart badge increments; item present.



\### TC-014 – Lighthouse perf baseline

\*\*Preconditions:\*\* Chrome desktop; Lighthouse extension or CLI installed.  

\*\*Steps:\*\*  

1\. Open Inventory page (logged in).  

2\. Run Lighthouse Performance audit.  

\*\*Expected:\*\* Performance score ≥ 90 (record actual); attach JSON/HTML report.

### TC-014 – Lighthouse Performance Baseline

**Executed:** 2025‑07‑20 21:04 EDT  
| Page | Score | LCP | TBT | Result |
|------|-------|-----|-----|--------|
| Login | 97 | 0.9 s | 90 ms | PASS |
| Inventory | 73 | 1.1 s | **470 ms** | FAIL |

**Result:** **FAIL**  
**Defect ID:** PERF-LH-BASE-001  
**Evidence:** see screenshots & JSON in `manual-evidence`  
**Notes:** High Total Blocking Time (470 ms) pulled score below 80. Likely heavy JS bundle or long main‑thread tasks.

---

#### TC-015 – Automation Smoke Script (pytest)

**Objective:** Verify the Selenium + pytest scaffold can log in, add an item, and assert cart count via command line (`pytest -m smoke`).

**Preconditions:** Framework installed (pytest, selenium, webdriver-manager); ENV vars set (`URL=https://www.saucedemo.com/`, `USER=standard_user`, `PASS=secret_sauce`).

**Steps (automated):**
1. Run `pytest -m smoke -v` (or `pytest tests/test_smoke.py`).
2. Script logs in, adds *Sauce Labs Backpack* to cart, asserts cart badge = 1.
3. Driver quits.

**Expected:** Exit code 0 (all assertions pass) within 30 s.

**Result:** **PASSED** (Local Windows 11 run)  
**Duration:** 6.28 s (first run), 4.77 s (second run)  
**Date/Build:** 2025‑07‑24, commit `<hash>`  
**Evidence:** Pytest output screenshot(s) in `reports/screenshots/` or console log attached; optional HTML report `reports/smoke_report.html`.

**Notes:**  
- Headless mode still commented; enable for CI.  
- Next: add screenshot-on-fail hook & integrate into GitHub Actions pipeline.  
- Candidate for nightly smoke job.


