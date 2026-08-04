# Part 1: Debugging Flaky Test Code

## Flakiness Issues Identified

## 1. Missing Wait After Login

Problem:
The test clicks login and immediately checks the dashboard URL.

Root Cause:
Login is asynchronous. The application needs time to authenticate and redirect.

Solution:

```python
page.click("#login-btn")
page.wait_for_url("**/dashboard")

2. Dynamic Dashboard Loading
Problem:
The welcome message may not appear immediately.

Root Cause:
Dashboard data loads through API calls.

Solution:

expect(page.locator(".welcome-message")).to_be_visible()

3. Exact URL Validation
Problem:
The test checks the complete URL.

Root Cause:
URLs can contain parameters or different formats.

Solution:

expect(page).to_have_url(re.compile("dashboard"))

4. Project Data Loading Issue
Problem:
Project cards are checked before they load.

Root Cause:
Tenant data loads dynamically.

Solution:

Wait until project cards are visible before validation.

5. CI/CD Environment Differences
Problem:
Tests fail more often in CI.

Root Cause:
CI machines are slower and may use different browsers.

Solution:

Use explicit waits, stable selectors, and browser configuration.

Assumptions
Automation users are available.
2FA is disabled for test users.
Test data is stable.
Application supports browser automation.
