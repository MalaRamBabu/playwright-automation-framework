import pytest
from pages.home_page import HomePage


class TestHomePage:
    """
    Test Suite: Home Page
    Target: https://automationexercise.com
    """

    def test_home_page_loads_successfully(self, page):
        """TC-001: Verify home page loads and URL is correct"""
        home = HomePage(page)
        home.open()
        assert home.is_home_page(), "Home page URL is incorrect"

    def test_home_page_logo_visible(self, page):
        """TC-002: Verify website logo is visible on home page"""
        home = HomePage(page)
        home.open()
        assert home.is_logo_visible(), "Website logo is not visible"

    def test_home_page_title(self, page):
        """TC-003: Verify home page has correct title"""
        home = HomePage(page)
        home.open()
        title = home.get_title()
        assert "Automation Exercise" in title, f"Unexpected title: {title}"

    def test_navigate_to_login_from_home(self, page):
        """TC-004: Verify clicking Signup/Login navigates to login page"""
        home = HomePage(page)
        home.open()
        home.go_to_login()
        assert "/login" in home.get_url(), "Did not navigate to login page"

    def test_navigate_to_products_from_home(self, page):
        """TC-005: Verify clicking Products navigates to products page"""
        home = HomePage(page)
        home.open()
        home.go_to_products()
        assert "/products" in home.get_url(), "Did not navigate to products page"

    def test_navigate_to_cart_from_home(self, page):
        """TC-006: Verify clicking Cart navigates to cart page"""
        home = HomePage(page)
        home.open()
        home.go_to_cart()
        assert "view_cart" in home.get_url(), "Did not navigate to cart page"
