from pages.base_page import BasePage


class ProductsPage(BasePage):
    """
    Page Object for Products Page
    URL: https://automationexercise.com/products
    """

    URL = "https://automationexercise.com/products"

    # Locators
    PRODUCTS_HEADING  = "h2.title.text-center"
    SEARCH_INPUT      = "input#search_product"
    SEARCH_BUTTON     = "button#submit_search"
    PRODUCT_CARDS     = ".productinfo"
    PRODUCT_NAMES     = ".productinfo p"
    NO_RESULTS        = "div.productinfo:has-text('No products found')"
    FIRST_VIEW_BTN    = ".choose a"
    ALL_PRODUCTS_TEXT = "h2:has-text('All Products')"
    SEARCHED_HEADING  = "h2:has-text('Searched Products')"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        """Open the products page"""
        self.navigate(self.URL)

    def search_product(self, keyword):
        """Search for a product by keyword"""
        self.fill(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)

    def get_product_count(self):
        """Get the number of product cards visible"""
        return self.page.locator(self.PRODUCT_CARDS).count()

    def get_first_product_name(self):
        """Get the name of the first product"""
        return self.page.locator(self.PRODUCT_NAMES).first.inner_text()

    def all_product_names(self):
        """Get list of all visible product names"""
        return self.page.locator(self.PRODUCT_NAMES).all_inner_texts()

    def is_all_products_heading_visible(self):
        """Verify 'All Products' heading is visible"""
        return self.is_visible(self.ALL_PRODUCTS_TEXT)

    def is_searched_heading_visible(self):
        """Verify 'Searched Products' heading shows after search"""
        return self.is_visible(self.SEARCHED_HEADING)

    def is_products_page(self):
        """Verify we are on the products page"""
        return "/products" in self.get_url()
