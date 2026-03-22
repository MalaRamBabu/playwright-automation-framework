class BasePage:
    """
    Base class for all page objects.
    Contains common reusable methods used across all pages.
    """

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        """Navigate to a specific URL"""
        self.page.goto(url)

    def click(self, locator):
        """Click an element"""
        self.page.locator(locator).click()

    def fill(self, locator, text):
        """Fill text into an input field"""
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        """Get visible text of an element"""
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator):
        """Check if an element is visible"""
        return self.page.locator(locator).is_visible()

    def wait_for(self, locator, timeout=5000):
        """Wait for an element to be visible"""
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    def get_title(self):
        """Get the current page title"""
        return self.page.title()

    def get_url(self):
        """Get the current page URL"""
        return self.page.url
