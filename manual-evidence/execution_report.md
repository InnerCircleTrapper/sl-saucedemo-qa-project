\# SauceDemo Manual Test Execution Report

\_Date:\_ YYYY-MM-DD  

\_Build / URL:\_ https://www.saucedemo.com  

\_Tester:\_ Steve Louis (SL)  

\_Environment ref:\_ See \[`env-notes.md`](../env-notes.md)



\## Legend

\*\*P\*\* = Pass | \*\*F\*\* = Fail | \*\*B\*\* = Blocked (env / data) | \*\*N/R\*\* = Not Run  

\_Defect ID\_ column links to GitHub Issue numbers (e.g., `#3`).  



\## Run Summary (update after execution)



| Total Cases | Passed | Failed | Blocked | Not Run | Pass % |

|-------------|--------|--------|---------|---------|--------|

| 12 | 0 | 0 | 0 | 12 | 0% |



\## Detailed Results



| TC ID | Title | Priority | Result | Defect ID | Notes |

|------|-------|----------|--------|-----------|-------|

| TC-001 | Valid Login (standard\_user) | High | PASS |  |  |

| TC-002 | Locked-Out User Blocked on Login | High | PASS |  |  |

| TC-003 | Add Single Item to Cart | High | PASS |  |  |

| TC-004 | Remove Item from Cart | Medium | PASS |  |  |

| TC-005 | Complete Checkout Happy Path | High | PASS |  |  |

| TC-006 | Checkout Missing Zip Validation | Medium | PASS |  |  |

| TC-007 | Sort Products Price Low→High | Low | PASS |  |  |

| TC-008 | Logout Ends Session | Medium | PASS |  |  |

| TC-009 | Session Cleared on Cookie Delete | Low | PASS |  |  |

| TC-010 | Inventory Images Load (Fast 3G) | Low | N/R |  |  |

| TC-011 | Keyboard Tab Navigation Accessible | Low | N/R |  |  |

| TC-012 | Error Banner Can Be Dismissed | Low | N/R |  |  |



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
**Browser:** Brave/Chrome <version> (desktop)  
**Network Throttle:** 3G (built-in)  
**Cache:** Disabled (DevTools)  
**Service Worker:** Bypass ON  
**Procedure Notes:** Hard reload (Ctrl+Shift+R) → immediate full-page scroll → DOM-driven performance timing snippet (responseEnd).  
**Images Detected:** 6 / 6 (DOM images = 6, network-backed = 6)  

| Image (file) | Finish ms | Duration ms | Notes |
|--------------|-----------|-------------|-------|
| bike-light … | 13035 | 4489 |  |
| bolt-shirt … | 13602 | 5098 |  |
| red-onesie … | 13917 | 5424 |  |
| sauce-backpack … | 14082 | 5536 |  |
| test-allthethings … | 14782 | 6235 |  |
| sauce-pullover (fleece) … | 15293 | 6746 | **Slowest** |

**Max finish (responseEnd):** 15,293 ms  
**Threshold:** ≤ 10,000 ms  
**Result:** **FAIL**  

**Console Notes:** Only slow-network font fallback warnings + analytics 401; no JS errors affecting images.  
**Root Cause (suspected):** Large 1200×1500 JPEG thumbnails (no smaller responsive variant or modern format); all full-res images fetched early on slow network → exceeds 10 s budget.  
**Next Action:** Defect *IMG-PERF-001* opened (optimize product thumbnails, consider srcset/WebP/AVIF, compression).  
**Evidence:** `/artifacts/TC-010/console_timing_screenshot.png`, `/artifacts/TC-010/perf_snippet_output.txt` (maxFinish 15293).  
**Notes:** Earlier attempts invalid (only 5 images captured) due to late scroll; resolved with DOM-driven enumeration.



\### TC-011 – Keyboard Tab Navigation Accessible

\*\*Preconditions:\*\* Logged in on Inventory page.  

\*\*Steps:\*\*  

1\. Press \*\*Tab\*\* repeatedly to move through page controls.  

2\. Use \*\*Space/Enter\*\* to activate first Add-to-Cart button.  

\*\*Expected:\*\* Focus indicator visible; tab order follows logical reading order; Add-to-Cart buttons reachable; no keyboard trap.  

\*\*Priority:\*\* Low



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



