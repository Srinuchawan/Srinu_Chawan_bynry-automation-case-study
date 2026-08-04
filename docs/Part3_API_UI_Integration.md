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

Company1:

Project visible ✅


Company2:

Project should not appear ✅


## Assumptions

- API authentication token is available.
- Test users already exist.
- BrowserStack credentials are configured.
- Cleanup API exists after test execution.
- Test environment supports automation.
