import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture(scope="session")
def playwright_instance():
    pw = sync_playwright().start()
    yield pw
    pw.stop()

@pytest.fixture(scope="function")
def page(playwright_instance: Playwright):
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()

@pytest.fixture(scope="function")
def main_login(page, MAIN_URL="your-app-url", USER="user", PASS="pass"):
    page.goto(MAIN_URL)
    page.locator("#username").fill(USER)  # Adjust selectors
    page.locator("#password").fill(PASS)
    page.locator("button[type=submit]").click()
    expect(page.locator("#dashboard")).to_be_visible()  # Verify login
    yield page  # Return logged-in page for plugin launch
