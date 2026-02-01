from playwright.sync_api import sync_playwright, expect



class LoginPage():
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Submit").click()

def test_login_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for CI
        context = browser.new_context()
        page = context.new_page()

        # Navigate to your login URL (replace with actual URL)
        page.goto("https://practicetestautomation.com/practice-test-login/")

        # Fill username/email (adapt locator to your form, e.g., by label or placeholder)
        page.get_by_label("Username").fill("student")  # Or page.locator("#username")

        # Fill password
        page.get_by_label("Password").fill("Password123")  # Or page.locator("#password")

        # Click sign-in button (adapt to your button's role/text)
        page.get_by_role("button", name="Submit").click()

        # Optional: Wait and assert successful login (e.g., check for dashboard element)
        expect(page.get_by_text("Logged In Successfully")).to_be_visible()

        browser.close()

if __name__ == "__main__":
    test_login_app()
