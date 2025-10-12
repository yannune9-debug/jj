import os
from playwright.sync_api import Page, expect
 
class BasePage:
    def __init__(self, page: Page):
        self.page = page
        # Read BASE_URL after dotenv has loaded
        self.base_url = os.getenv("BASE_URL")
        if not self.base_url:
            raise ValueError("BASE_URL is not set in .env file!")
 
    def navigate(self, url: str = None):
        """Navigate to given URL or fallback to BASE_URL from .env"""
        target_url = url if url else self.base_url
        print(f"Navigating to: {target_url}")
        self.page.goto(target_url)
 
    def take_screenshot(self, path="scr.png"):
        """Take screenshot and save to file"""
        self.page.screenshot(path=path)
 
    def wait_for_url(self, url: str):
        """Wait until page has expected URL"""
        expect(self.page).to_have_url(url)