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
        email_input = self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        assert email_input.is_displayed()
        email_input.clear()
        email_input.send_keys(email)
        pass_input = self.driver.find_element(*self.PASSWORD_FIELD)
        pass_input.send_keys(password)
        assert pass_input.get_attribute("value") == password
        self.click(self.LOGIN_BTN)
        self.wait.until(EC.url_contains("account"))
        assert "account" in self.driver.current_url
        menu = self.wait.until(EC.element_to_be_clickable(self.USER_MENU))
        assert menu.is_displayed()
        self.click(self.HOME_BRAND)
        assert self.wait.until(EC.visibility_of_element_located(self.SEARCH_BAR))

    def search_and_add(self, item):
        search_box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BAR))
        search_box.clear()
        search_box.send_keys(item)
        self.click(self.SEARCH_BTN)
        time.sleep(2)
        product = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_CARD))
        assert product.is_displayed()
        self.driver.execute_script("arguments[0].click();", product)
        add_btn = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))
        assert add_btn.is_displayed()
        add_btn.click()

    def manage_cart(self):
        nav_cart_btn = self.wait.until(EC.presence_of_element_located(self.NAV_CART))
        self.driver.execute_script("arguments[0].click();", nav_cart_btn)
        self.wait.until(EC.url_contains("checkout"))
        assert "checkout" in self.driver.current_url
        qty_field = self.wait.until(EC.visibility_of_element_located(self.QTY_INPUT))
        qty_field.send_keys(Keys.CONTROL + "a")
        qty_field.send_keys(Keys.DELETE)
        qty_field.send_keys("2")
        qty_field.send_keys(Keys.ENTER)
        assert qty_field.get_attribute("value") == "2"
        time.sleep(1)
        delete_btn = self.wait.until(EC.presence_of_element_located(self.REMOVE_ITEM))
        assert delete_btn.is_enabled()
        self.driver.execute_script("arguments[0].click();", delete_btn)

    def logout_user(self):
        self.driver.refresh()
        menu = self.wait.until(EC.element_to_be_clickable(self.USER_MENU))
        assert menu.is_displayed()
        menu.click()
        signout = self.wait.until(EC.element_to_be_clickable(self.SIGNOUT_OPTION))
        assert signout.is_displayed()
        self.driver.execute_script("arguments[0].click();", signout)
        assert self.wait.until(EC.visibility_of_element_located(self.SIGN_IN_NAV))


#$dt = Get-Date -Format "yyyy-MM-dd_HH-mm"; $env:PYTHONPATH="."; pytest tests/test_csv_driven.py -v -s --browser chrome --html="results/Pytest_Capstone_Report_$dt.html" --self-contained-html