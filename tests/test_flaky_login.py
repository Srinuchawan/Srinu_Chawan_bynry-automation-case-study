from playwright.sync_api import sync_playwright, expect


def test_user_login():

    with sync_playwright() as p:

        # Open browser
        browser = p.chromium.launch(headless=True)
        
        page = browser.new_page()

        page.goto(
            "https://app.workflowpro.com/login"
        )


        page.fill(
            "#email",
            "admin@company1.com"
        )

        page.fill(
            "#password",
            "password123"
        )



        page.click("#login-btn")

        page.wait_for_url(
            "**/dashboard"
        )

        expect(
            page.locator(".welcome-message")
        ).to_be_visible()

        browser.close()
