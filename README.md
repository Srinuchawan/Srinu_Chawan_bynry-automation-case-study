# Bynry QA Automation Case Study Solution

## Overview

This repository contains my QA Automation Engineering case study solution.

The project demonstrates:
- Playwright automation testing
- Flaky test analysis
- Test reliability improvements
- CI/CD testing considerations

## Tools Used

- Python
- Pytest
- Playwright

## Setup Instructions

Install dependencies:

pip install -r requirements.txt


Install Playwright browsers:


playwright install


## Run Tests

Execute:


pytest tests/


## Project Structure


docs/ - Test documentation
tests/ - Automation scripts
test_data/ - Test data files
reports/ - Test execution reports

# QA Automation Case Study Summary

## Part 1: Flaky Test Debugging

Implemented analysis and fixes for unstable Playwright login tests.

Improvements:
- Added proper waits
- Improved dynamic element handling
- Added better URL validation
- Considered CI/CD issues


## Part 2: Automation Framework Design

Designed a scalable framework supporting:

- Web automation
- Mobile testing
- API testing
- Multiple tenants
- Multiple user roles
- BrowserStack execution
- CI/CD integration


## Part 3: API + UI Integration

Implemented a complete project creation validation flow:

1. Create project using API
2. Verify project in web UI
3. Validate mobile compatibility
4. Check tenant isolation


## Future Improvements

- Add real CI/CD pipeline
- Add automated reports
- Add screenshots/videos on failure
- Add test data cleanup

