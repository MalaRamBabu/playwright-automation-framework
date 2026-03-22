import pytest
from playwright.sync_api import sync_playwright


# ── Browser Configuration ─────────────────────────────────────────────────────
def pytest_addoption(parser):
    parser.addoption(
        "--browser-type",
        action="store",
        default="chromium",
        help="Browser to run tests on: chromium | firefox | webkit"
    )
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="Run in headless mode: true | false"
    )


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser-type")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless").lower() == "true"


# ── Playwright Browser Fixtures ───────────────────────────────────────────────
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, browser_type, headless):
    """Launch browser once per session"""
    browsers = {
        "chromium": playwright_instance.chromium,
        "firefox":  playwright_instance.firefox,
        "webkit":   playwright_instance.webkit,
    }
    launcher = browsers.get(browser_type, playwright_instance.chromium)
    browser = launcher.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Create a fresh browser context and page for each test"""
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    yield page
    context.close()


# ── Test Data ─────────────────────────────────────────────────────────────────
@pytest.fixture
def valid_user():
    return {
        "email":    "testuser@example.com",
        "password": "Test@12345"
    }


@pytest.fixture
def invalid_user():
    return {
        "email":    "wrong@example.com",
        "password": "WrongPass"
    }


@pytest.fixture
def search_terms():
    return {
        "valid":   "dress",
        "partial": "top",
        "invalid": "xyznotexist999"
    }
