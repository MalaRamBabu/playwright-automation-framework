from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for Login and Signup Page
    URL: https://automationexercise.com/login
    """

    URL = "https://automationexercise.com/login"

    # Login locators
    LOGIN_EMAIL    = "input[data-qa='login-email']"
    LOGIN_PASSWORD = "input[data-qa='login-password']"
    LOGIN_BUTTON   = "button[data-qa='login-button']"
    LOGIN_ERROR    = "p:has-text('Your email or password is incorrect!')"
    LOGIN_HEADING  = "h2:has-text('Login to your account')"

    # Signup locators
    SIGNUP_NAME    = "input[data-qa='signup-name']"
    SIGNUP_EMAIL   = "input[data-qa='signup-email']"
    SIGNUP_BUTTON  = "button[data-qa='signup-button']"
    SIGNUP_ERROR   = "p:has-text('Email Address already exist!')"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        """Open the login page"""
        self.navigate(self.URL)

    def login(self, email, password):
        """Perform login with given credentials"""
        self.fill(self.LOGIN_EMAIL, email)
        self.fill(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_login_error(self):
        """Get login error message text"""
        return self.get_text(self.LOGIN_ERROR)

    def is_login_error_visible(self):
        """Check if login error message is shown"""
        return self.is_visible(self.LOGIN_ERROR)

    def signup(self, name, email):
        """Fill and submit signup form"""
        self.fill(self.SIGNUP_NAME, name)
        self.fill(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)

    def is_signup_error_visible(self):
        """Check if signup email-already-exists error is shown"""
        return self.is_visible(self.SIGNUP_ERROR)

    def is_login_page(self):
        """Verify we are on the login page"""
        return "/login" in self.get_url()
