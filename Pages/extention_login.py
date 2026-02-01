import time
from playwright.sync_api import sync_playwright

def login_to_extension(extension_path, login_url, username, password):
    # Launch Chromium with the extension loaded
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                f"--disable-extensions-except={extension_path}",
                f"--load-extensions={extension_path}",
            ]
        )
        
        # Access the extension's login page directly
        # You'll need to find the specific URL for your extension's login page
        # This is often something like "chrome-extension://<extension_id>/login.html"
        # The extension ID will be generated when you run the script.
        # You can print the page.url after the first navigation to find it.
        page = browser.new_page()
        page.goto(login_url) 
        print(f"Navigated to: {page.url}")

        # --- Login Actions ---
        # Replace these locators with the actual selectors from your extension's page
        
        # Fill in the username/email field
        page.locator('input[name="username"]').fill(username)
        print("Entered username")
        
        # Fill in the password field
        page.locator('input[name="password"]').fill(password)
        print("Entered password")

        # Click the login button
        page.locator('button[type="submit"]').click()
        print("Clicked login button")

        # Wait for the login process to complete (e.g., page navigation, element appearance)
        # Add appropriate wait conditions here
        page.wait_for_url("**/dashboard.html") # Example: wait for dashboard page

        print("Successfully logged in to the extension.")
        
        # Keep the browser open for a few seconds to visually verify
        time.sleep(5) 
        
        browser.close()

# --- Example Usage ---
# Replace with your actual extension details
EXTENSION_PATH = "/path/to/your/unpacked/extension/folder"
# The exact login URL will depend on your extension's ID (which changes)
# For testing, you can open the extension manually to get the ID, e.g.,
# "chrome-extension://abcdef1234567890abcdef1234567890/login.html"
LOGIN_PAGE_URL = "chrome-extension://<your_extension_id>/login.html" 
USERNAME = "testuser"
PASSWORD = "testpassword"

# Call the function
# login_to_extension(EXTENSION_PATH, LOGIN_PAGE_URL, USERNAME, PASSWORD)
