from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page Object for Cart Page
    URL: https://automationexercise.com/view_cart
    """

    URL = "https://automationexercise.com/view_cart"

    # Locators
    CART_ITEMS         = "tr.cart_menu"
    CART_ITEM_NAMES    = ".cart_description h4 a"
    CART_PRICES        = ".cart_price p"
    CART_QUANTITIES    = ".cart_quantity button"
    REMOVE_BUTTONS     = "a.cart_quantity_delete"
    EMPTY_CART_MSG     = "b:has-text('Cart is empty!')"
    PROCEED_CHECKOUT   = "a.btn.btn-default.check_out"
    CART_HEADING       = "li.active:has-text('Shopping Cart')"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        """Open the cart page"""
        self.navigate(self.URL)

    def get_cart_item_count(self):
        """Get number of items in cart"""
        return self.page.locator(self.CART_ITEM_NAMES).count()

    def get_cart_item_names(self):
        """Get list of all item names in cart"""
        return self.page.locator(self.CART_ITEM_NAMES).all_inner_texts()

    def get_first_item_name(self):
        """Get name of first item in cart"""
        return self.page.locator(self.CART_ITEM_NAMES).first.inner_text()

    def remove_first_item(self):
        """Remove the first item from cart"""
        self.page.locator(self.REMOVE_BUTTONS).first.click()

    def is_cart_empty(self):
        """Check if cart is empty"""
        return self.is_visible(self.EMPTY_CART_MSG)

    def is_cart_page(self):
        """Verify we are on the cart page"""
        return "view_cart" in self.get_url()

    def proceed_to_checkout(self):
        """Click proceed to checkout"""
        self.click(self.PROCEED_CHECKOUT)
