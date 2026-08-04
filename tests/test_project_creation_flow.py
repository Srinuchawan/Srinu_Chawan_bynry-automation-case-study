import requests
import uuid
from playwright.sync_api import sync_playwright, expect


# Application details
API_URL = "https://api.workflowpro.com"

COMPANY1 = "company1"
COMPANY2 = "company2"


# Step 1: Create project using API
def create_project():

    project_name = "Test_Project_" + str(uuid.uuid4())

    data = {
        "name": project_name,
        "description": "Created by automation test",
        "team_members": [
            "user1"
        ]
    }

    headers = {
        "Authorization": "Bearer test_token",
        "X-Tenant-ID": COMPANY1
    }


    response = requests.post(
        API_URL + "/api/v1/projects",
        json=data,
        headers=headers
    )


    # Check API response
    assert response.status_code == 200


    project = response.json()

    assert project["name"] == project_name

    return project_name



# Login function
def login(page, tenant):

    page.goto(
        f"https://{tenant}.workflowpro.com/login"
    )


    page.fill(
        "#email",
        "automation@test.com"
    )


    page.fill(
        "#password",
        "password123"
    )


    page.click("#login-btn")


    page.wait_for_url("**/dashboard")



# Main Integration Test
def test_project_creation_flow():


    # 1. Create project through API

    project_name = create_project()



    with sync_playwright() as p:


        browser = p.chromium.launch(
            headless=True
        )


        page = browser.new_page()



        # 2. Verify project in Company1 UI

        login(
            page,
            COMPANY1
        )


        page.fill(
            "#project-search",
            project_name
        )


        expect(
            page.locator(".project-card")
        ).to_be_visible()


        assert project_name in page.text_content(
            ".project-card"
        )



        # 3. Verify tenant isolation

        login(
            page,
            COMPANY2
        )


        page.fill(
            "#project-search",
            project_name
        )


        projects = page.locator(
            ".project-card"
        ).all_text_contents()


        assert project_name not in projects



        browser.close()



# BrowserStack mobile testing example

def test_mobile_testing_example():


    mobile_device = {

        "device": "iPhone 14",

        "browser": "Safari",

        "platform": "iOS"

    }


    # In real project:
    # This configuration will be connected
    # with BrowserStack remote browser.


    assert mobile_device["device"] == "iPhone 14"
    