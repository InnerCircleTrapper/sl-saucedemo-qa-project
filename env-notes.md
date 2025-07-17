\# Environment Notes



\## 1. Local Desktop



| Component | Version |

|-----------|---------|

| OS        | Windows 11 Pro 22H2 (build 22635.385) |

| Chrome    | \*\*125.0.6422.0\*\* (Official Build, 64‑bit) |

| Firefox   | 127.0 (64‑bit) |



\## 2. Remote Mobile (BrowserStack)



| Device               | OS Version | Browser |

|----------------------|-----------|---------|

| Samsung Galaxy S22   | Android 12 | Chrome 125 |



\## 3. Tooling



\* Python 3.11.4 (virtualenv: `/envs/sauce`)

\* Selenium 4.20.0  

\* pytest 8.0.0  

\* Selenium IDE Chrome Ext 3.141  



\## 4. Test Data



| User             | Password       | Purpose      |

|------------------|---------------|--------------|

| `standard\_user`  | `secret\_sauce`| Happy path   |

| `locked\_out\_user`| `secret\_sauce`| Negative path|



\## 5. Network \& Settings



\* Chrome DevTools throttling: \*\*Fast 3G\*\*  

\* Chrome flag: `--disable-notifications` to suppress pop‑ups



