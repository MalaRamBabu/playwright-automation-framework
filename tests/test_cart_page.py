import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage


class TestCartPage:
    """
    Test Suite: Cart Page
    Target: https://automationexercise.com/view_cart
    """

    def test_cart_page_loads(self, page):
        """TC-024: Verify cart page loads correctly"""
        cart = CartPage(page)
        cart.open()
        assert cart.is_cart_page(), "Not on cart page"

    def test_cart_page_title(self, page):
        """TC-025: Verify cart page has correct title"""
        cart = CartPage(page)
        cart.open()
        title = cart.get_title()
        assert "Automation Exercise" in title, f"Unexpected title: {title}"

    def test_empty_cart_navigates_correctly(self, page):
        """TC-026: Verify navigating to cart when empty works"""
        home = HomePage(page)
        home.open()
        home.go_to_cart()
        cart = CartPage(page)
        assert cart.is_cart_page(), "Did not navigate to cart page"

    def test_cart_url_is_correct(self, page):
        """TC-027: Verify cart page URL contains view_cart"""
        cart = CartPage(page)
        cart.open()
        assert "view_cart" in cart.get_url(), "Cart URL is incorrect"

    def test_navigate_to_cart_from_home(self, page):
        """TC-028: Verify cart is accessible from home page nav"""
        home = HomePage(page)
        home.open()
        home.go_to_cart()
        cart = CartPage(page)
        assert cart.is_cart_page(), "Cart not accessible from home"
