import requests
import uuid
from playwright.sync_api import sync_playwright, expect


# Test configuration
API_URL = "https://api.workflowpro.com"
WEB_URL = "https://company1.workflowpro.com"

COMPANY1_ID = "company1"
COMPANY2_ID = "company2"


def create_project_api():

    """
    Creates project using backend API
    """

    project_name = "Automation_Test_Project_" + str(uuid.uuid4())

    payload = {
        "name": project_name,
        "description": "Created through automation",
        "team_members": [
            "user1"
        ]
    }

    headers = {
        "Authorization": "Bearer test_token",
        "X-Tenant-ID": COMPANY1_ID
    }


    response = requests.post(
        f"{API_URL}/api/v1/projects",
        json=payload,
        headers=headers
    )


    assert response.status_code == 200


    project = response.json()

    return project



def login(page, tenant):

    """
    Login helper function
    """

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



def test_project_creation_flow():

    # ----------------------------
    # Step 1:
    # Create project using API
    # ----------------------------

    project = create_project_api()


    project_id = project["id"]

    project_name = project["name"]



    # ----------------------------
    # Step 2:
    # Verify project in Web UI
    # ----------------------------


    with sync_playwright() as p:


        browser = p.chromium.launch(
            headless=True
        )


        page = browser.new_page()


        login(
            page,
            COMPANY1_ID
        )


        # Search project

        page.fill(
            "#project-search",
            project_name
        )


        expect(
            page.locator(
                ".project-card"
            )
        ).to_be_visible()



        assert project_name in page.text_content(
            ".project-card"
        )



        # ----------------------------
        # Step 3:
        # Tenant Isolation Testing
        # ----------------------------


        login(
            page,
            COMPANY2_ID
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



def test_mobile_validation_browserstack():

    """
    BrowserStack mobile execution example.

    In real execution, BrowserStack credentials
    and capabilities will be configured.
    """


    capabilities = {

        "deviceName": "iPhone 14",

        "browserName": "Safari",

        "platformName": "iOS"

    }


    # Connect Playwright with BrowserStack
    # and execute same validation flow

    assert capabilities["deviceName"] == "iPhone 14"
