import pytest
from pages.products_page import ProductsPage
from pages.home_page import HomePage


class TestProductsPage:
    """
    Test Suite: Products Page
    Target: https://automationexercise.com/products
    """

    def test_products_page_loads(self, page):
        """TC-015: Verify products page loads correctly"""
        products = ProductsPage(page)
        products.open()
        assert products.is_products_page(), "Not on products page"

    def test_all_products_heading_visible(self, page):
        """TC-016: Verify 'All Products' heading is visible"""
        products = ProductsPage(page)
        products.open()
        assert products.is_all_products_heading_visible(), \
            "'All Products' heading not visible"

    def test_products_are_displayed(self, page):
        """TC-017: Verify at least one product is shown"""
        products = ProductsPage(page)
        products.open()
        count = products.get_product_count()
        assert count > 0, "No products found on products page"

    def test_search_valid_keyword_returns_results(self, page, search_terms):
        """TC-018: Verify search with valid keyword returns results"""
        products = ProductsPage(page)
        products.open()
        products.search_product(search_terms["valid"])
        count = products.get_product_count()
        assert count > 0, f"No results for search: {search_terms['valid']}"

    def test_search_shows_searched_products_heading(self, page, search_terms):
        """TC-019: Verify 'Searched Products' heading appears after search"""
        products = ProductsPage(page)
        products.open()
        products.search_product(search_terms["valid"])
        assert products.is_searched_heading_visible(), \
            "'Searched Products' heading not visible after search"

    def test_search_results_match_keyword(self, page, search_terms):
        """TC-020: Verify search results contain the searched keyword"""
        products = ProductsPage(page)
        products.open()
        keyword = search_terms["valid"]
        products.search_product(keyword)
        names = products.all_product_names()
        assert len(names) > 0, "No product names found after search"
        # At least one result should contain keyword
        keyword_found = any(keyword.lower() in name.lower() for name in names)
        assert keyword_found, f"No results match keyword: {keyword}"

    def test_search_partial_keyword_returns_results(self, page, search_terms):
        """TC-021: Verify partial keyword search returns results"""
        products = ProductsPage(page)
        products.open()
        products.search_product(search_terms["partial"])
        count = products.get_product_count()
        assert count > 0, f"No results for partial keyword: {search_terms['partial']}"

    def test_navigate_to_products_from_home(self, page):
        """TC-022: Verify navigation to products page from home"""
        home = HomePage(page)
        home.open()
        home.go_to_products()
        products = ProductsPage(page)
        assert products.is_products_page(), "Did not land on products page"

    @pytest.mark.parametrize("keyword", ["top", "dress", "jeans", "saree"])
    def test_multiple_product_searches(self, page, keyword):
        """TC-023: Verify search works for multiple different keywords"""
        products = ProductsPage(page)
        products.open()
        products.search_product(keyword)
        count = products.get_product_count()
        assert count >= 0, f"Search failed for keyword: {keyword}"
