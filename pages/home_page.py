from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page Object for Automation Exercise Home Page
    URL: https://automationexercise.com
    """

    URL = "https://automationexercise.com"

    # Locators
    LOGO             = "img[alt='Website for automation practice']"
    SIGNUP_LOGIN_BTN = "a[href='/login']"
    PRODUCTS_BTN     = "a[href='/products']"
    CART_BTN         = "a[href='/view_cart']"
    HOME_BTN         = "a[href='/']"
    CONSENT_BTN      = "p.fc-button-label"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        """Open the home page"""
        self.navigate(self.URL)
        # Handle cookie consent popup if it appears
        try:
            if self.page.locator(self.CONSENT_BTN).is_visible():
                self.page.locator(self.CONSENT_BTN).first.click()
        except Exception:
            pass

    def go_to_login(self):
        """Click Signup / Login button"""
        self.click(self.SIGNUP_LOGIN_BTN)

    def go_to_products(self):
        """Click All Products button"""
        self.click(self.PRODUCTS_BTN)

    def go_to_cart(self):
        """Click Cart button"""
        self.click(self.CART_BTN)

    def is_logo_visible(self):
        """Check if homepage logo is visible"""
        return self.is_visible(self.LOGO)

    def is_home_page(self):
        """Verify we are on the home page"""
        return "automationexercise.com" in self.get_url()
