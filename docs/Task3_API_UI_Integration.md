# Part 3: API + UI Integration Test

## Testing Approach

The test validates the complete project creation workflow.

Flow:

API

↓

Create Project

↓

Store Project ID

↓

Login through Web UI

↓

Verify Project Display

↓

Validate Mobile Access

↓

Verify Tenant Isolation


## API Testing

The project is created using:

POST /api/v1/projects


Headers:

Authorization:
Bearer token

X-Tenant-ID:
company1


## UI Validation

After API creation:

- Login into Company1 tenant
- Search project
- Verify project name appears


## Mobile Validation

The same workflow should execute on BrowserStack mobile devices:

Examples:

- iPhone
- Android devices


## Tenant Isolation

Security validation:

Company1 tenant:

Project should be visible ✅


Company2 tenant:

Project should not be visible ✅



## Assumptions

- API authentication token is available.
- Test users already exist.
- BrowserStack credentials are configured.
- Cleanup API exists after test execution.
- Test environment supports automation.

---

# Integration Test Implementation

The automation flow combines API testing and UI validation.

## Step 1: Create Project Using API

The project is created using the backend API.

Example:

```python
response = requests.post(
    "/api/v1/projects",
    headers={
        "Authorization": "Bearer token",
        "X-Tenant-ID": "company1"
    },
    json={
        "name": "Automation Test Project",
        "description": "Created through API",
        "team_members": ["user1"]
    }
)

assert response.status_code == 200
```

The created project ID and name are stored for UI validation.

---

## Step 2: Verify Project Through Web UI

After API creation:

1. Login into Company1 tenant.
2. Navigate to project page.
3. Search the created project.
4. Verify project details.

Example:

```python
page.goto("https://company1.workflowpro.com")

page.fill("#search", project_name)

expect(
    page.locator(".project-card")
).to_be_visible()
```

---

## Step 3: Mobile Validation Using BrowserStack

The same test flow should execute on mobile devices.

Example BrowserStack capabilities:

```python
capabilities = {
    "deviceName": "iPhone 14",
    "browserName": "Safari",
    "platformName": "iOS"
}
```

Supported devices:

- iOS devices
- Android devices

---

## Step 4: Tenant Isolation Validation

Security validation ensures data separation between companies.

Test:

Company1 user:

```
Project should be visible
```

Company2 user:

```
Project should not be visible
```

This prevents cross-tenant data exposure.

---

# Edge Cases Considered

## Network Failure

- Add API retry mechanism.
- Capture logs when requests fail.

## Slow Loading

- Use Playwright explicit waits.
- Avoid fixed sleep statements.

## Mobile Responsiveness

- Validate UI elements across different screen sizes.

## Test Data Cleanup

After execution:

- Delete created project using cleanup API.
- Maintain clean test environment.

---

# Testing Strategy Summary

The integration test validates:

✅ Backend project creation  
✅ Frontend project visibility  
✅ Mobile accessibility  
✅ Tenant security isolation  
✅ Error handling scenarios  
