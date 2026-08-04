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


bynry-qa-automation-case-study

├── docs
│ ├── Part1_Flaky_Test_Analysis.md
│ ├── Framework_Design.md
│ └── Part3_API_UI_Integration.md
│
├── tests
│ ├── test_flaky_login.py
│ └── test_project_creation.py
│
├── test_data
│ └── users.json
│
├── reports
│ └── test_execution_report.md
│
├── requirements.txt
└── README.md


## Case Study Coverage

### Part 1: Flaky Test Debugging

- Identified flaky test causes
- Added proper waits
- Improved CI/CD reliability


### Part 2: Framework Design

Designed a scalable automation framework supporting:

- Web testing
- API testing
- Mobile testing
- Multiple tenants
- Different user roles


### Part 3: API + UI Integration

Implemented approach for:

- Creating projects through API
- Validating projects in UI
- Mobile validation
- Tenant isolation testing
