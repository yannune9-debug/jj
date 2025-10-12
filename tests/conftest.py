# conftest.py
import pytest
import os

# -------------------------------
# 📸 Take screenshot on test failure
# -------------------------------
@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(page, request):
    """Automatically take a screenshot if a test using Playwright's 'page' fails."""
    yield  # Let the test run first
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}.png")

        try:
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"📸 Screenshot saved to: {screenshot_path}")

            # Attach screenshot to Allure report (if installed)
            try:
                import allure
                allure.attach.file(
                    screenshot_path,
                    name=request.node.name,
                    attachment_type=allure.attachment_type.PNG
                )
            except ImportError:
                pass  # Allure not installed, ignore gracefully

        except Exception as e:
            print(f"⚠️ Failed to capture screenshot: {e}")


# -------------------------------
# 🧩 Hook to track test result status
# -------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make test results available to fixtures (e.g., to detect test failure)."""
    outcome = yield
    result = outcome.get_result()
    setattr(item, "rep_" + result.when, result)
