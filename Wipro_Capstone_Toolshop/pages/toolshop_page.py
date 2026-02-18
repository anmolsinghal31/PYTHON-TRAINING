import time
from pages.common_ops import CommonOps
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ToolShopPage(CommonOps):
    SIGN_IN_NAV = (By.CSS_SELECTOR, "a[data-test='nav-sign-in']")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input[data-test='login-submit']")
    USER_MENU = (By.CSS_SELECTOR, "a[data-test='nav-menu']")
    HOME_BRAND = (By.CSS_SELECTOR, ".navbar-brand")
    SEARCH_BAR = (By.ID, "search-query")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[data-test='search-submit']")
    PRODUCT_CARD = (By.CSS_SELECTOR, "a.card")
    ADD_TO_CART = (By.ID, "btn-add-to-cart")
    NAV_CART = (By.CSS_SELECTOR, "a[data-test='nav-cart']")
    QTY_INPUT = (By.CSS_SELECTOR, "input[data-test='product-quantity']")
    REMOVE_ITEM = (By.CSS_SELECTOR, ".btn-danger")
    SIGNOUT_OPTION = (By.CSS_SELECTOR, "a[data-test='nav-sign-out']")

    def login(self, email, password):
        self.click(self.SIGN_IN_NAV)
        email_el = self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        email_el.clear()
        email_el.send_keys(email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.click(self.LOGIN_BTN)
        # ASSERT: Verify login success
        self.wait.until(EC.url_contains("account"))
        assert "account" in self.driver.current_url, "Assertion Failed: Login redirect did not happen"
        self.click(self.HOME_BRAND)

    def search_and_add(self, item):
        search_box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BAR))
        search_box.clear()
        search_box.send_keys(item)
        self.click(self.SEARCH_BTN)
        time.sleep(2)
        # ASSERT: Verify product appears
        product = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_CARD))
        assert product.is_displayed(), f"Assertion Failed: Product {item} not visible"
        product.click()
        # ASSERT: Verify on product page
        add_btn = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))
        assert add_btn.is_enabled(), "Assertion Failed: Add to Cart button not clickable"
        add_btn.click()

    def manage_cart(self):
        nav_cart_btn = self.wait.until(EC.element_to_be_clickable(self.NAV_CART))
        self.driver.execute_script("arguments[0].click();", nav_cart_btn)
        # ASSERT: Verify Cart loaded
        qty_field = self.wait.until(EC.visibility_of_element_located(self.QTY_INPUT))
        assert qty_field.is_displayed(), "Assertion Failed: Cart page did not load"
        qty_field.send_keys(Keys.CONTROL + "a")
        qty_field.send_keys(Keys.DELETE)
        qty_field.send_keys("2")
        qty_field.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.REMOVE_ITEM))

    def logout_user(self):
        self.driver.refresh()
        self.click(self.USER_MENU)
        signout = self.wait.until(EC.element_to_be_clickable(self.SIGNOUT_OPTION))
        self.driver.execute_script("arguments[0].click();", signout)