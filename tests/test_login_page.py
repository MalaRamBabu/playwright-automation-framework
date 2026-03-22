import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLoginPage:
    """
    Test Suite: Login & Signup Page
    Target: https://automationexercise.com/login
    """

    def test_login_page_loads(self, page):
        """TC-007: Verify login page loads correctly"""
        login = LoginPage(page)
        login.open()
        assert login.is_login_page(), "Not on login page"

    def test_login_page_title(self, page):
        """TC-008: Verify login page has correct title"""
        login = LoginPage(page)
        login.open()
        title = login.get_title()
        assert "Automation Exercise" in title, f"Unexpected title: {title}"

    def test_invalid_login_shows_error(self, page, invalid_user):
        """TC-009: Verify error message shown for invalid credentials"""
        login = LoginPage(page)
        login.open()
        login.login(invalid_user["email"], invalid_user["password"])
	page.wait_for_timeout(2000)
        assert login.is_login_error_visible(), "Error message not shown for invalid login"

    def test_invalid_login_error_message_text(self, page, invalid_user):
        """TC-010: Verify exact error message text for invalid login"""
        login = LoginPage(page)
        login.open()
        login.login(invalid_user["email"], invalid_user["password"])
        error_text = login.get_login_error()
        assert "incorrect" in error_text.lower(), f"Unexpected error: {error_text}"

    def test_empty_email_stays_on_login(self, page):
        """TC-011: Verify empty email field prevents login"""
        login = LoginPage(page)
        login.open()
        login.login("", "somepassword")
        assert login.is_login_page(), "Should stay on login page with empty email"

    def test_empty_password_stays_on_login(self, page):
        """TC-012: Verify empty password field prevents login"""
        login = LoginPage(page)
        login.open()
        login.login("test@example.com", "")
        assert login.is_login_page(), "Should stay on login page with empty password"

    def test_signup_with_existing_email_shows_error(self, page):
        """TC-013: Verify error shown when signing up with existing email"""
        login = LoginPage(page)
        login.open()
        # Using a known registered email on automationexercise
        login.signup("Test User", "test@test.com")
        assert login.is_signup_error_visible(), "Error not shown for duplicate email"

    @pytest.mark.parametrize("email,password", [
        ("notanemail", "password123"),
        ("@nodomain.com", "password123"),
        ("spaces in@email.com", "password123"),
    ])
    def test_invalid_email_formats(self, page, email, password):
        """TC-014: Verify invalid email formats are handled"""
        login = LoginPage(page)
        login.open()
        login.login(email, password)
        # Should either show error or stay on login page
        current_url = login.get_url()
        assert "/login" in current_url or login.is_login_error_visible(), \
            f"Invalid email '{email}' should not pass validation"
