from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        # Existing Locators
        self.my_account = (By.XPATH, "//span[text()='My Account']")
        self.register_link = (By.LINK_TEXT, "Register")
        self.firstname = (By.ID, "input-firstname")
        self.country_dropdown = (By.ID, "input-country")
        self.zone_dropdown = (By.ID, "input-zone")
        # New Locators for Part 4
        self.newsletter_yes = (By.XPATH, "//input[@name='newsletter'][@value='1']")
        self.privacy_policy = (By.NAME, "agree")
        self.continue_button = (By.XPATH, "//input[@value='Continue']")

    def navigate_to_register(self):
        self.driver.find_element(*self.my_account).click()
        self.driver.find_element(*self.register_link).click()

    def fill_newsletter_and_privacy(self):
        self.driver.find_element(*self.newsletter_yes).click()
        self.driver.find_element(*self.privacy_policy).click()
        self.driver.find_element(*self.continue_button).click()

    def select_country_and_zone(self, country_name, zone_name):
        Select(self.driver.find_element(*self.country_dropdown)).select_by_visible_text(country_name)
        import time
        time.sleep(2) # Wait for Ajax to load zones
        Select(self.driver.find_element(*self.zone_dropdown)).select_by_visible_text(zone_name)